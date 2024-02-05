# This module contains common functions for plotting multiple models' learning
# curves into one plot.

import matplotlib
matplotlib.use("Agg") # Save as PNG
import matplotlib.pyplot as plt
import matplotlib.ticker as tick

import numpy as np
import os
import json


def default_parse(file_name):
    """
    Default function for parsing a given file containing the performance of a
    model into list of x and y values.
    This assumes that the data points are given from second line of the file,
    and every line is formatted as "x_value y_value".
    """
    with open(file_name, "r") as in_file:
        lines = in_file.readlines()

    x_list = []
    y_list = []

    for line in lines[1:]:
        x, y = line.split()
        x = float(x)
        y = float(y)
        x_list.append(x)
        y_list.append(y)

    return x_list, y_list


# This function is coded by Dan Friedman, 2020, from
# https://dfrieds.com/data-visualizations/how-format-large-tick-values.html
def reformat_large_tick_values(tick_val, pos):
    """
    Turns large tick values (in the billions, millions and thousands) such as
    4500 into 4.5K and also appropriately turns 4000 into 4K (no zero after the
    decimal).
    """
    if tick_val >= 1000000000:
        val = round(tick_val/1000000000, 2)
        new_tick_format = "{:}B".format(val)
    elif tick_val >= 1000000:
        val = round(tick_val/1000000, 2)
        new_tick_format = "{:}M".format(val)
    elif tick_val >= 1000:
        val = round(tick_val/1000, 2)
        new_tick_format = "{:}K".format(val)
    elif tick_val < 1000:
        new_tick_format = round(tick_val, 2)
    else:
        new_tick_format = tick_val

    # make new_tick_format into a string value
    new_tick_format = str(new_tick_format)

    # code below will keep 4.5M as is but change values such as 4.0M to 4M
    # since that zero after the decimal isn't needed
    index_of_decimal = new_tick_format.find(".")

    if index_of_decimal != -1:
        value_after_decimal = new_tick_format[index_of_decimal+1]
        if value_after_decimal == "0":
            # remove the 0 after the decimal point since it's not needed
            new_tick_format = new_tick_format[0:index_of_decimal] + \
                new_tick_format[index_of_decimal+2:]

    return new_tick_format


def get_interpolated_data(query_xs, data_x, data_y):
    """
    Using original data points (x,y) given by `data_x` and `data_y`,
    produce new data points where the x values are given by `query_xs` and
    y values are interpolated.

    Argument(s):
    - query_xs: List of x values to interpolate to. Assumes that query_xs is
                in increasing order.
    - data_x:   List of original x values
    - data_y:   List of original y values

    Return(s):
    - List of x values to which new y values are interpolated. Identical to
      `query_xs`, except that those values outside the range of `data_x` are
      ignored.
    - List of interpolated y values.
    """

    def interpolate(query_x, data_x, data_y):
        # print(f"*** interpolate 1: query_x {query_x}, data_x {data_x}")
        if query_x < data_x[0]:
            return "low"
        # Linear interpolation between two nearest neighbours
        for idx in range(len(data_x) - 1):
            if query_x <= data_x[idx + 1] and query_x >= data_x[idx]:
                slope = (data_y[idx + 1] - data_y[idx]) / (data_x[idx + 1] - \
                    data_x[idx])
                return data_y[idx] + (query_x - data_x[idx]) * slope
        return None

    inter_xs = []
    inter_ys = []

    for query_x in query_xs:
        inter_y = interpolate(query_x, data_x, data_y)

        # Ignore x points out of range (too low)
        if inter_y == "low":
            continue

        # Return if x point beyond the range (too high)
        if inter_y is None:
            return inter_xs, inter_ys

        inter_xs.append(query_x)
        inter_ys.append(inter_y)

    return inter_xs, inter_ys


def convert_to_color_blind(colors):
    """
    Convert given colors to color-blind-friendly counterparts.
    """
    color_dict = {
        "blue": "#4477aa", "cyan": "#66ccee", "green": "#228833",
        "yellow": "#ccbb44", "red": "#ee6677", "purple": "#aa3377",
        "grey": "#bbbbbb", "orange": "#ee8866"
    }
    color_blind_colors = [(color_dict[c] if c in color_dict else c) for c in \
        colors]
    return color_blind_colors


def get_curve(file_list, interval, min_inter_x, max_inter_x,
    parse_func=default_parse):
    """
    Given a list of file paths for a model, each containing a trial, return
    mean/standard deviation across the trials.
    """

    # x values to interpolate to
    inter_xs = list(range(min_inter_x, max_inter_x, interval))
    # List to contain interpolated y values
    inter_ys_list = []

    # Get interpolated y values for each file
    for file_name in file_list:
        # print(f"*** get_curve 0.1: {file_name}")
        data_x, data_y = parse_func(file_name)
        # print(f"*** get_curve 1: {len(data_x)}, {len(data_y)}, {len(inter_xs)}")
        inter_xs, inter_ys = get_interpolated_data(inter_xs, data_x, data_y)
        inter_ys_list.append(inter_ys)

    # Calculate mean and std
    out_data_y = np.array([y[:len(inter_xs)] for y in inter_ys_list])
    mean_y = out_data_y.mean(0)
    std_y = out_data_y.std(0)

    return inter_xs, mean_y, std_y


def draw_plots(file_names, result_png_path, config, exp_note="", parse_func=default_parse):

    # Create directory for output file.
    result_png_path_dir = result_png_path[:result_png_path.rindex("/")]
    os.makedirs(result_png_path_dir, exist_ok=True)

    _config = {
        "exp_note": exp_note,
        "file_names": file_names,
        "result_png_path": result_png_path
    }
    _config.update(config)
    log_ctn = json.dumps(_config, indent=2)
    log_path = result_png_path[:result_png_path.rindex(".png")] + ".log"
    with open(log_path, "w") as out_file:
        out_file.write(log_ctn)

    # Declare config values as those from config dict or some default values
    min_inter_x = _config["min_updates"]
    max_inter_x = _config["max_updates"]
    interval = _config["interval"]
    font_size = _config.get("font_size", 16)
    fig_size = _config.get("fig_size", [7, 5])
    colors = _config.get("colors", None)
    linestyles = _config.get("linestyles", None)
    color_blind = _config.get("color_blind", True)
    line_width = _config.get("line_width", 2)
    x_label = _config.get("x_label", "x")
    y_label = _config.get("y_label", "y")
    use_legend = _config.get("use_legend", True)
    legend_loc = _config.get("legend_loc", "upper left")
    xlim = _config["xaxis_bound"]
    ylim = _config.get("yaxis_bound", None)
    tick_format = _config.get("tick_format", True)
    draw_grid = _config.get("draw_grid", True)

    # Set font size
    plt.rcParams.update({
        "font.size": font_size,
        "figure.figsize": fig_size,
    })

    # Default colors
    if colors is None:
        colors = ["red", "blue", "purple", "yellow", "green"]
    
    if len(colors) < len(file_names):
        raise ValueError("Not enough colors to cover all curves.")

    # Convert to color-blindness-friendly colors
    if color_blind is True:
        colors = convert_to_color_blind(colors)

    if linestyles is None:
        linestyles = ["solid" for _ in range(len(colors))]

    # Initialize plots
    fig, ax = plt.subplots(1)

    # Iterate for every model
    for model_idx in range(len(file_names)):
        model_name = list(file_names.keys())[model_idx]

        # x values to interpolate to
        inter_xs = list(range(min_inter_x, max_inter_x, interval))

        # Ignore model with no file provided
        if len(file_names[model_name]) == 0:
            continue

        # Get mean and std across files of the model
        # print(f"*** draw_plots 1: {y_label}, {len(inter_xs)}")
        inter_xs, mean_y, std_y = get_curve(file_names[model_name], interval,
            min_inter_x, max_inter_x, parse_func=parse_func)

        # Draw mean
        ax.plot(inter_xs, mean_y, color=colors[model_idx], linestyle=linestyles[model_idx], \
            label=model_name, linewidth=line_width)

        # Indicate standard deviation
        upper_y = mean_y + std_y
        lower_y = mean_y - std_y
        ax.fill_between(inter_xs, lower_y, upper_y, color=colors[model_idx], \
            alpha=0.3)

    ax.ticklabel_format(axis="x", style="sci", scilimits=(0, 0))

    # Set axes labels
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    # Add legend
    if use_legend is True:
        ax.legend(loc=legend_loc)

    # Draw grid
    if draw_grid is True:
        ax.grid(visible=True, which="major", axis="both", color="#aaaaaa", \
            linestyle="-")

    # Set boundaries
    if xlim is not None:
        plt.xlim(xlim)
    if ylim is not None:
        plt.ylim(ylim)

    # Display in thousands, millions, billions
    if tick_format is True:
        ax.xaxis.set_major_formatter(tick.FuncFormatter(
            reformat_large_tick_values))

    # Save the figure
    fig.savefig(result_png_path)


def check_best_perf(file_names, config, log_path, exp_note, parse_func=default_parse):

    _config = {
        "exp_note": exp_note,
        "file_names": file_names,
        "result_png_path": log_path
    }
    _config.update(config)
    # log_ctn = json.dumps(_config, indent=2)
    # log_path = log_path[:log_path.rindex(".png")] + ".log"
    # with open(log_path, "w") as out_file:
    #     out_file.write(log_ctn)

    with open(log_path, "w") as _:
        pass

    min_inter_x = _config["min_updates"]
    max_inter_x = _config["max_updates"]
    interval = _config["interval"]
    
    for model_idx in range(len(file_names)):
        model_name = list(file_names.keys())[model_idx]
        if len(file_names[model_name]) == 0:
            continue

        xs, mean_ys, std_ys = get_curve(file_names[model_name], interval,
            min_inter_x, max_inter_x, parse_func=parse_func)

        best_idx = None
        best_y = None
        for idx, y in enumerate(mean_ys.tolist()):
            if best_y is None or y > best_y:
                best_idx = idx
                best_y = y

        best_x = xs[best_idx]
        best_std_y = std_ys[best_idx]

        # msg = '{}: {:.1f} $\pm$ {:.1f} (at {} steps)'.format(model_name,
        #     best_y * 100, best_std_y * 100, best_x)
        msg = '{}: {:.3f} (at {} steps)'.format(model_name, best_y, best_x)
        with open(log_path, 'a') as out_file:
            out_file.write(msg + '\n')
        print(msg)
