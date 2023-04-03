# calculates the brightness of one star in one image by taking a field of a few
# times a few pixels as input.

from math import sqrt
import numpy as np


def getMeanAndDeviation(starRegion, debug=False):
    mean = [0, 0]
    sum = 0
    for i in range(0, len(starRegion)):
        for j in range(0, len(starRegion[0])):
            mean[0]+=i*starRegion[i][j]
            mean[1]+=j*starRegion[i][j]
            sum+=starRegion[i][j]

    mean[0]/=sum
    mean[1]/=sum

    s = 0
    for i in range(0, len(starRegion)):
        for j in range(0, len(starRegion[0])):
            distSquared=(i-mean[0])**2+(j-mean[1])**2
            s+=distSquared*starRegion[i][j]
    s/=sum
    s = np.sqrt(max(0, s))     # Negative s can occur because of background-subtraction

    return mean,s


def subdivideMatrix(starRegion, amount):
    newRegion = []
    for i in range(0, len(starRegion)*amount):
        newRegion.append([])
        for j in range(0, len(starRegion[0])*amount):
            newRegion[i].append(starRegion[int(i/amount)][int(j/amount)])

    return newRegion


def backgroundRemoval(starRegion):
    values = []
    for i in starRegion:
        for j in i:
            values.append(j)
    values.sort()
    numbackground = int(len(values)/4)
    background = 0
    for k in range(numbackground):
        background += values[k]
    background /= numbackground
    background2 = values[int(len(values)/4)]

    #print("Background:")
    #print(background)
    #print(" Background2:")
    #print(background2)
    for i in range(len(starRegion)):
        for j in range(len(starRegion[0])):
            starRegion[i][j]-=background

    return starRegion

def saturationFinder(starRegion):
    found = False
    for i in starRegion:
        for j in i:
           found = found or j>=0.99
    return found

def getBrightnessOfOneStarInField(starRegion, subdivide=3, debug=False):

    if saturationFinder(starRegion):
        return 0

    starRegion = backgroundRemoval(starRegion)

    starRegion = subdivideMatrix(starRegion, subdivide)

    # print(background)

    mean,s = getMeanAndDeviation(starRegion, debug)
    # print(s)

    res = 0

    for i in range(0, len(starRegion)):
        for j in range(0, len(starRegion[0])):
            if sqrt((i-mean[0])**2 + (j-mean[1])**2).real <= s*2.5:
                res += starRegion[i][j]
            # elif sqrt((i-mean[0])**2 + (j-mean[1])**2).real <= s*2.5+1.5:
            #     res += (1-((sqrt((i-mean[0])**2 + (j-mean[1])**2) - s)/1.5).real) * starRegion[i][j]

    return res

