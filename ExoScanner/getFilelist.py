# This function returns all the files present in one folder. It filters out all
# files starting with "." (hidden files). It is planned to later implement the
# function to filter the selected files with a regex.

import os, glob

def getFilelist(pathToFolder):
    files = os.listdir(pathToFolder)
    files.sort()
    res = []

    res.extend(glob.glob(os.path.join(pathToFolder,"*.[fF][iI][tT][sS]")))
    res.extend(glob.glob(os.path.join(pathToFolder,"*.[fF][iI][tT]")))

    print("found", len(res), "files")

    return res

