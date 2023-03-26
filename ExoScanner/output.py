# The function output() generates the output.

import matplotlib.pyplot as plt
from ExoScanner import myAlgorithms
import os



def outputVariable(lightcurves, times, imageNumber, analysis, output_location, count=20):
    count = min(count, len(analysis))
    analysis = sorted(analysis, key=lambda d: d['score'], reverse=True)

    print(count, "canditates will be returned. Default is 20.")

    try:
        os.makedirs(output_location)
    except:
        print(f"directory {output_location} already exists, continuing anyway...")

    for i in range(count):

        lc = lightcurves[analysis[i]["index"]]
        plt.scatter(times, lc, marker='.', color="black")

        WS = max(1,int(len(lc)/5))
        rolling = myAlgorithms.rolling(lc, WS)
        plt.plot(times[int(WS / 2):len(rolling) + int(WS / 2)], rolling, color="blue")

        upper = rolling[:]
        lower = rolling[:]
        for j in range(0, len(rolling)):
            upper[j] += rolling[j]*analysis[i]["error"]
            lower[j] -= rolling[j]*analysis[i]["error"]

        plt.plot(times[int(WS / 2):len(rolling) + int(WS / 2)], upper, color="gray")
        plt.plot(times[int(WS / 2):len(rolling) + int(WS / 2)], lower, color="gray")

        plt.title("candidate: " + str(analysis[i]["index"]))
        plt.title("coordinates: " + str(analysis[i]["coordinates"]) +
                  "\nscore: " + str(round(analysis[i]["score"], 3)) +
                  "\ndepth: " + str(round(analysis[i]["depth"], 5)))

        plt.subplots_adjust(top=0.8)

        if imageNumber:
            plt.xlabel("time (image number)")
        else:
            plt.xlabel("time (julian date)")
        plt.ylabel("brightness (normalized flux)")

        plt.savefig(f"{output_location}/candidate-" + str(i) + ".png")

        plt.clf()


def outputExoplanet(lightcurves, times, imageNumber, analysis, output_location, count=20):
    count = min(count, len(analysis))
    analysis = sorted(analysis, key=lambda d: d['score'], reverse=True)

    print(count, "canditates will be returned. Default is 20.")

    try:
        os.makedirs(output_location)
    except:
        print(f"directory {output_location} already exists, continuing anyway...")

    for i in range(count):

        lc = lightcurves[analysis[i]["index"]]
        plt.scatter(times, lc, marker='.', color="black")

        WS = max(1,int(len(lc)/5))
        rolling = myAlgorithms.rolling(lc, WS)
        plt.plot(times[int(WS / 2):len(rolling) + int(WS / 2)], rolling, color="blue")

        fit = ([analysis[i]["normalFlux"]] * analysis[i]["startTime"] + [analysis[i]["dipFlux"]] * (
                    analysis[i]["endTime"] - analysis[i]["startTime"]) + [analysis[i]["normalFlux"]] * (
                           len(times) - analysis[i]["endTime"]))
        plt.plot(times, fit, color="red")

        plt.title("candidate: " + str(analysis[i]["index"]))
        plt.title("coordinates: " + str(analysis[i]["coordinates"]) +
                  "\nscore: " + str(round(analysis[i]["score"], 3)) +
                  "\ndepth: " + str(round(analysis[i]["depth"], 5)))

        plt.subplots_adjust(top=0.8)

        if imageNumber:
            plt.xlabel("time (image number)")
        else:
            plt.xlabel("time (julian date)")
        plt.ylabel("brightness (normalized flux)")

        plt.savefig(f"{output_location}/candidate-" + str(i) + ".png")

        plt.clf()
