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
In order for Blender to run without additional installations, TopoBlender requires the input DEM to have a ASCII file format (.asc). To convert your DEM to this format, I recommend **gdal\_translate** in GDAL. An example script file (**convert_tif\_to\_asc\_example.sh**) is included. The script file assumes that GDAL is installed within an [Anaconda Environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html). Last, in addition to .tif files, GDAL can also convert other DEM filetypes to .asc.

## TopoBlender UI
TopoBlender can be used with the Blender UI. It is as simple as opening the **TopoBlenderUI.blend** file with Blender. You will be greeted with the following window. You will see a viewport of a cube, the default starting polygon in Blender, and a code window.

<p align="center">
<img src="https://github.com/jeffskwang/TopoBlender/blob/5a394780c97979234d8a0c5733489a84f56fefd9/readme_images/UI_0.png" alt="Blender UI" width="600"/>
</p>

Before running the code, you will need to change one line of code (**highlighted text**) to point your code to the TopoBlender folder.

<p align="center">
<img src="https://github.com/jeffskwang/TopoBlender/blob/5a394780c97979234d8a0c5733489a84f56fefd9/readme_images/UI_1.png" alt="Line of code of TopoBlender folder location" width="600"/>
</p>

After changing the line of code, you can run the code by hitting the play button!

<p align="center">
<img src="https://github.com/jeffskwang/TopoBlender/blob/5a394780c97979234d8a0c5733489a84f56fefd9/readme_images/UI_2.png" alt="Run script button" width="400"/>
</p>

You will get the spinning wheel cursor, indicating the code is running. Just wait a few seconds until the screen updates. When it does, click the **Layout** tab to preview the render.

<p align="center">
<img src="https://github.com/jeffskwang/TopoBlender/blob/5a394780c97979234d8a0c5733489a84f56fefd9/readme_images/UI_3.png" alt="Layout Tab" width="400"/>
</p>

The cube will be gone and you will now see a small flat plane. This is your topography. To view the topography from the render's camera view, click the **Camera View** button.

<p align="center">
<img src="https://github.com/jeffskwang/TopoBlender/blob/5a394780c97979234d8a0c5733489a84f56fefd9/readme_images/UI_4.png" alt="Camera View Button" width="400"/>
</p>

This will show you the plane that we created that holds the topography data, but you will not see any relief in the topograpghy. To see that you, will need to preview the render by click the **Viewport Shading** button the top-right corner of the viewport.

<p align="center">
<img src="https://github.com/jeffskwang/TopoBlender/blob/5a394780c97979234d8a0c5733489a84f56fefd9/readme_images/UI_5.png" alt="Viewport Shading Button" width="400"/>
</p>

After click **Viewport Shading** you will now see a preview of the render!

<p align="center">
<img src="https://github.com/jeffskwang/TopoBlender/blob/5a394780c97979234d8a0c5733489a84f56fefd9/readme_images/UI_6.png" alt="Render Preview" width="600"/>
</p>

You can also see a higher fidelity render in the TopoBlender/renders folder. If you are running the example, the file is named **trout_creek.png**, also found [here](https://github.com/jeffskwang/TopoBlender/blob/70572a57dea077ac8ff8e97ab6b1135b66aadc4b/renders/trout_creek.png).



