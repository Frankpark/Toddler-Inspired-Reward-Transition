import torch
from torch.autograd import Variable

import logging
from setproctitle import setproctitle as ptitle

from models import A3C_LSTM_GA
from s2d_vizdoom.mazeenv import MazeEnv
from agent import A3CAgent
from utils import format_elapsed_time

import os
import time
import datetime

params = None


def test(rank, shared_model, shared_optimizer, count, lock, _params, start_time):
    global params
    params = _params

    # Set up logging
    os.makedirs('./'+params.weight_dir, exist_ok=True)
    os.makedirs('./log', exist_ok=True)
    logging.basicConfig(filename='./log/'+params.log_file+'.log', level=logging.INFO)

    # Change process title
    ptitle('Testing {}'.format(rank))

    # Set GPU for current instance/process
    gpu_id = params.gpu_ids_test[rank % len(params.gpu_ids_test)]

    if shared_optimizer is None:
        print("\nshared_optimizer is None\n")

    # Set seed
    torch.manual_seed(params.seed + rank)
    if gpu_id >= 0:
        torch.cuda.manual_seed(params.seed + rank)

    # Load MazeEnv environment
    maze_id = params.eval_mazes[rank % len(params.eval_mazes)]
    maze_path = params.mazes_path_root + str(maze_id)
    env = MazeEnv.load_vizdoom_env(mazes_path=maze_path,
                                   number_maps=1,
                                   helper_rwd_config=params.helper_rwd_config,
                                   num_obj_to_spawn=len(params.keys_used_list),
                                   action_frame_repeat=params.action_frame_repeat,
                                   scaled_resolution=params.scaled_resolution,
                                   living_reward=params.living_reward,
                                   target_reward=params.target_reward,
                                   non_target_penalty=params.non_target_penalty,
                                   timeout_penalty=params.timeout_penalty,
                                   non_target_break=params.non_target_break,
                                   target_break=params.target_break)

    # Initialize model
    model = A3C_LSTM_GA()
    with torch.cuda.device(gpu_id):
        model = model.cuda()

    # Initialize agent
    agent = A3CAgent(model, gpu_id)

    now = datetime.datetime.now()
    now_date = now.strftime("%Y%m%d-%H%M%S")
    # writer = SummaryWriter(f"runs/{now_date}_{self.log_file}")

    best_rate = 0.0
    save_model_index = 0
    # Last time (num of updates) the weights ckpt was saved
    last_update_save_wgt = -1 * params.save_param_interval
    n_update = 0
    phase_idx = 0
    next_transition_time, rwd_setting = params.curriculum[phase_idx]

    while n_update < params.max_updates:
        while n_update >= next_transition_time:
            phase_idx += 1
            next_transition_time, rwd_setting = params.curriculum[phase_idx]

        env.set_rwd_setting(rwd_setting)
        with torch.cuda.device(gpu_id):
            agent.model.load_state_dict(shared_model.state_dict())

        best_rate, save_model_index = testing(rank, env, maze_id, gpu_id, agent, n_update, lock,
                                              best_rate, save_model_index, start_time, logging,
                                              last_update_save_wgt)

        with lock:
            n_update = count.value


def testing(rank, env, maze_id, gpu_id, agent, n_update, lock, best_rate, save_model_index, start_time,
        logging, last_update_save_wgt):
    evals = []
    agent.model.eval()

    for _ in range(params.n_eval):
        next_obs = env.reset()
        target = env.get_target_idx()

        with torch.cuda.device(gpu_id):
            target = Variable(torch.LongTensor([target])).cuda()
            agent.cx = Variable(torch.zeros(1, 256)).cuda()
            agent.hx = Variable(torch.zeros(1, 256)).cuda()
            agent.target = target

        step, total_rew, good = 0, 0, 0
        done = False

        while not done:
            obs = next_obs
            act, *_ = agent.action_test(obs, target)
            next_obs, rew, done, info = env.step(act[0])
            total_rew += rew

            if info[3]['success'] is True:
                good = 1

            step += 1

        evals.append((step, total_rew, good))

    if len(evals) > 0:
        success = [e for e in evals if e[2] > 0]
        success_rate = (len(success) / len(evals)) * 100.

        with lock:
            if n_update - last_update_save_wgt >= params.save_param_interval:
                if success_rate > best_rate:
                    best_rate = success_rate
                with torch.cuda.device(gpu_id):
                    torch.save(agent.model.state_dict(),
                               params.weight_dir + 'model' + str(n_update) + '.ckpt')
                save_model_index += 1

        avg_reward = sum([e[1] for e in evals]) / len(evals)
        avg_length = sum([e[0] for e in evals]) / len(evals)

        time_str = format_elapsed_time(time.time() - start_time)

        msg = ' '.join([
            "++++++++++ Task Stats +++++++++++\n",
            "Time {}\n".format(time_str),
            "Episode Played: {:d}\n".format(len(evals)),
            "N_Update = {:d}\n".format(n_update),
            "Maze id: {:d}\n".format(maze_id),
            "Avg Reward = {:5.3f}\n".format(avg_reward),
            "Avg Length = {:.3f}\n".format(avg_length),
            "Best rate {:3.2f}, Success rate {:3.2f}%".format(best_rate, success_rate)
        ])

        print(msg)
        logging.info(msg)

        csv_path = './log/' + params.log_file + '.csv'
        log_list = [
            time_str, n_update, maze_id, save_model_index, avg_reward, avg_length,
            success_rate, best_rate
        ]
        log_list = [str(e) for e in log_list]
        csv_msg = '\t'.join(log_list)
        csv_msg += '\n'
        with open(csv_path, 'a') as file:
            file.write(csv_msg)

    return best_rate, save_model_index
