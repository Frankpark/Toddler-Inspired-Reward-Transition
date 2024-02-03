from collections import OrderedDict
import time
import os
import datetime
import git


class Params:
    def __init__(self):
        # suffix for labeling the log file name
        self.suffix = "vzd_seen_unseen_default"
        # Do not change
        self.date_str = f"{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}_{self.suffix}"
        # Map name
        self.map_str = "main_seen_unseen"

        ########## Configs for running trains/test ##########
        self.exp_note = """
            Default setting for Vizdoom seen & unseen experiment
        """

        # Number of workers for training/testing
        self.num_train_processes = 20
        self.num_test_processes = 2

        # number of episodes for each evaluation
        self.n_eval = 1000

        # number of steps between training updates
        self.num_steps_bw_updates = 200

        # GPUs to allocate for train/test
        self.gpu_ids_train = [0, 1, 2, 3]
        self.gpu_ids_test = [0, 1]

        # NOTE: this is a different seed from `gen_map_seed` used for generating maps
        self.seed = 0

        # maze 0 is the "seen" and maze 1 is unseen
        self.train_mazes = [0]
        self.eval_mazes = [0, 1]

        # root directory for saving generated maps. DO NOT CHANGE
        self.mazes_path_root = './maps/{}/'.format(self.map_str)

        # Transition experiment settings.
        # `max_updates` is the total number of updates to train.
        # `curriculum` is a list of 2-tuples (int, int). The first index is the time
        # (in updates) to transition to next reward setting, and the second
        # index is the reward setting.
        # Note that the reward setting 1 corresponds to sparse reward and
        # reward setting 5 corresponds to dense reward, for the Vizdoom Seen&Unseen
        # experiments reported in the paper.
        # Example: max_updates 1100000, curriculum [(50000, 1), (1100000, 5)]
        #          means to use setting 1 until 50k updates, and then
        #          setting 5 until 1.1M updates (which is the end of the
        #          experiment in this case).
        self.max_updates = 1100000
        self.curriculum = [
            (50000, 1), (1100000, 5)
        ]

        ########## Logging-related ##########
        # log file name
        self.log_file = self.date_str

        # directory to save wgt files
        self.weight_dir = './wgt/{}_wgt/'.format(self.date_str)

        # log file name for gen_map
        self.gen_maps_log_file = '{}_gen_map'.format(self.map_str)

        self.log_debug = False

        # intervals for saving weights checkpoint file
        self.save_param_interval = 200000

        # log current git commit hash
        repo = git.Repo(search_parent_directories=True)
        self.git_commit_hash = repo.head.object.hexsha

        ########## Model/optimizer hyperparameters ##########
        self.gamma = 1.0
        self.def_entropy_coef = 0.1
        self.st1_entropy_coef = 0.1
        self.lr = 7e-5
        self.tau = 1.0
        self.clip_grad_norm = 10.0
        self.value_loss_coef = 0.5
        self.amsgrad = True
        self.weight_decay = 0  # do not change

        ########## Configuration for `gen_maps.py` ##########
        # Note that these parameters are not used for the experiment script `main.py`.

        # NOTE: this is a different seed from `seed` that is used for running agent
        self.gen_map_seed = 0

        # max number of time steps for each episode * 4
        # due to 4-frame stack, 400 time steps for agent is 1600 time steps within
        # the environment
        self.episode_timeout = 200

        self.resolution = 'RES_160X120'
        #self.resolution = 'RES_640X480'  # DEBUG

        self.acs_script = 'quartile_acs_template_2.txt'
        self.gen_maps_dir_prefix = self.map_str

        # whether to randomize player spawn position at the start of every episode
        self.random_player_spawn = False

        # default position for player to spawn on when `random_player_spawn` is False.
        # setting to None will let the player spawn position be fixed at random position
        self.def_player_spawn_pos = (790, 790)

        # whether to randomize player spawn angle at the start of every episode
        self.random_player_spawn_angle = True

        # default player spawn angle for when `random_player_spawn_angle` is False
        self.def_player_spawn_angle = None

        # whether to randomly sample background texture every episode
        self.random_wall_texture = True
        self.random_ceiling_texture = False
        self.random_floor_texture = False

        # list of textures to randomly sample every episode
        self.wall_texture_list = ["ZIMMER8", "WOOD8", "MODWALL2"]
        self.ceiling_texture_list = ["CEIL5_1"]
        self.floor_texture_list = ["CEIL5_2"]

        # whether to randomize object position every episode
        self.random_key_positions = True

        # default positions for object spawns when `random_key_positions` is False
        self.def_key_pos = None

        # setting this to True will shuffle object positions among default
        # positions or boxes
        self.shuffle_obj_pos = True

        # whether to use random object textures every episode
        self.random_key_textures = True

        # types of objects
        self.key_categories = OrderedDict({
            "Card": ["RedCard", "BlueCard", "YellowCard"],
            "Skull": ["YellowSkull", "BlueSkull", "RedSkull"],
        })
        self.keys_used_list = [0, 1]

        self.map_size = (7, 7)
        self.complexity = 0
        self.density = 0

        # can specify maze layout explicitly in 2D grid, where ` ` is empty space and
        # `X` is a wall
#         self.maze_layout = """XXXXXXXXX
# X    X  X
# X    X  X
# X    X  X
# X  X X  X
# X  X    X
# X  X    X
# X  X    X
# XXXXXXXXX"""
        self.maze_layout = None

        # dividing the map into boxes, where at most one object spawns in each box
        self.use_key_boxes = True
        self.boxes_dims = (2, 2)

        self.min_spawn_dist_from_player = 200.0

        ########## Gym environment settings ##########
        self.reward_clip = (-10.0, 10.0)
        self.action_frame_repeat = 4  # hardcoded. please do not modify
        self.scaled_resolution = (42, 42)
        self.data_augmentation = False
        self.living_reward = -0.0025   # 4-frame stack, so living reward is quadrupled
        self.target_reward = 10.0
        self.non_target_penalty = 1.0
        self.non_target_break = True
        self.target_break = True
        self.timeout_penalty = 0.1
        self.helper_rwd_config = {
            2: {
                "rwd": 5.0,
                "max_dist": 200.0,
            },
            3: {
                "rwd": 5.0,
                "max_dist": 200.0,
                "non_target_rwd": -5.0,
                "non_target_max_dist": 200.0,
            },
            4: {
                "rwd_scale": 5 / 800,
            },
            5: {
                "rings": [
                    {"rwd": 2.5, "max_dist": 150.0},
                    {"rwd": 5.0, "max_dist": 100.0},
                ]
            },
        }


params = Params()
debug_log_path = './log/' + params.log_file + '.log'


def log_params(is_gen_maps=False):
    if is_gen_maps:
        path = './log/{}'.format(params.gen_maps_log_file)
    else:
        path = './log/{}'.format(params.log_file)

    msg = str('start time\t{}\n'.format(time.strftime('%X %x %Z')))

    params_dict = params.__dict__
    for key in params_dict.keys():
        msg += '{}\t{}\n'.format(key, str(params_dict[key]))

    msg += '\n' + '\t'.join(['time', 'numUpdates', 'mazeId', 'saveModelIdx',
                             'avgReward', 'avgLength', 'successRate',
                             'bestRate']) + '\n'
    csv_path = path + '.csv'
    if not os.path.isdir('./log'):
        os.mkdir('./log')
    # commented out as DEBUG
    # if os.path.isfile(csv_path):
    #     raise ValueError('Log CSV file already exists')
    with open(csv_path, 'w') as file:
        file.write(msg)

    if params.log_debug:
        msg = str('start time\t{}\n'.format(time.strftime('%X %x %Z')))
        msg += '\n' + '\t'.join(['rank', 'episode', 'maze_id', 'total_rew', 'step', 'good', \
            'n_update', 'action', 'value', 'logit', 'prob', 'rew', 'done', 'info']) + '\n'
        with open(path + '.log', 'w') as file:
            file.write(msg)
