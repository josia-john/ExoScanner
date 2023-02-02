# This is the main file of this program. It contains the main function which
# calls the run function with all the parameters it extracted from the program-call.
import sys

from ExoScanner.gui import start_gui
from ExoScanner.run import run


def main():
    if len(sys.argv) == 1:
        start_gui()
    else:
        if len(sys.argv) > 2:
            run(sys.argv[1], output_location=sys.argv[3])
        else:
            run(sys.argv[1])


if __name__ == "__main__":
    main()
