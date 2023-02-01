import tkinter.ttk as ttk
from ttkthemes import ThemedTk as tk

from ExoScanner.run import run

class Window:

    def __init__(self, master):
        path_to_files_label = ttk.Label(text="Enter path to 'fits' files")
        path_to_files = ttk.Entry()

        path_to_files_label.pack(anchor="nw", padx=15)
        path_to_files.pack(anchor="n", padx=15, fill="x")

        submit = ttk.Button(master, text="Submit", command=lambda: run(path_to_files.get()))
        submit.pack(anchor="e", padx=15, pady=15)

def start_gui():
    root = tk(theme="adapta", themebg=True)
    root.geometry("400x100")
    root.title("ExoScanner")
    window = Window(root)

    root.mainloop()