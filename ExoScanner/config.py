params = {
    "input_path": "G:/2023-08-18 (Sh2-114)/V2",           # input location
    "output_path": "G:/2023-08-18 (Sh2-114)/V2/Results",          # output location
    "FWHM": 4,                  # Full-Width-Half-Maximum for finding stars. (passed to DAOFIND)
    "starThreshold": 15,        # Threshold for finding stars. (passed to DAOFIND)
    "StarImageRatio": 3,        # Higher -> Remove more stars; Lower -> Remove more images
    "boxSize": 8,               # Box Size for determining brightness of a star
    "analysisMode": "variable", # search for variable stars ("variable") or transits ("exoplanet")
    "saturated": 1,             # Max value for a pixel. If this is reached, the star is thrown away.
    "astrometryApiKey": "insyqargwvmkesov", # Atrometry.net API key
    "outputCount":  20          # Number of results (graphs, files, queries)
}


def setParams(p):
    global params
    params = p