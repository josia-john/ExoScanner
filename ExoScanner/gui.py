import tkinter.ttk as ttk

from ExoScanner.run import run

class Window:

    def __init__(self, master):
        path_to_files_label = ttk.Label(text="Enter path to 'fits' files")
        path_to_files = ttk.Entry()

        path_to_files_label.pack(anchor="nw", padx=15)
        path_to_files.pack(anchor="n", padx=15, fill="x")

        submit = ttk.Button(master, text="Submit", command=lambda: run(path_to_files.get()))
        submit.pack(anchor="e", padx=15, pady=15)