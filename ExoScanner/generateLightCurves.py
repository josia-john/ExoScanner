# The function generateLightCurves() generates lightcurves using the calculated
# brightness values by comparing them.

from ExoScanner.generateBrightnessOfAllStarsInAllImages import getBrightnessScoreOfStars
from ExoScanner.generateBrightnessOfAllStarsInAllImages import getNoiseScoreOfStars

def generateLightCurves(brightness):
    brigthnessScore = getBrightnessScoreOfStars(brightness) # get information about all the stars
    noiseScore = getNoiseScoreOfStars(brightness)


    lightCurves = []
    for star in range(0, len(brightness[0])):
        factors = []

        for i in brightness:
            exoplanet = i[star]
            reference = sum(i[j] for j in range(len(i)) if abs(brigthnessScore[j]-brigthnessScore[star])/brigthnessScore[star] < 0.3 and noiseScore[j] < noiseScore[star]*1.2) - exoplanet
            if (reference == 0):
                if len(factors): factors.append(factors[-1])
                else: factors.append(1)
                continue
            factors.append(exoplanet/reference)

        multiplier = 1/(sum(factors)/len(factors))
        for i in range(len(factors)): factors[i]*=multiplier#*brigthnessScore[star]

        lightCurves.append(factors)
    
    return lightCurves