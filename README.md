# ExoScanner
A CLI-tool to analyze an image-series for exoplanet transits.

## What is this?
ExoScanner is a software which can analyze image-series recorded by amateurs
with the goal of detecting exoplanet-transits in them. The project started as
a high-school paper. But because I think that it might be useful for others,
I am publishing it. I hope to be able to maintain the program.

## How to install?
A working python-installation is needed for ExoScanner can be installed with pip:
```
pip install https://github.com/josia-john/ExoScanner/archive/main.zip
```

## How to use?
To run ExoScanner run the following command:
```
python -m ExoScanner <path>
```
with `<path>` being the path to a folder with the to be analyzed light-frames.

When the light-frames are sorted by name, they should also be sorted by observation-time.

Exoscanner generates a folder `results/` in the current directory, make sure it
doesn't already exist, or that there is nothing important in it.
