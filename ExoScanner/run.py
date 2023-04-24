# The function run() calls all the functions needed in the correct order and
# combines their returned results.

from ExoScanner.getFilelist import getFilelist
from ExoScanner.generateBrightnessOfAllStarsInAllImages import generateBrightnessOfAllStarsInAllImages
from ExoScanner.generateBrightnessOfAllStarsInAllImages import cleanUpData
from ExoScanner.generateCatalogs import generateCatalogs
from ExoScanner.mergeCatalogs import mergeCatalogs
from ExoScanner.analyzeLightCurves import analyzeLightCurves
from ExoScanner.getTimeOfObservation import getTimeOfObservation
from ExoScanner.generateLightCurves import generateLightCurves
from ExoScanner.output import outputExoplanet
from ExoScanner.output import outputVariable


import ExoScanner.config

from astropy.time import Time

import ExoScanner.myAlgorithms
from ExoScanner.data import brightness,files,catalogs

def run():
    pathToLights = ExoScanner.config.params["input_path"]
    output_location = ExoScanner.config.params["output_path"]
    
    if len(ExoScanner.data.files) == 0:
        print("finding files...")
        files = getFilelist(pathToLights)   # get all files
        ExoScanner.data.files = files
        print("found", len(files), "files")
    else:
        files = ExoScanner.data.files
    if (len(files)<25):
        print("ERROR: At least 25 files are required.")
        exit(0)

    if len(ExoScanner.data.catalogs) == 0:
        print("finding stars in all images")
        catalogs, files = generateCatalogs(files)   # get catalogs and ignore files with less than 20 stars
        ExoScanner.data.catalogs = catalogs
        ExoScanner.data.files = files
    else:
        catalogs = ExoScanner.data.catalogs
        files = ExoScanner.data.files
    if len(ExoScanner.data.brightness) == 0:
        print("calculate brightness of stars")
        brightness = generateBrightnessOfAllStarsInAllImages(files, catalogs, mergeCatalogs(catalogs))  # get brightness
        ExoScanner.data.brightness = brightness
    else:
        brightness = ExoScanner.data.brightness

    print("cleanup data")
    brightness, axis, stars = cleanUpData(brightness)   # remove bad images and bad stars

    print(len(axis), "files are usable. The others will be ignored.")
    print(len(stars), "stars are usable. The others will be ignored.")

    if (len(axis)<25):
        print("ERROR: At least 25 files are required. Only", len(axis), "usable files were provided.")
        exit(0)

    if (len(stars)<5):
        print("ERROR: At least 5 stars are required. Only", len(stars), "usable stars were found.")
        exit(0)

    print("generate all lightcurves by comparing the brightness of different stars")
    lightCurves = generateLightCurves(brightness)   # get Lightcurves

    print("analyzing the lightcurves")
    analysis = analyzeLightCurves(lightCurves)

    times = []  # get observation-times for the included images
    for i in axis:
        times.append(getTimeOfObservation(files[i]))

    imageNumber = 0

    if not -1 in times:
        times = Time(times, format='isot', scale='utc').jd
    else:
        times = axis
        imageNumber = 1

    for i in range(len(analysis)):  # add index and coordinates in the first image to the analysis of each star
        analysis[i]["index"] = i
        analysis[i]["coordinates"] = (round(catalogs[0]["xcentroid"][stars[i]]),round(catalogs[0]["ycentroid"][stars[i]]))

    print("writing output files")

    if (ExoScanner.config.params["analysisMode"] == "variable"):
        outputVariable(lightCurves, times, imageNumber, analysis, output_location)
    elif (ExoScanner.config.params["analysisMode"] == "exoplanet"):
        outputExoplanet(lightCurves, times, imageNumber, analysis, output_location)
    else:
        outputVariable(lightCurves, times, imageNumber, analysis, output_location)

    ExoScanner.myAlgorithms.open_file(output_location)
    print("done")
