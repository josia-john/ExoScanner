import os
import tkinter.ttk as ttk
from tkinter import PhotoImage, Menu, Frame, filedialog, END
from ttkthemes import ThemedTk as tk
from PIL import Image, ImageTk

from ExoScanner.run import run

import ExoScanner.myAlgorithms 
import ExoScanner.config 

import sys

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)

        file_menu = Menu(menu, tearoff=0)
        file_menu.add_command(label="Open", command=self.on_open)
        file_menu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="File", menu=file_menu)


        self.master.config(menu=menu)

        file_manage_frm = ttk.Frame(self.master)

        # initializing fields
        self.path_to_files_label = ttk.Label(wraplength=500, text="Input files directory:")
        self.path_to_files = ttk.Entry()
        self.browse_input = ttk.Button(self.master, text="browse", command=self.set_input_file_location)

        self.path_to_output_label = ttk.Label(wraplength=500, text="Destination:")
        self.path_to_output = ttk.Entry()
        self.browse_output = ttk.Button(self.master, text="browse", command=self.set_output_file_location)

        self.param_FWHM_label = ttk.Label(wraplength=500, text="FWHM (used for finding stars; default (4) should be ok)")
        self.param_FWHM = ttk.Entry()
        self.param_FWHM.insert(0, "4")

        self.param_star_threshold_label = ttk.Label(wraplength=500, text="Star threshold (used for finding stars; default (15) should be ok)")
        self.param_star_threshold = ttk.Entry()
        self.param_star_threshold.insert(0, "15")

        self.param_star_image_ratio_label = ttk.Label(wraplength=500, text="Star to image valuing ratio. (determines to throw away more stars (higher) or to throw away more images (lower); default (3) should be ok)")
        self.param_star_image_ratio = ttk.Entry()
        self.param_star_image_ratio.insert(0, "3")

        self.param_box_size_brightness_calc_label = ttk.Label(wraplength=500, text="brightness calculation box size (determines the size of the box which is used to determine the brightness of a star; default (8) should be ok)")
        self.param_box_size_brightness_calc = ttk.Entry()
        self.param_box_size_brightness_calc.insert(0, "8")

        self.mode_label = ttk.Label(wraplength=500, text="Search for variable stars ('variable') or transits ('exoplanet'). Default is 'variable'")
        self.mode = ttk.Combobox(values=["variable", "exoplanet"])
        self.mode.insert(0, "variable")

        self.submit = ttk.Button(self.master, text="Submit",
                                 command=lambda: self.on_submit())

        # positioning fields
        self.path_to_files_label.grid(column=0, row=0, padx=5)
        self.path_to_files.grid(column=0, row=1, padx=5, ipady=5, ipadx=100)
        self.browse_input.grid(column=1, row=1, padx=5)
        self.path_to_output_label.grid(column=0, row=2, padx=5)
        self.path_to_output.grid(column=0, row=3, padx=5, ipady=5, ipadx=100)
        self.browse_output.grid(column=1, row=3, padx=5)

        self.param_FWHM_label.grid(column=0, row=5, padx=5)
        self.param_FWHM.grid(column=0, row=6, padx=5, ipady=5, ipadx=100)
        self.param_star_threshold_label.grid(column=0, row=7, padx=5)
        self.param_star_threshold.grid(column=0, row=8, padx=5, ipady=5, ipadx=100)
        self.param_star_image_ratio_label.grid(column=0, row=9, padx=5)
        self.param_star_image_ratio.grid(column=0, row=10, padx=5, ipady=5, ipadx=100)
        self.param_box_size_brightness_calc_label.grid(column=0, row=11, padx=5)
        self.param_box_size_brightness_calc.grid(column=0, row=12, padx=5, ipady=5, ipadx=100)
        self.mode_label.grid(column=0, row=13, padx=5)
        self.mode.grid(column=0, row=14, padx=5, ipady=5, ipadx=100)
        

        self.submit.grid(column=1, row=4, padx=5, pady=25)

    def on_open(self):
        file = filedialog.askopenfilename()
        ExoScanner.myAlgorithms.open_file(file)

    def set_input_file_location(self):
        path = filedialog.askdirectory()
        self.path_to_files.delete(0, END)
        self.path_to_files.insert(0, path)

    def set_output_file_location(self):
        path = filedialog.askdirectory()
        self.path_to_output.delete(0, END)
        self.path_to_output.insert(0, path)

    def on_submit(self):
        if self.path_to_files.get() is None:
            print("no input path provided, can't start ExoScanner!")
            return
        ExoScanner.config.params["input_path"] = self.path_to_files.get()
        if self.path_to_output.get() is None:
            print("no output path provided, can't start ExoScanner!")
            return
        ExoScanner.config.params["output_path"] = self.path_to_output.get()
        if self.param_FWHM.get() is None:
            print("no FWHM provided, can't start ExoScanner!")
            return
        ExoScanner.config.params["FWHM"] = float(self.param_FWHM.get())
        if self.param_star_threshold.get() is None:
            print("no star-threshold provided, can't start ExoScanner!")
            return
        ExoScanner.config.params["starThreshold"] = float(self.param_star_threshold.get())
        if self.param_star_image_ratio.get() is None:
            print("no star to image importance ratio provided, can't start ExoScanner!")
            return
        ExoScanner.config.params["StarImageRatio"] = float(self.param_star_image_ratio.get())
        if self.param_box_size_brightness_calc.get() is None:
            print("no box size provided, can't start ExoScanner!")
            return
        ExoScanner.config.params["boxSize"] = int(self.param_box_size_brightness_calc.get())
        if self.mode.get() is None:
            print("no mode provided, can't start ExoScanner")
            return
        ExoScanner.config.params["analysisMode"] = self.mode.get()
        
        self.submit["state"] = "disabled"
        run()
        self.submit["state"] = "normal"

    def exitProgram(self):
        sys.exit()


def start_gui():
    absolute_path = os.path.dirname(__file__)
    relative_path = "Exoscanner_logo.png"
    full_path = os.path.join(absolute_path, relative_path)

    master = tk(theme="black", themebg=True)
    master.title("ExoScanner")
    master.iconphoto(False, PhotoImage(file=full_path))
    app = Window(master)
    master.mainloop()
