# This is the main file of this program. It contains the main function which
# calls the run function with all the parameters it extracted from the program-
# call.

from ExoScanner.run import run

import sys

def main():
    run(sys.argv[1])


if __name__ == "__main__":
    main()
