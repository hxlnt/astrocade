REM This handy script compiles Bally Astrocade assembly code and launches the resulting binary in MAME.
REM Edit the lines as indicated below, put this .bat file alongside your .asm files, and run compileAndTest.bat in the Command Prompt. You must have zmac and MAME (with Astrocade support) already installed.
REM hxlnt 2018

REM Line 7 uses zmac to compile game.asm to game.bin. You can change "game" to some other name--just be sure to do it throughout the script.
REM Run this script inside the folder containing game.asm and ensure that zmac is on the path or in the same folder.
zmac -o game.bin game.asm

REM Line 11 copies game.bin into MAME's Astrocade ROMs folder. Edit this line with the correct path.
REM The spelling of "astrocde" (without the 'a') is not a mistake--this follows MAME's folder naming convention. 
copy game.bin "C:\your\path\to\mame\roms\astrocde\" 

REM Lines 15 and 16 launch game.bin in MAME. Edit these lines with the correct path.
REM You may also need to edit "mame64.exe" if your MAME .exe has a different name.
cd "C:\your\path\to\mame\"
mame64.exe astrocde -cart "C:\your\path\to\mame\roms\astrocde\game.bin"
