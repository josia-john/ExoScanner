# The function output() generates the output.

import matplotlib.pyplot as plt
from ExoScanner import myAlgorithms
import os

def output(lightcurves, times, analysis, count=10):
    count = min(count, len(analysis))
    analysis = sorted(analysis, key=lambda d: d['score'], reverse=True)

    try:
        os.makedirs("results/lightcurves")
    except:
        print("directory results/lightcurves already exists, continuing anyway...")

    for i in range(count):
        lc = lightcurves[analysis[i]["index"]]
        plt.scatter(times, lc, marker='.', color="black")

        WS = round(len(lc)/10) + 1
        rolling = myAlgorithms.rolling(lc, WS)
        plt.plot(times[int(WS/2):len(rolling)+int(WS/2)], rolling, color="blue")

        fit = ([analysis[i]["normalFlux"]]*analysis[i]["startTime"] + [analysis[i]["dipFlux"]]*(analysis[i]["endTime"]-analysis[i]["startTime"]) + [analysis[i]["normalFlux"]]*(len(times)-analysis[i]["endTime"]))
        plt.plot(times, fit, color="red")

        plt.title("candidate: " + str(analysis[i]["index"]))
        plt.title("coordinates: " + str(analysis[i]["coordinates"]) +
            "\nscore: " + str(round(analysis[i]["score"], 3)) +
            "\ndepth: " + str(round(analysis[i]["depth"], 5)))

        plt.subplots_adjust(top=0.8)

        plt.xlabel("time (julian date)")
        plt.ylabel("brightness (normalized flux)")

        plt.savefig("results/lightcurves/candidate-" + str(i) + ".png")

        plt.clf()