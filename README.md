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

## How to compile with pyinstaller?
Be sure to replace "<path>" with the location to the cli.py file
```
pyinstaller --noconfirm --onefile --console --name "ExoScanner" --hidden-import "photutils.geometry.core" --collect-data "photutils" --hidden-import "ttkthemes"  "<path>/cli.py"
```

## How to use?
To run ExoScanner run the following command:
```
python -m ExoScanner <path>
```
with `<path>` being the path to a folder with the to be analyzed light-frames.

When the light-frames are sorted by name, they should also be sorted by observation-time.

Exoscanner generates a folder `results/` in the current directory, make sure it
doesn't already exist, or that there is nothing important in it. There it stores
the results. It generates 10 images like the following, of the stars it thinks
it's most likely that a transit occured.

![example output](images/exampleOutput.png)

An example data-set to test the software can be found here: 
https://drive.google.com/drive/folders/13AZ1xhNR8qf8G5aFWLcC5ObRZvBCNXpz?usp=sharing



## FAQ
If you have any questions, feel free to contact me! I can be reached at [me@jlabs.anonaddy.com](mailto:me@jlabs.anonaddy.com)

If you already want a copy of my paper, please also contact me. The final version
will be uploaded here on January 9th though.
