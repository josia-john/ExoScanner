# This file implements some standard-algorithms which are used all over the
# program. Currently there is only a function which calculates the rolling
# average over data.

import os, sys, subprocess

def rolling(numbers, window_size):
    i = 0
    moving_averages = []
    this_window = sum(numbers[0:window_size])
    while i < len(numbers) - window_size:
        moving_averages.append(this_window/window_size)

        this_window += numbers[i+window_size]
        this_window -= numbers[i]
        i += 1

    moving_averages.append(this_window/window_size)

    return moving_averages


def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])
        