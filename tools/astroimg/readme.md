# astroimg

`astroimg` converts an image file to Z80 source code that can be compiled for the Bally Astrocade. Some cool features include automatic horizontal color boundary detection to get as many as 8 colors on screen simultaneously and an optional flag for dithering the image.

![astroimg demo](https://hxlntblob.blob.core.windows.net/nbm/astroimgtest.jpg)

## Prerequisites

Python 2.7 or higher. Tested with Python 2.7 and Python 3.6 on Mac OS X and Python 3.5 on Windows 10. Install prerequisite packages by running `pip install -r requirements.txt`.

## Usage 

`python astroimg.py path/to/img.png`

Add `--dither` after the file path to dither the image. 

## Output

`your_filename.gfx`: An assembly file containing just the pixel data for your image in standard Astrocade (low-resolution) format. The last line is commented out to ensure proper fullscreen display.

`your_filename.asm`: An assembly file that will compile with Zmac 1.3 to make a functioning Astrocade ROM (.bin). This file calls `your_filename.gfx` and includes a custom horizontal color boundary and a basic palette that you can change. You can use the `compileAndLaunch.bat` script in the `tools` folder to simplify building and testing in MAME.  
