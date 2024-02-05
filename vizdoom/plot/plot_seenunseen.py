from collections import OrderedDict
from datetime import datetime
import argparse
import json
from plot_tb import draw_plots, check_best_perf
from copy import deepcopy

parser = argparse.ArgumentParser()
parser.add_argument("--debug", default="False")
args = parser.parse_args()
debug = False if args.debug == "False" else True

# Plotting parameters
output_folder_prefix = "out/"
output_folder_suffix = ""

input_json_path = "config_seenunseen.json"

with open(input_json_path, 'r') as in_file:
    input_json = json.load(in_file)


def provide_file_names(task):
    file_names = OrderedDict(input_json["tasks"][task]["file_names"])
    model_order = input_json["tasks"][task]["order"]
    for model_name in model_order:
        file_names.move_to_end(model_name)
    return file_names


def parse_func_success_rate(file_name, seen):
    with open(file_name, 'r') as in_file:
        lines = in_file.readlines()

    x_list = []
    y_list = []

    keep_continuing = True

    for line in lines:
        if keep_continuing:
            if len(line.split()) > 0 and line.split()[0] == "time":
                keep_continuing = False
            continue
        maze_id = int(line.split()[2])
        if (seen and maze_id != 0) or (not seen and maze_id != 1):
            continue
        x = float(line.split()[1])
        y = float(line.split()[6]) / 100.   # success rate
        # y = float(line.split()[4])     # reward
        x_list.append(x)
        y_list.append(y)

    return x_list, y_list

def parse_func_reward(file_name, seen):
    with open(file_name, 'r') as in_file:
        lines = in_file.readlines()

    x_list = []
    y_list = []

    keep_continuing = True

    for line in lines:
        if keep_continuing:
            if len(line.split()) > 0 and line.split()[0] == "time":
                keep_continuing = False
            continue
        maze_id = int(line.split()[2])
        if (seen and maze_id != 0) or (not seen and maze_id != 1):
            continue
        x = float(line.split()[1])
        # y = float(line.split()[6]) / 100.   # success rate
        y = float(line.split()[4])     # reward
        x_list.append(x)
        y_list.append(y)

    return x_list, y_list


if __name__ == "__main__":
    output_folder = output_folder_prefix
    if debug is True:
        output_folder += "dbg"
    else:
        output_folder += datetime.now().strftime("%Y%m%d_%H%M%S")
        output_folder += output_folder_suffix

    exp_note = input_json["exp_note"]

    for task, config in input_json["tasks"].items():
        print("task: {}".format(task))
        file_names = provide_file_names(task)

        # For using different y axis bounds for seen and unseen
        _yaxis_bounds = deepcopy(config["yaxis_bound"])

        for seen in [True, False]:
            if type(_yaxis_bounds) == dict:
                config["yaxis_bound"] = _yaxis_bounds["seen" if seen else "unseen"]

            seen_str = "seen" if seen else "unseen"
            result_png_path = "./{}/{}_{}.png".format(output_folder, task, seen_str)

            if task == "success_rate":
                parse_func = lambda f: parse_func_success_rate(f, seen)
            else:
                parse_func = lambda f: parse_func_reward(f, seen)
            draw_plots(file_names, result_png_path, config, exp_note, parse_func)

            print("Plot saved to {}".format(result_png_path))

        # result_png_path = f"./{output_folder}/{task}_best_perf.txt"
        # check_best_perf(file_names, config, result_png_path, exp_note, parse_func)
