import torch
from torch.autograd import Variable
import numpy as np

from setproctitle import setproctitle as ptitle

from models import A3C_LSTM_GA
from s2d_vizdoom.mazeenv import MazeEnv
from agent import A3CAgent

import os

params = None

def run_sim(rank, shared_model, shared_optimizer, count, lock, _params):
    global params
    params = _params
    # Set up logging
    os.makedirs('./'+params.weight_dir, exist_ok=True)
    os.makedirs('./log', exist_ok=True)

    # Change process title
    ptitle('Training {}'.format(rank))

    # Set GPU for current instance/process
    gpu_id = params.gpu_ids_train[rank % len(params.gpu_ids_train)]

    if shared_optimizer is None:
        print("\nshared_optimizer is None\n")

    # Set seed
    torch.manual_seed(params.seed + rank)
    if gpu_id >= 0:
        torch.cuda.manual_seed(params.seed + rank)

    # Load MazeEnv environment
    maze_id = params.train_mazes[rank % len(params.train_mazes)]
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

    n_update = 0
    phase_idx = 0
    next_transition_time, rwd_setting = params.curriculum[phase_idx]

    while n_update < params.max_updates:
        while n_update >= next_transition_time:
            phase_idx += 1
            next_transition_time, rwd_setting = params.curriculum[phase_idx]
        env.set_rwd_setting(rwd_setting)
        # for ablation on entropy coefficient
        # entropy_coef = params.st1_entropy_coef if rwd_setting == 1 else params.def_entropy_coef
        entropy_coef = params.def_entropy_coef
        training(env, gpu_id, shared_model, agent, shared_optimizer, lock, count, entropy_coef)
        with lock:
            n_update = count.value


def training(env, gpu_id, shared_model, agent, optimizer, lock, count, entropy_coef):
    next_obs = env.reset()
    target = env.get_target_idx()
    target = torch.from_numpy(np.array(target)).view(1, -1)

    with torch.cuda.device(gpu_id):
        target = Variable(torch.LongTensor(target)).cuda()
        agent.model.load_state_dict(shared_model.state_dict())
        agent.cx = Variable(torch.zeros(1, 256).cuda())
        agent.hx = Variable(torch.zeros(1, 256).cuda())
        agent.target = target

    num_steps = 0
    agent.done = False
    done = False

    while not done:
        num_steps += 1
        obs = next_obs
        act, entropy, value, log_prob, _ = agent.action_train(obs, target)
        next_obs, reward, done, _ = env.step(act[0])
        agent.put_reward(reward, entropy, value, log_prob)
        if done:
            agent.done = True
        if done or (num_steps % params.num_steps_bw_updates == 0):
            with lock:
                count.value += 1
            agent.training(next_obs, target, shared_model, optimizer, entropy_coef)

