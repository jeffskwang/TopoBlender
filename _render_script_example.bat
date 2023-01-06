@echo off
:: USER SPECIFIED
:: Paramter File 
set parameter1=trout_creek_ortho_example
set parameter2=trout_creek_persp_example
set parameter3=trout_creek_hillshade_example

:: Define locations of blender <--IMPORTANT, NEEDS TO BE UPDATED TO YOUR SYSTEM
set blender_location=C:\Program Files\Blender Foundation\Blender 3.4

:: AUTOMATED SECTION
:: TopoBlender file is assumed to be in the same directory as this .sh file
set TopoBlender_location=%cd%

:: moves to blender location to run blender
cd %blender_location%

blender.exe -b -P %TopoBlender_location%/TopoBlender.py -- %TopoBlender_location%/parameters/%parameter1%
blender.exe -b -P %TopoBlender_location%/TopoBlender.py -- %TopoBlender_location%/parameters/%parameter2%
blender.exe -b -P %TopoBlender_location%/TopoBlender.py -- %TopoBlender_location%/parameters/%parameter3%

PAUSE 