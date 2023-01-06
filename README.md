# TopoBlender
Python script to render images of topography using Blender

## What does this mean?
- Python - a coding language
- script - a text file with code
- render - a process of turning a 3D scene into a realistic 2D image, like taking a picture
- topography - the shape of the surface of Earth (or other planets)
- Blender - a free and open-source software used to render 3D scenes

## What do rendered images look like?
<p align="center">
<img src="https://github.com/jeffskwang/TopoBlender/blob/7f9317b485e64b394df67d7b2428c4a3794cfca3/readme_images/trout_creek_ortho_low_res.png" alt="rendered topography with orthographic view" width="400"/>
<img src="https://github.com/jeffskwang/TopoBlender/blob/7f9317b485e64b394df67d7b2428c4a3794cfca3/readme_images/trout_creek_hillshade_low_res.png" alt="rendered topography with hillshade view" width="400"/>
 </p>

## What will you need
1. [Blender](https://www.blender.org/download/)
2. A way to convert your digital elevation models (DEMs) to [ASCII format](https://desktop.arcgis.com/en/arcmap/latest/manage-data/raster-and-images/esri-ascii-raster-format.htm) (.asc), e.g., [GDAL](https://gdal.org/), [QGIS](https://qgis.org/en/site/), ArcGIS.
3. *Optional* - A GPU will allow the render engine (CYCLES) to run faster
4. Inputs
    * .tif file of your DEM (located in TopoBlender/data folder), this needs to be converted to .asc
    * .asc file of your DEM (located in TopoBlender/converted folder)
    * .py file of your render settings (located in TopoBlender/parameters folder)

## Converting .tif to .asc
In order for Blender to run without additional installations, TopoBlender requires the input DEM to have a ASCII file format (.asc). To convert your DEM to this format, I recommend **gdal_translate** in GDAL. An example script file (**convert_tif_to_asc_example.sh**) is included. The script file assumes that GDAL is installed within an [Anaconda Environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html). Last, in addition to .tif files, GDAL can also convert other DEM filetypes to .asc.

##TopoBlender UI
TopoBlender can be used with the Blender UI. It is as simple as opening the **TopoBlenderUI.blend** file with blender.

