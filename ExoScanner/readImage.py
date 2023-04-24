# This file is responsible for reading images from files. Theoretically cr2
# (canon raw) is supported. But the file "getTimeOfFile.py" breaks that
# support.
# The function bin() allows for the data to be binned. That is useful when the
# image is bayered (color-cameras).

import os
from astropy.io import fits
import numpy as np

import ExoScanner.config

def rebin(arr, new_shape):
    """Rebin 2D array arr to shape new_shape by averaging."""
    shape = (new_shape[0], arr.shape[0] // new_shape[0],
             new_shape[1], arr.shape[1] // new_shape[1])
    return arr.reshape(shape).mean(-1).mean(1)

def bin(rgb, size):
    rgb = np.array(rgb)
    newRGB = rebin(rgb, (int(len(rgb)/size), int(len(rgb[0])/size)))
    return newRGB

def readImage(filename, binning = 1):
    if (os.path.splitext(filename)[1].lower() == '.fits' or os.path.splitext(filename)[1].lower() == '.fit'):
        with fits.open(filename) as hdu:
            rgb = list(hdu[0].data)
            # rgb.reverse() <- Use this when you want the coordinates to be in GIMP-format.

    else:
        raise ValueError("your file has a not supported type!")

    if binning != 1: rgb = bin(rgb, binning)
    ExoScanner.config["saturated"] = max(ExoScanner.config["saturated"], max(rgb))
    return rgb