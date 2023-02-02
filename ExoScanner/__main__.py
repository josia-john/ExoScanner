# This is the main file of this program. It contains the main function which
# calls the run function with all the parameters it extracted from the program-call.
import sys

from ExoScanner.gui import start_gui
from ExoScanner.run import run


def main():
    if len(sys.argv) == 1:
        print("starting GUI...")
        start_gui()
    else:
        print("running ExoScanner with given parameters...")
        if len(sys.argv) > 2:
            run(sys.argv[1], output_location=sys.argv[2])
        else:
            run(sys.argv[1])


if __name__ == "__main__":
    main()
