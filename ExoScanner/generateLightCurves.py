# The function generateLightCurves() generates lightcurves using the calculated
# brightness values by comparing them.

from ExoScanner.generateBrightnessOfAllStarsInAllImages import getBrightnessScoreOfStars
from ExoScanner.generateBrightnessOfAllStarsInAllImages import getNoiseScoreOfStars


def getReferenceMask(brightnessScore, noiseScore, x):
    n = len(brightnessScore)

    brightnessFactor = 0.3
    noiseFactor = 1.2
    
    mask = []

    while (len(mask) == 0):
        mask = []
        for i in range(0, n):
            if i == x:
                continue
            
            if abs(brightnessScore[i]-brightnessScore[x])/brightnessScore[x] > brightnessFactor:
                continue
        
            if noiseScore[i] > noiseScore[x] * noiseFactor:
                continue

            mask.append(i)
        
        brightnessFactor += 0.1
        noiseFactor += 0.1


    return mask


def generateLightCurves(brightness):
    brigthnessScore = getBrightnessScoreOfStars(brightness) # get information about all the stars
    noiseScore = getNoiseScoreOfStars(brightness)


    lightCurves = []
    for star in range(0, len(brightness[0])):
        factors = []

        mask = getReferenceMask(brigthnessScore, noiseScore, star)
        for i in brightness:
            exoplanet = i[star]
            reference = sum(i[j] for j in mask)
            if (reference == 0):
                print("ERROR: Something really bad happened... Please contact me about this! [generateLightCurves:ReferenceIsZero]")
                exit(0)

            factors.append(exoplanet/reference)

        multiplier = 1/(sum(factors)/len(factors))
        for i in range(len(factors)): factors[i]*=multiplier#*brigthnessScore[star]

        lightCurves.append(factors)
    
    return lightCurves