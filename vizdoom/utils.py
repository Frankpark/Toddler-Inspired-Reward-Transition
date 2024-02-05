import os
import time


def ensure_shared_grads(model, shared_model, gpu=False):
    for param, shared_param in zip(model.parameters(),
                                   shared_model.parameters()):
        if shared_param.grad is not None and not gpu:
            return
        elif not gpu:
            shared_param._grad = param.grad
        else:
            shared_param._grad = param.grad.cpu()


def check_and_make_dir(dir):
    if not os.path.exists('./'+dir):
        os.mkdir('./' + dir)


def make_dirs(dirs, upper=''):
    for dir in dirs:
        check_and_make_dir(upper + '/' + dir)


def log_to_file(file_path, msg):
    with open(file_path, 'a') as file:
        file.write(msg + '\n')


def format_elapsed_time(elapsed_secs):
    mins, secs = int(elapsed_secs) // 60, int(elapsed_secs) % 60
    hrs, mins = mins // 60, mins % 60
    days, hrs = hrs // 24, hrs % 24
    out = f"{str(days).zfill(2)}D_"
    out += f"{str(hrs).zfill(2)}H_"
    out += f"{str(mins).zfill(2)}M_"
    out += f"{str(secs).zfill(2)}S"
    return out