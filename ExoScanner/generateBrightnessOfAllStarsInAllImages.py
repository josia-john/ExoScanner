# This file contains functions for getting information about stars, like their
# brightness or their noise-level.
# The function generateBrightnessOfAllStarsInAllImages() calls another function
# to find the brightness of all stars in all images.
# The function cleanUpData() is responsible for data-cleansing.

from math import ceil, floor
from ExoScanner.generateField import generateField
from ExoScanner.getBrightnessOfOneStarInField import getBrightnessOfOneStarInField
from ExoScanner.readImage import readImage
from ExoScanner.myAlgorithms import rolling
import numpy as np
from multiprocessing import Pool

def cleanUpData(brightness):
    brightness = np.array(brightness)
    removeStars = []
    removeImages = []
    for star in range(0, len(brightness[0])):
        for i in range(0, len(brightness)):
            if brightness[i][star] == 0:
                percentageStar = np.count_nonzero(brightness[:, star]==0)/len(brightness)
                percentageImage = np.count_nonzero(brightness[i]==0)/len(brightness[0])
                if percentageStar*2 > percentageImage or i == 0:
                    removeStars.append(star)
                else:
                    removeImages.append(i)
    
    cleanData = []
    usedImagesIndex = []
    usedStarsIndex = []
    for i in range(0, len(brightness)):
        if i in removeImages:
            continue
        usedImagesIndex.append(i)
        cleanData.append([])
        for star in range(0, len(brightness[0])):
            if star in removeStars:
                continue
            if i == 0: usedStarsIndex.append(star)
            cleanData[-1].append(brightness[i][star])
    
    return cleanData, usedImagesIndex, usedStarsIndex




def getNoiseScoreOfStars(brightness):
    score = []

    for star in range(0, len(brightness[0])):
        s = 0
        curve = [brightness[i][star] for i in range(len(brightness))]
        windowWidth = 20
        rolled = rolling(curve, windowWidth)
        for i in range(ceil(windowWidth/2)-1, len(brightness)-floor(windowWidth/2)):
            s += (rolled[i-ceil(windowWidth/2)-1]-curve[i])**2/rolled[i-ceil(windowWidth/2)-1]**2

        score.append((s/len(rolled))**0.5)

    return score

def getBrightnessScoreOfStars(brightness):
    score = []
    for star in range(0, len(brightness[0])):
        score.append(0)
        for i in range(0, len(brightness)):
            score[star] += int(brightness[i][star])

    return score



def getBrightnessInOneStar(files, catalogs, transitions, i, radius=8):
    rgb = readImage(files[i])

    starsInImage = []

    for currentStarIndex in range(0, len(catalogs[0])):
        indexInCatalog = transitions[i-1][currentStarIndex]
        if indexInCatalog == -1:
            starsInImage.append(0)
            continue

        field = generateField(rgb, catalogs[i]["xcentroid"][indexInCatalog], catalogs[i]["ycentroid"][indexInCatalog], 8)
        starsInImage.append(getBrightnessOfOneStarInField(field))

    return starsInImage



def generateBrightnessOfAllStarsInAllImages(files, catalogs, transitions, debug=False, radius=8):
    with Pool() as mp_pool:
        brightness = mp_pool.starmap(getBrightnessInOneStar, [(files, catalogs, transitions, i, radius) for i in range(1, len(files))])

    return brightness
