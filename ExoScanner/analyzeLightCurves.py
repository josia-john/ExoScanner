# This file contains the function "analyzeLightCurve()" which is responsible
# to fit a step-curve to the reduced data. It thin returns information about
# the fit like: score of the transit, depth, fit-quality, brightness in dip,
# normal brightness, start of transit, end of transit


import statistics
from multiprocessing import Pool

def fitStepCurve(l, r, curve):
    valuesIn = []
    valuesOut = []
    for i in range(0, l):
        valuesOut.append(curve[i])
    for i in range(l, r):
        valuesIn.append(curve[i])
    for i in range(r, len(curve)):
        valuesOut.append(curve[i])

    medianIn = statistics.median(valuesIn)
    medianOut = statistics.median(valuesOut)
    
    squares = 0

    for i in range(0, l):
        squares+=(curve[i]-medianOut) * (curve[i]-medianOut)
    for i in range(l, r):
        squares+=(curve[i]-medianIn) * (curve[i]-medianIn)
    for i in range(r, len(curve)):
        squares+=(curve[i]-medianOut) * (curve[i]-medianOut)

    return squares, medianIn, medianOut


def analyzeOneLightCurve(curve, minLength=10):
    bestSquare = -1
    mIn = 0
    mOut = 0
    l = -1
    r = -1
    for i in range(0, len(curve)-minLength):
        for j in range(i+minLength, len(curve)):
            if (i+1 + (len(curve)-j) < minLength): continue
            s, r1, r2 = fitStepCurve(i, j, curve)
            if (bestSquare == -1 or s < bestSquare):
                bestSquare = s
                mIn = r1
                mOut = r2
                l = i
                r = j
    
    bestSquare /= len(curve)
    if (bestSquare == 0): bestSquare = 0.0000000001

    d = {
        "score": (mOut-mIn) / bestSquare,
        "depth": mOut-mIn,
        "error": bestSquare,
        "dipFlux": mIn,
        "normalFlux": mOut,
        "startTime": l,
        "endTime": r
    }

    return d


def analyzeLightCurves(lightcurves):
    mp_pool = Pool()
    return mp_pool.map(analyzeOneLightCurve, lightcurves)