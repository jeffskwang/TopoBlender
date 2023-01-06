#!/bin/bash

####USER SPECIFIED
#Paramter File 
parameter1=trout_creek_ortho_example
parameter2=trout_creek_persp_example
parameter3=trout_creek_hillshade_example

#Define locations of blender <--IMPORTANT, NEEDS TO BE UPDATED TO YOUR SYSTEM
blender_location=/Applications/Blender.app/contents/MacOS

####AUTOMATED SECTION
#moves to blender location to run blender
cd $blender_location

#TopoBlender file is assumed to be in the same directory as this .sh file
TopoBlender_location=$(dirname $0)

./Blender -b -P $TopoBlender_location/TopoBlender.py -- $TopoBlender_location/parameters/$parameter1
./Blender -b -P $TopoBlender_location/TopoBlender.py -- $TopoBlender_location/parameters/$parameter2
./Blender -b -P $TopoBlender_location/TopoBlender.py -- $TopoBlender_location/parameters/$parameter3