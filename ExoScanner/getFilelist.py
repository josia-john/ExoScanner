# This function returns all the files present in one folder. It filters out all
# files starting with "." (hidden files). It is planned to later implement the
# function to filter the selected files with a regex.

import os

def getFilelist(pathToFolder):
    files = os.listdir(pathToFolder)
    files.sort()
    res = []

    for i in files:
        if(i[0]=="."): continue
        res.append(os.path.join(pathToFolder, i))

    return res

