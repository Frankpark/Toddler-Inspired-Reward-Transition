from gym.envs.registration import register

register(
    id="s2d_vizdoom/nav-v0",
    entry_point="s2d_vizdoom.mazeenv:VizDoom",
)
