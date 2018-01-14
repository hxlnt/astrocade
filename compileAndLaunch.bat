@REM This handy script compiles Bally Astrocade assembly code and launches the resulting binary in MAME.
@REM Edit line 6 below, put this .bat file alongside your .asm files, and run "./compileAndLaunch.bat yourasmfilename" (without the quotes). 
@REM You must have zmac from Bally Alley and MAME (with Astrocade support) already installed.
@REM hxlnt 2018

@set mamepath="C:\Users\rache\Desktop\Astrocade dev\mame"

:parse
@if "%1"=="" goto noargs
@zmac -o %1.bin %1.asm
@copy %1.bin "%mamepath:"=%\roms\astrocde"
@cd %mamepath%
@mame64.exe astrocde -cart "%mamepath:"=%\roms\astrocde\%1.bin"
@goto :eof

:noargs
@echo Pass in the filename of your .asm file without the .asm extension. Example: ./compileAndLaunch.bat helloworld

:eof
