################################################################################
# Import Libraries
import bpy
import numpy as np
import math
from mathutils import Matrix
import importlib
import sys
import os

#Adding the parameters folder to the list of folders that python looks for 
#module files in. Also, imports the parameter file. Add additional arguments
#if you want to modify the code to go through a batch of files.
argv = sys.argv
argv = argv[argv.index("--") + 1:] 
module_file = argv[0]
function_folder = os.path.dirname(module_file)
sys.path.insert(1, function_folder)
parameters = importlib.import_module(os.path.basename(module_file))
importlib.reload(parameters)
globals().update(parameters.__dict__)

################################################################################
# Remove everything from the scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

################################################################################
# This sets the render enginer to CYCLES.
# In order for TopoBlender to render your topography correctly, you must use
# this render engine. This engine is optimized for GPUs, so if your computer
# lacks a GPU, TopoBlender may be slow.

# define current scene
scn = bpy.context.scene

# check the render engine, and change to CYCLES
if not scn.render.engine == 'CYCLES':
    scn.render.engine = 'CYCLES'

#if cycles, change to gpu rendering if user selects GPU
if scn.render.engine == 'CYCLES':
    if GPU_boolean == 1:
        scn.cycles.device = 'GPU'

################################################################################
# read in .asc file
data = np.loadtxt(datafile,skiprows=6)

# find nodata value by iterating through the header
with open(datafile) as f:
  for line in f:
    arr = line.split()
    if len(arr) == 2:   # 2 columns signifies the header
        if arr[0] == 'NODATA_value':
            nodata_value = float(arr[1])
        elif arr[0] == 'cellsize':
            dx = float(arr[1])

# find minimum elevation
data_min = np.min(data[data!=nodata_value])
# find maximum elevation
data_max = np.max(data[data!=nodata_value])
# calculate total relief
relief = data_max - data_min
#scale values from 0 to 1
data[data!=nodata_value] = (data[data!=nodata_value] - data_min) / relief
#convert nodata value to nan
data[data==nodata_value] = np.nan
# data y_length we use this to scale the topography
y_length = (2.0+float(data.shape[1])) * dx 
# create an image that holds the data
displacement_array = np.zeros(((data.shape[0]+2)*(data.shape[1]+2)*4), dtype=np.float32)
color_array = np.zeros(((data.shape[0]+2)*(data.shape[1]+2)*4), dtype=np.float32)

# Add a 1-pixel border around the entire topography and rescale the topgraphy
# so minimum elevation is zero and the maximum elevation is 1.
k=0
for j in range(0,data.shape[1]+2):
    for i in range(0,data.shape[0]+2):
        i_data = i - 1
        j_data = j - 1

        i_minus = max(i_data-1,0)
        i_plus = min(i_data+1,data.shape[0]-1)
        j_minus = max(j_data-1,0)
        j_plus = min(j_data+1,data.shape[1]-1)
        
        i_data = min(max(i_data,0),data.shape[0]-1)
        j_data = min(max(j_data,0),data.shape[1]-1)
        
        if i >= 1 and j >= 1 and i <= data.shape[0] and j <= data.shape[1]:
            if np.isnan(data[i_data,j_data]):
                displacement_array[k:k+4] = np.nan
                color_array[k:k+4] = 1.0
            else:
                displacement_array[k:k+4] = data[i_data,j_data]
                color_array[k:k+4] = data[i_data,j_data]
        else:
            displacement_array[k:k+4] = np.nan
            color_array[k:k+4] = 1.0
        k+=4
        
# Create an image from the datafile        
displacement_image = bpy.data.images.new('displacement_data', data.shape[0]+2, data.shape[1]+2, alpha=False, float_buffer = True)
color_image = bpy.data.images.new('color_data', data.shape[0]+2, data.shape[1]+2, alpha=False, float_buffer = True)
# Fast way to set pixels (since 2.83)
displacement_image.pixels.foreach_set(displacement_array)
color_image.pixels.foreach_set(color_array)
# Pack the image into .blend so it gets saved with it
displacement_image.pack()
color_image.pack()

#make plane
plane_size = 1.0
topo_mesh = bpy.ops.mesh.primitive_plane_add(size=plane_size)
topo_obj = bpy.context.active_object

#Change the shape of the object to match data_aspect
topo_obj.scale = ((2.0+data.shape[0])/(2.0+data.shape[1]),1,1)

#add material
topo_mat = bpy.data.materials.new("topo_mat")
topo_mat.cycles.displacement_method = "DISPLACEMENT"
topo_mat.use_nodes = True

#calculate subdivisions
order_of_magnitude = math.floor(math.log10(number_of_subdivisions))
first_digit = int(np.round(number_of_subdivisions / (10.0 ** order_of_magnitude)))

topo_obj.data.materials.append(topo_mat)
bpy.ops.object.mode_set(mode="EDIT")
for i in range(0,order_of_magnitude):
    bpy.ops.mesh.subdivide(number_cuts=10)
bpy.ops.mesh.subdivide(number_cuts=first_digit)
bpy.ops.object.mode_set(mode="OBJECT")

#add image node - determines the displacement
displacement_image_node = topo_mat.node_tree.nodes.new("ShaderNodeTexImage")
#assign png to image to node
displacement_image_node.image = displacement_image
#change colorspace to b&w
displacement_image_node.image.colorspace_settings.name="Linear"

#add image node - determines the color of the lanscape
color_image_node = topo_mat.node_tree.nodes.new("ShaderNodeTexImage")
#assign png to image to node
color_image_node.image = color_image
#change colorspace to b&w
color_image_node.image.colorspace_settings.name="Linear"
    
#add displacement node - done
displacement_node = topo_mat.node_tree.nodes.new("ShaderNodeDisplacement")
displacement_node.inputs.get("Scale").default_value = exaggeration * plane_size * relief / y_length
displacement_node.inputs.get("Midlevel").default_value = 0.0

#add world sky - done
topo_world = bpy.data.worlds.new('topo_world')
topo_world.use_nodes = True
topo_world_node = topo_world.node_tree.nodes.new("ShaderNodeTexSky")
topo_world_node.sun_elevation = np.radians(sun_tilt)
topo_world_node.sun_rotation = np.radians(sun_rotation-90.0)
topo_world_node.sun_intensity = sun_intensity
topo_world.node_tree.links.new(topo_world_node.outputs['Color'], topo_world.node_tree.nodes['Background'].inputs[0])

#add camera - done
camera_distance = 2.0 #meters
cam = bpy.data.cameras.new('topo_cam')
cam_obj = bpy.data.objects.new('topo_cam',cam)
cam_obj.rotation_euler = (np.radians(90.0 - camera_tilt), np.radians(0), np.radians(270.0 - camera_rotation))
cam_obj.matrix_basis @= Matrix.Translation((0.0, 0.0, camera_distance))

if camera_type == 'orthogonal':
    bpy.data.cameras['topo_cam'].type = 'ORTHO'
    bpy.data.cameras['topo_cam'].ortho_scale = ortho_scale
elif camera_type == 'perspective':
    bpy.data.cameras['topo_cam'].type = 'PERSP'
    bpy.data.cameras['topo_cam'].lens = focal_length
    bpy.data.cameras['topo_cam'].shift_x = shift_x
    bpy.data.cameras['topo_cam'].shift_y = shift_y
    bpy.data.cameras['topo_cam'].dof.use_dof = True
    bpy.data.cameras['topo_cam'].dof.aperture_fstop = f_stop
    bpy.data.cameras['topo_cam'].dof.focus_distance = camera_distance
    
#connect nodes - done
topo_mat.node_tree.links.new(displacement_image_node.outputs["Color"], \
                             displacement_node.inputs["Height"])
topo_mat.node_tree.links.new(displacement_node.outputs["Displacement"], \
                             topo_mat.node_tree.nodes["Material Output"].inputs["Displacement"])
topo_mat.node_tree.links.new(color_image_node.outputs["Color"], \
                             topo_mat.node_tree.nodes["Principled BSDF"].inputs[0])

bpy.context.scene.collection.objects.link(cam_obj)                         
bpy.context.scene.camera = cam_obj    
bpy.context.scene.world = topo_world

#render settings
bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.cycles.samples = samples
bpy.context.scene.render.resolution_x = int(res_x)
bpy.context.scene.render.resolution_y = int(res_y)
bpy.context.scene.render.filepath = output
bpy.ops.render.render(write_still=True)