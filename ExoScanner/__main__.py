# This is the main file of this program. It contains the main function which
# calls the run function with all the parameters it extracted from the program-call.
import sys

from ExoScanner.gui import start_gui
from ExoScanner.run import run

import ExoScanner.config

def main():
    if len(sys.argv) == 1:
        print("starting GUI...")
        start_gui()
    else:
        print("running ExoScanner with given parameters...\nit is recommended to use ExoScanner with the provided GUI...")
        if len(sys.argv) > 2:
            ExoScanner.config.params["input_path"] = sys.argv[1]
            ExoScanner.config.params["output_path"] = sys.argv[2]
            run()
        else:
            ExoScanner.config.params["input_path"] = sys.argv[1]
            ExoScanner.config.params["output_path"] = "results/lightcurves"
            run()

if __name__ == "__main__":
    main()
