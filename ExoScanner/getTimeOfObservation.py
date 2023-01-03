# This function returns the observation-time of a fits-image. It gets it out of
# the fits-header. If cr2 files (canon-raw) are used, the program will crash
# here because cr2 files don't have fits-headers.

import os
from astropy.io import fits

def getTimeOfObservation(filename):
    if (os.path.splitext(filename)[1].lower() == '.fits' or os.path.splitext(filename)[1].lower() == '.fit'):
        with fits.open(filename) as hdu:
            return hdu[0].header["DATE-OBS"]

    raise Exception("File type not supported!")