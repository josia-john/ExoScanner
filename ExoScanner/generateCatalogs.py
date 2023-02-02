# This file is responsible for generating a catalog for each image in the
# sequence, each catalog containing all the stars in the image. This is done
# using the algorithm "DAOPHOT / DAOFIND"

from astropy.stats import sigma_clipped_stats
from photutils.detection import DAOStarFinder
from ExoScanner.readImage import readImage
import numpy as np
from multiprocessing import Pool


def generateCatalogForOneImage(file):
    data = readImage(file)
    border = int(((len(data) + len(data[0]))/2) * 0.1)
    mean, median, std = sigma_clipped_stats(data, sigma=3.0)
    box = np.ones([len(data), len(data[0])], dtype=bool)
    box[border:len(data)-border, border:len(data[0])-border] = False
    daofind = DAOStarFinder(fwhm=4.0, threshold=20*std)
    sources = daofind.find_stars(data-median, mask=box)

    return sources


def generateCatalogs(files):
    with Pool() as mp_pool:
        res = mp_pool.map(generateCatalogForOneImage, files)

    newRes=[]
    newFiles=[]

    for i in range(len(files)):
        if res[i] is None or len(res[i]) < 20: continue
        newRes.append(res[i])
        newFiles.append(files[i])

    return newRes, newFiles


