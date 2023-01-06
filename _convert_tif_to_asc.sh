#!/bin/bash

# Location where anaconda is installed
source /opt/anaconda3/etc/profile.d/conda.sh

# Activate environment where gdal is installed (my environment is named pygdal)
conda activate pygdal

# define data location
data_location=/Users/jeffreykwang/Documents/GitHub/TopoBlender/data
coverted_data_location=/Users/jeffreykwang/Documents/GitHub/TopoBlender/converted
filename=trout_creek

# Translate .tif file into a .asc file so that blender can read it
gdal_translate $data_location/$filename.tif $coverted_data_location/$filename.asc

exit