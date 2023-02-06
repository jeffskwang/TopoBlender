# TopoBlender
Python script that renders images of topography using Blender

## What does this mean?
- Python - a coding language
- script - a text file with code
- render - a process of turning a 3D scene into a 2D image, like taking a picture
- topography - the shape of the surface of Earth (or other planets)
- Blender - a free and open-source software used to render 3D scenes

## What do rendered images look like?
<p align="center">
   <img src="https://github.com/jeffskwang/TopoBlender/blob/7f9317b485e64b394df67d7b2428c4a3794cfca3/readme_images/trout_creek_ortho_low_res.png" alt="rendered topography with orthographic view" width="500"/>
</p>
<p align="center">
Fig.1 - Topography viewed from an oblique angle.
</p>
<p align="center">
   <img src="https://github.com/jeffskwang/TopoBlender/blob/7f9317b485e64b394df67d7b2428c4a3794cfca3/readme_images/trout_creek_hillshade_low_res.png" alt="rendered topography with hillshade view" width="500"/>
</p>
<p align="center">
Fig.2 - Topography viewed from a bird's-eye view, a hillshade map.
</p>

## What will you need
1. [Blender](https://www.blender.org/download/)
2. DEMs in [ASCII format](https://desktop.arcgis.com/en/arcmap/latest/manage-data/raster-and-images/esri-ascii-raster-format.htm) (.asc). DEMs in this format can be downloaded directly from [OpenTopography](https://opentopography.org/) (see image below) or can be generated from [landlab-based](https://landlab.readthedocs.io/en/master/reference/io/esri_ascii.html#landlab.io.esri_ascii.write_esri_ascii) models. If you have .tifs or other formats, you will need a way to convert your digital elevation models (DEMs) to ASCII format, e.g., [GDAL](https://gdal.org/), [QGIS](https://qgis.org/en/site/), ArcGIS.
<p align="center">
<img src="https://github.com/jeffskwang/TopoBlender/blob/29e5e84fc744642a1b600bfb2fd5061b13f7841f/readme_images/open_topo_ascii.png" alt="Blender UI" width="400"/>
</p>

3. *Optional* - A GPU will allow the render engine (CYCLES) to run faster
4. Inputs
    * .tif file of your DEM (located in **/TopoBlender/data** folder), this needs to be converted to .asc
    * .asc file of your DEM (located in **/TopoBlender/converted** folder)
    * .py file of your render settings (located in **/TopoBlender/parameters** folder)

## Converting .tif to .asc
In order for Blender to run without additional installations, TopoBlender requires the input DEM to have a ASCII file format. If you need to convert your DEM to this format, I recommend **gdal\_translate** in GDAL. An example script file (**convert_tif\_to\_asc\_example.sh**) is included. The script file assumes that GDAL is installed within an [Anaconda Environment](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html). Last, in addition to .tif files, GDAL can also convert other DEM filetypes to .asc.

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

The cube will be gone, and you will now see a small flat plane. This is your topography. To view the topography from the render's camera view, click the **Camera View** button.

<p align="center">
<img src="https://github.com/jeffskwang/TopoBlender/blob/5a394780c97979234d8a0c5733489a84f56fefd9/readme_images/UI_4.png" alt="Camera View Button" width="400"/>
</p>

This will show you the plane that we created that holds the topography data, but you will not see any relief in the topography. To see that you, will need to preview the render by click the **Viewport Shading** button the top-right corner of the viewport.

<p align="center">
<img src="https://github.com/jeffskwang/TopoBlender/blob/5a394780c97979234d8a0c5733489a84f56fefd9/readme_images/UI_5.png" alt="Viewport Shading Button" width="400"/>
</p>

After click **Viewport Shading** you will now see a preview of the render!

<p align="center">
<img src="https://github.com/jeffskwang/TopoBlender/blob/5a394780c97979234d8a0c5733489a84f56fefd9/readme_images/UI_6.png" alt="Render Preview" width="600"/>
</p>

You can also see a higher fidelity render in the **/TopoBlender/renders folder**. If you are running the example, the file is named **trout_creek.png**, also found [here](https://github.com/jeffskwang/TopoBlender/blob/925d863da14f670f595d5430afd5ec20c3487566/renders/trout_creek.png).

## Changing the Render Settings
TopoBlender has a couple user settings that will allow you to change the look of the rendered image. You can also use this code as a template and improve/modify it for your uses. I hope that this code can help get you started!

### Parameters
#### Main Controls
- **Topo_Blender_folder** - path to the TopoBlender folder
- **datafile** - path to the input .asc file containing the DEM
- **output** - path to the output .png file of the render
- **GPU_boolean** - setting that allows you to use a GPU (if you have one) to speed up the render. 0 = CPU, 1 = GPU
#### Camera Properties
- **camera_type** - type of camera to use. 'orthogonal' or 'perspective'
- **camera_tilt** - camera tilt in degrees. 0 degrees = side view, 90 degrees = top view
- **camera_rotation** - camera rotational location in degrees (CW from North). 0 degrees = camera shoots from the North, 180 degrees = camera shoots from the South
- **Orthogonal Camera**
   - **ortho_scale** - decides how "zoomed" in or out the camera is. default = 1.0
- **Perspective Camera**
   - **focal_length** = decides how "zoomed" in or out the camera is. default = 50mm
   - **f_stop** - changes the depth of field (dof). Use low values to get the "portrait mode effect" (blurry effect). low values = shallow dof, high values = wide dof
   - **shift_x** - shifts the camera horizontally if the topography is not centered to your liking
   - **shift_y** - shifts the camera vertically if the topography is not centered to your liking
#### Sun Properties
- **sun_tilt** - [sun altitude](https://pro.arcgis.com/en/pro-app/latest/tool-reference/3d-analyst/how-hillshade-works.htm). 0 degree = sunset, 90 degrees = noontime
- **sun_rotation** - [solar azimuth angle](https://pro.arcgis.com/en/pro-app/latest/tool-reference/3d-analyst/how-hillshade-works.htm). 0 degrees = sun in the North, 180 degrees = sun in the South
- **sun_intensity** -  intensity the sunlight. default = 0.1

#### Landscape Properties
- **number_of_subdivisions** - number of subdivisions, effectively settings the landscape resolution. Increasing this value will make the landscape more detailed but will require more computation resources to render. default = 500
- **exaggeration** - amount of vertical exaggeration to make relief more visable. default = 2.0

#### Render Properties
- **res_x** - horizontal resolution of image render
- **res_y** - vertical resolution of image render
- **samples** - number of samples the render engine takes to resolve the render. Higher values will resolve a better image but will require more computation resources. default = 10

## TopoBlender using Command Line
If you are a bit more code savvy, you can also run TopoBlender using a script. You will need to create a **parameters** file that contains information about the render settings, camera settings, and fileIO. The parameters are the same as the ones listed above. The **parameters** file needs to be saved in the **/TopoBlender/parameters** folder. You will either run the code using command prompt (windows) or terminal (linux/MacOS). If you use a script file (.sh) or a batch file (.bat) you will need to specify the following.

### Script File Example (.sh) (Linux/MacOS)
```
   #!/bin/bash
   ####USER SPECIFIED
   #Parameter File 
   parameter=trout_creek_ortho_example

   #Define locations of blender <--IMPORTANT, NEEDS TO BE UPDATED TO YOUR SYSTEM
   blender_location=/Applications/Blender.app/contents/MacOS

   ####AUTOMATED SECTION
   #TopoBlender file is assumed to be in the same directory as this .sh file
   TopoBlender_location=$(dirname $0)

   #moves to blender location to run blender
   cd $blender_location
   
   #Run TopoBlender
   ./Blender -b -P $TopoBlender_location/TopoBlender.py -- $TopoBlender_location/parameters/$parameter
```

### Batch File Example (.bat) (Windows)
```
   @echo off
   :: USER SPECIFIED
   :: Parameter File 
   set parameter=trout_creek_ortho_example

   :: Define locations of blender <--IMPORTANT, NEEDS TO BE UPDATED TO YOUR SYSTEM
   set blender_location=C:\Program Files\Blender Foundation\Blender 3.4

   :: AUTOMATED SECTION
   :: TopoBlender file is assumed to be in the same directory as this .sh file
   set TopoBlender_location=%cd%

   :: moves to blender location to run blender
   cd %blender_location%
   
   :: Run TopoBlender
   blender.exe -b -P %TopoBlender_location%/TopoBlender.py -- %TopoBlender_location%/parameters/%parameter%
```

The included [script](https://github.com/jeffskwang/TopoBlender/blob/main/_render_script_example.sh) and [batch](https://github.com/jeffskwang/TopoBlender/blob/main/_render_script_example.bat) files will render three higher-quality images:
- [**trout_creek_ortho.png**](https://github.com/jeffskwang/TopoBlender/blob/925d863da14f670f595d5430afd5ec20c3487566/renders/trout_creek_ortho.png) - An image taken at an oblique angle using an orthographic camera.
- [**trout_creek_persp.png**](https://github.com/jeffskwang/TopoBlender/blob/925d863da14f670f595d5430afd5ec20c3487566/renders/trout_creek_persp.png) - An image taken at an oblique angle using an perspective camera. A shallow depth of field is used to create a more "artistic" style where the close and far regions are slightly out of focus. 
- [**trout_creek_hillshade.png**](https://github.com/jeffskwang/TopoBlender/blob/925d863da14f670f595d5430afd5ec20c3487566/renders/trout_creek_hillshade.png) - An image taken at a planform view using an orthographic camera, creating a hillshade map. The sun altitude is 15 degrees and the sun azimuth is 315 degrees (sun in the NW) a default value for most hillshade algorithms.

That's it! Have fun using Blender!
