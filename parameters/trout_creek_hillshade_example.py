################File IO##############
Topo_Blender_folder = "/Users/jeffreykwang/Documents/GitHub/TopoBlender" #IMPORTANT - THIS NEEDS TO POINT TO THE TOPOBLENDER FOLDER TO WORK
datafile = Topo_Blender_folder + "/converted/trout_creek.asc"
output = Topo_Blender_folder + "/renders/trout_creek_hillshade.png"
#####################################


##########camera parameters##########
#camera type
camera_type = 'orthogonal' #orthogonal or perspective 

#orthogonal
ortho_scale = 1.0 #when using orthogonal scale, increase to "zoom" out

#perspective
focal_length = 50.0 #mm when using perspective camera, increase to zoom in
f_stop = 0.75 #affects depths of field, lower for a shallow dof, higher for wide dof
shift_x = 0.0 # you may need to shift the camera to center the topo in the frame
shift_y = -0.05 # you may need to shift the camera to center the topo in the frame

#camera location
camera_tilt = 90.0 #degrees from horizontal
camera_rotation = 180.0 #camera location degrees CW from North
######################################


##########sun properties##############
sun_tilt = 15.0 #degrees from horizontal
sun_rotation = 315.0 #degrees CW from North
sun_intensity = 0.1 #sun intensity
######################################


#####landscape representation#########
number_of_subdivisions = 1000 #number of subvisions, more increases the detail
exaggeration = 2.0 #vertical exaggeration
######################################


#########render settings##############
res_x = 2400 #x resolution of the render
res_y = 2118 #y resolution of the render
samples = 20 #number of samples that decides how "good" the render looks. more is better but takes longer
######################################