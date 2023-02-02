import os
import tkinter.ttk as ttk
from tkinter import PhotoImage, Menu, Frame, filedialog, END
from ttkthemes import ThemedTk as tk
from PIL import Image, ImageTk

from ExoScanner.run import run


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


        self.path_to_files_label = ttk.Label(text="Input files directory:")
        self.path_to_files = ttk.Entry()
        self.browse_input = ttk.Button(self.master, text="browse", command=self.set_input_file_location)

        self.path_to_output_label = ttk.Label(text="Destination:")
        self.path_to_output = ttk.Entry()
        self.browse_output = ttk.Button(self.master, text="browse", command=self.set_output_file_location)
        self.submit = ttk.Button(self.master, text="Submit",
                                 command=lambda: self.on_submit(self.path_to_files.get(), self.path_to_output.get()))


        self.path_to_files_label.grid(column=0, row=0, padx=5)
        self.path_to_files.grid(column=0, row=1, padx=5, ipady=5, ipadx=100)
        self.browse_input.grid(column=1, row=1, padx=5)
        self.path_to_output_label.grid(column=0, row=2, padx=5)
        self.path_to_output.grid(column=0, row=3, padx=5, ipady=5, ipadx=100)
        self.browse_output.grid(column=1, row=3, padx=5)
        self.submit.grid(column=1, row=4, padx=5, pady=25)

    def on_open(self):
        file = filedialog.askopenfilename()
        os.startfile(file)

    def set_input_file_location(self):
        path = filedialog.askdirectory()
        self.path_to_files.delete(0, END)
        self.path_to_files.insert(0, path)

    def set_output_file_location(self):
        path = filedialog.askdirectory()
        self.path_to_output.delete(0, END)
        self.path_to_output.insert(0, path)

    def on_submit(self, path_to_files, output_location):
        if path_to_files is not None:
            if output_location is not None:
                run(path_to_files, output_location=output_location)

    def exitProgram(self):
        exit()


def start_gui():
    master = tk(theme="black", themebg=True)
    master.title("ExoScanner")
    app = Window(master)
    master.mainloop()
