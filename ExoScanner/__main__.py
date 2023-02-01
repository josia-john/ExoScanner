# This is the main file of this program. It contains the main function which
# calls the run function with all the parameters it extracted from the program-call.

from ExoScanner.gui import Window

import sys
import multiprocessing
# import tkinter as tk
from ttkthemes import ThemedTk as tk
import tkinter.ttk as ttk

def main():
    root = tk(theme="adapta", themebg=True)
    root.geometry("400x100")
    root.title("ExoScanner")
    window = Window(root)

    root.mainloop()
    # run(sys.argv[1])


if __name__ == "__main__":
    main()
