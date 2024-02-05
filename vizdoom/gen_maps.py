import random

from s2d_vizdoom.mazeenv import MazeEnv

from params import Params, log_params
from utils import check_and_make_dir


if __name__ == '__main__':
    params = Params()
    log_params(is_gen_maps=True)
    num_trials = 0

    check_and_make_dir('maps')

    path = 'maps/{}'.format(params.gen_maps_dir_prefix)
    check_and_make_dir(path)

    if params.gen_map_seed is not None:
        seed = params.gen_map_seed
    else:
        seed = None

    for idx in range(params.num_maps):
        # keep trying to generate the map, changing seed if necessary
        while True:
            try:
                num_trials += 1
                if seed is not None:
                    seed += 1
                random.seed(seed)

                map_path = '{}/{}'.format(path, idx)

                MazeEnv(unique_maps=False,
                        number_maps=1,
                        size=params.map_size,
                        random_spawn=params.random_player_spawn,
                        random_key_positions=params.random_key_positions,
                        seed=seed,
                        clip=params.reward_clip,
                        random_wall_texture=params.random_wall_texture,
                        random_floor_texture=params.random_floor_texture,
                        random_ceiling_texture=params.random_ceiling_texture,
                        wall_texture_list=params.wall_texture_list,
                        floor_texture_list=params.floor_texture_list,
                        ceiling_texture_list=params.ceiling_texture_list,
                        episode_timeout=params.episode_timeout,
                        complexity=params.complexity,
                        density=params.density,
                        data_augmentation=params.data_augmentation,
                        mazes_path=map_path,
                        key_categories=params.key_categories,
                        random_key_textures=params.random_key_textures,
                        maze_layout=params.maze_layout,
                        default_spawn_pos=params.def_player_spawn_pos,
                        default_key_pos=params.def_key_pos,
                        resolution=params.resolution,
                        acs_path=params.acs_script,
                        keys_used_list=params.keys_used_list,
                        use_key_boxes=params.use_key_boxes,
                        boxes_dims=params.boxes_dims,
                        shuffle_obj_pos=params.shuffle_obj_pos,
                        random_player_spawn_angle=params.random_player_spawn_angle,
                        def_player_spawn_angle=params.def_player_spawn_angle,
                        gen_map=True,
                        min_spawn_dist_from_player=params.min_spawn_dist_from_player)

                break

            except AssertionError:
                print("***gen_maps: invalid object/player spawn positions. trying another seed...")

    print("{} maps generated in {} trials!".format(params.num_maps, num_trials))