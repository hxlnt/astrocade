# 🍄 ASTROCADE DEV 🍄

Let's make cute software for the Bally Astrocade!

## Table of contents
- [Introduction](#introduction)
- [What's in this repo](#whats-in-this-repo)
- [Development toolchain](#development-toolchain)
    - Writing code
    - Creating graphics and sound
    - Assembling and testing code
- [Additional learning resources](#additional-learning-resources)

![Sketch depicting Bally Astrocade](bally.png)

## Introduction
I'm teaching myself how to develop for the slightly-obscure Bally Astrocade, an 8-bit home computer/game console released in 1977. The Astrocade boasts impressive (for its day) specs: a 1.7MHz Z80 8-bit CPU, 4KB RAM, 256 available colors, 3 square-wave audio channels, and 4 controller ports. If you want to learn alongside me, this repo will contain the demos I create as well as any tools I create to make my workflow easier and more fun. 

## What's in this repo
- The `demos` folder contains my Astrocade assembly language experiments, complete with comments where applicable. They require `HVLIB.H` and the Zmac assembler. (See [Development toolchain](#development-toolchain) for more information.)
- The `tools` folder contains any tools or scripts I've created that may be of use for Astrocade software development. There's not much there now, but hopefully this will grow!

## Development toolchain
To make games and software for the Bally Astrocade, grab the tools listed below. Note that these are external links; proceed with care. :)

### Writing code
1. [HVGLIB.H](http://www.ballyalley.com/ml/ml_tools/HVGLIB.zip) is a Bally Astrocade library used in most tutorials and sample code. You'll typically include it at the top of your source code files by typing `INCLUDE HVGLIB.H` at the very top of your code.
2. Your favorite IDE with Z80 syntax highlighting. I use [VS Code](http://code.visualstudio.com) for Windows, Mac, or Linux, which also has a built-in terminal pane for running your compilation and testing scripts.

### Creating graphics and sound
Unfortunately, there aren't many tools to help you create your own graphics and audio for Bally Astrocade games. (That's one of the things I'm working on, actually!) In the meantime, there are some tools related to Astrocade image creation on the [AtariAge Astrocade forum]
(http://atariage.com/forums/topic/251416-programming-the-bally-arcadeastrocade/) as well as in [this repo for a port of Nyan Cat to the Astrocade](https://github.com/zhuowei/Nyastrocat).

### Assembling and testing code
1. The Zmac assembler for [Windows](http://www.ballyalley.com/ml/ml_tools/Zmac13_win32.zip) or [Linux](http://www.ballyalley.com/ml/ml_tools/zmac-linux.zip) is used in many tutorials. If you choose a different Z80 assembler, do note that macros, input rules, and other assembler-specific features will differ and code examples will need to be modified accordinly.
2. Once your code is successfully assembled into a binary file, you can test it in the Astrocade emulator inside [MAME](https://github.com/mamedev/mame/releases).
3. Compiling and launching your code requires several sequential command-line processes. It's only four or five lines, but you won't want to type them again and again--and risk making errors--every time you want to test a new bit of your code. So, I recommend you grab the [tools/compileAndLaunch.bat script](https://github.com/hxlnt/astrocade-dev/tools/tree/master/compileAndLaunch.bat) in this repo. To assemble your code and launch the resulting ROM in MAME, simply place the script alongside your source code, edit a line in the script to point to your MAME installation, and run `compileAndLaunch.bat mycode` where `mycode` is the name of your .asm file without the file extension.

## Additional learning resources
[Bally Alley](http://www.ballyalley.com/) is the definitive source for Bally Astrocade development. There, you'll find source code samples, tutorials, tools, manual scans, even an Astrocade-themed podcast! Much of what I make and post here will likely borrow heavily from Bally Alley's wealth of information. It's an excellent resource!