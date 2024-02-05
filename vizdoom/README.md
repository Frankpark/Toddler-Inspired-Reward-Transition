# ViZDoom Experiments for Toddler-Inspired Reward Transition
This directory includes the source code and environments for running the toddler-inspired reward transition experiments on ViZDoom-Seen and ViZDoom-Unseen.

## Installation
Usage of [Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) is recommended, and the current installation guide is centered around Conda.

1. Install the dependencies for [ViZDoom](https://github.com/Farama-Foundation/ViZDoom) as below.
```
apt-get update
apt-get install build-essential zlib1g-dev libsdl2-dev libjpeg-dev \
tar libbz2-dev libgtk2.0-dev cmake libfluidsynth-dev libgme-dev \
libopenal-dev timidity libwildmidi-dev unzip libboost-all-dev
```

2. Create a Conda environment and activate it.
```
conda create -n vzd python=3.8.10
conda activate vzd
```

3. Compile ACC, which is used to compile ACS scripts into ViZDoom environments.
```
git submodule update --init
make -C env/s2d_vizdoom/mazeenv/acc
```

4. Install PyTorch according to the official documentation ([link](https://pytorch.org/get-started/locally/)).

5. Install other requirements from `requirements.txt`.
```
pip install -r requirements.txt
```

6. Install the environment.
```
cd env
pip install -e .
```

For the versions of dependencies, please refer to `requirements.txt`. Also, experiments were run under below additional settings:
- Python 3.8.10
- PyTorch 2.1.2+cu118

## Running Experiments
Check the arguments in `params.py`. Particularly, pay attention to the following arguments:
- `self.num_train_processes` and `self.gpu_ids_train` define how many processes and which GPUs should be used for training. The processes will be split evenly among the list of GPUs specified. These arguments should be set according to the number of GPUs and the amount of GPU VRAM in your machine.
- `self.gpu_ids_test` defines which GPUs should be used for evaluation. Note that one process is allocated to Seen environment and one process is allocated to Unseen environment.
- `self.max_updates` and `self.curriculum` define the reward transitions during this experiment. Currently, the arguments are set to default settings for sparse-to-dense (S2D) transition. Also note that reward setting 1 corresponds to the sparse reward and reward setting 5 corresponds to the dense reward used in the ViZDoom Seen & Unseen experiments in the paper.

Afterwards, execute `python main.py`, and results will be yielded in the `log` directory in the form of CSV files.

The results can be plotted using `plot/plot_seenunseen.py`. It should be noted that the paths to the correct CSV files should be entered into the `file_names` entries of `plot/config_seenunseen.json`. Then, run `python plot/plot_seenunseen.py` to obtain the plot, which is saved in the directory `plot/out`.

## TODO List
- [ ] Clean up the map generation script; make them readable
- [ ] Resolve deprecation warnings that involve the usage of `autograd.Variable`
- [ ] Enable providing arguments via `argparse`

## References

The ViZDoom environment codes are modified versions of `microsoft/MazeExplorer` repository ([link](https://github.com/microsoft/MazeExplorer)) and `lionminhu/maze_env` repository ([link](https://github.com/lionminhu/maze_env)). A significant portion of the training and evaluation code is modified version of the corresponding source code from `kibeomKim/House3D_baseline` repository ([link](https://github.com/kibeomKim/House3D_baseline)). The details are listed in `NOTICE`.