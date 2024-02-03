from s2d_vizdoom.mazeenv import MazeEnv
import numpy as np
from itertools import count
import cv2
import os
from params import params


output_folder = './interactive_img_dbg/2'
maze_path = params.mazes_path_root +'/0'

if __name__ == '__main__':

    env = MazeEnv.load_vizdoom_env(mazes_path=maze_path,
                                        number_maps=1,
                                        helper_rwd_config=params.helper_rwd_config,
                                        num_obj_to_spawn=len(params.keys_used_list),
                                        action_frame_repeat=params.action_frame_repeat,
                                        scaled_resolution=(480, 600),
                                        living_reward=params.living_reward,
                                        target_reward=params.target_reward,
                                        non_target_penalty=params.non_target_penalty,
                                        timeout_penalty=params.timeout_penalty,
                                        non_target_break=params.non_target_break,
                                        target_break=params.target_break,
                                        min_spawn_dist_from_player=params.min_spawn_dist_from_player)
    env.set_rwd_setting(4)

    if not os.path.isdir(output_folder):
        os.makedirs(output_folder)

    obs = env.reset()
    target = env.get_target_idx()
    target_type = list(params.key_categories.keys())[target]
    print('start, target {}, {}'.format(target, target_type))
    total_reward = 0.0
    convert_img = True
    save_img_idx = 0
    for t in count():
        if convert_img:
            obs = obs[-1,:-1]
            obs = np.transpose(obs, (1, 2, 0))
            obs = cv2.cvtColor(obs, cv2.COLOR_BGR2RGB)
            cv2.imshow('window', obs)

        convert_img = True
        key = cv2.waitKey(0)
        if key == ord('q'):
            break
        elif key == ord('1'):
            obs, reward, dones, info = env.step(0)
        elif key == ord('2'):
            obs, reward, dones, info = env.step(1)
        elif key == ord('3'):
            obs, reward, dones, info = env.step(2)
        elif key == ord('r'):
            obs = env.reset()
            target = env.get_target_idx()
            print('manual reset, target {}'.format(target))
            continue
        elif key == ord('s'):
            path = '{}/{}.png'.format(output_folder, save_img_idx)
            while os.path.isfile(path):
                save_img_idx += 1
                path = '{}/{}.png'.format(output_folder, save_img_idx)
            cv2.imwrite(path, obs)
            print('image saved to path {}'.format(path))
            save_img_idx += 1
            convert_img = False
            continue
        else:
            convert_img = False
            continue
        total_reward += reward
        print('total reward: {}, dones: {}, info: {}'.format(total_reward, dones, info))
        if dones:
            obs = env.reset()
            target = env.get_target_idx()
            print('new episode, target {}'.format(target))
