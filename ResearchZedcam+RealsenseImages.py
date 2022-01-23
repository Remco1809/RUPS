import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2 as cv
import open3d as o3d


'''
#eigen beelden VGA
color_raw = o3d.io.read_image("/media/jordi/USB DISK/test1512/test/image/ZED_image657.png")
depth_raw = o3d.io.read_image("/media/jordi/USB DISK/test1512/test/depth/Depth_657.png")
rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(color_raw, depth_raw, convert_rgb_to_intensity=False)
    
print(rgbd_image)
'''


#beelden uit tutorial, gemaakt met intel realsense
color_raw = o3d.io.read_image("/media/jordi/USB DISK/test1512/image01364.png")
depth_raw = o3d.io.read_image("/media/jordi/USB DISK/test1512/depth01364.png")
rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(color_raw, depth_raw)

plt.subplot(1, 2, 1)
plt.title('Image from tutorial by Intel Realsense')
plt.imshow(rgbd_image.color)

plt.subplot(1, 2, 2)
plt.title('Corresponding depth image')
plt.imshow(rgbd_image.depth)
plt.show()

#eigen beelden HD720
color_raw = o3d.io.read_image("/media/jordi/USB DISK/test1512/ZED_image0.png")
depth_raw = o3d.io.read_image("/media/jordi/USB DISK/test1512/Depth_0.png")
rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(color_raw, depth_raw) #convert_rgb_to_intensity=False) #convert_rgb_to_intensity=False)  #toegevoegd, anders zwart beeld

plt.subplot(1, 2, 1)
plt.title('Image of kitchen made with Zedcam')
plt.imshow(rgbd_image.color)

plt.subplot(1, 2, 2)
plt.title('Corresponding depth image')
plt.imshow(rgbd_image.depth)
plt.show()

#eigen beelden Realsense, van deze laatste 2 images wordt ook het 3D part gemaakt.
color_raw = o3d.io.read_image("/media/jordi/UUI/datasetboom2/realsense/color/000275.jpg")
depth_raw = o3d.io.read_image("/media/jordi/UUI/datasetboom2/realsense/depth/000275.png")
rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(color_raw, depth_raw, convert_rgb_to_intensity=False)  #toegevoegd, anders zwart beeld: , convert_rgb_to_intensity=False

print(rgbd_image)

plt.subplot(1, 2, 1)
plt.title('Image of tree by Intel Realsense')
plt.imshow(rgbd_image.color)

plt.subplot(1, 2, 2)
plt.title('Corresponding depth image')
plt.imshow(rgbd_image.depth)
plt.show()


camera_intrinsic = o3d.camera.PinholeCameraIntrinsic(o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault)

pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd_image, camera_intrinsic)
# Flip it, otherwise the pointcloud will be upside down
pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])


vis = o3d.visualization.Visualizer()
vis.create_window()
vis.add_geometry(pcd)
o3d.visualization.ViewControl.set_zoom(vis.get_view_control(), 0.5)
vis.run()

