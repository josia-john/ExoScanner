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
from ExoScanner.output import output

from astropy.time import Time


def run(pathToLights):
    files = getFilelist(pathToLights)   # get all files

    catalogs, files = generateCatalogs(files)   # get catalogs and ignore files with less than 20 stars

    brightness = generateBrightnessOfAllStarsInAllImages(files, catalogs, mergeCatalogs(catalogs))  # get brightness
    brightness, axis, stars = cleanUpData(brightness)   # remove bad images and bad stars

    lightCurves = generateLightCurves(brightness)   # get Lightcurves

    analysis = analyzeLightCurves(lightCurves)

    times = []  # get observation-times for the included images
    for i in axis:
        times.append(getTimeOfObservation(files[i]))
    times = Time(times, format='isot', scale='utc').jd

    for i in range(len(analysis)):  # add index and coordinates in the first image to the analysis of each star
        analysis[i]["index"] = i
        analysis[i]["coordinates"] = (round(catalogs[0]["xcentroid"][stars[i]]),round(catalogs[0]["ycentroid"][stars[i]]))
        
    output(lightCurves, times, analysis)    # generate output
