# Pygame-3D

![image](https://github.com/Anthony-Gambale/Pygame-3D/blob/main/images/1.5_screenshot.png)  

Pygame 3D is a 3D rendering package for Pygame. It does perspective-projection onto a 2D plane in the space, representing a virtual screen, and uses Pygame's regular 2D drawing functions to display the result of the projection.

### Install and Use
The `pygame3D` folder is the core package that you can import into your own pygame projects. See `example.py` in this repository for an example of how to use pygame3D.

## Virtual 2D screen
The user's physical screen, as it sits within the virtual 3D world, is modelled as a plane with rotational and translational motion.

![image](https://github.com/Anthony-Gambale/Pygame-3D/blob/main/images/3.0_my_rotate.png)  

The screen plane is defined by local basis vectors and a normal vector, as shown below. These vectors are orthonormal.

![image](https://github.com/Anthony-Gambale/Pygame-3D/blob/main/images/3.1_plane_definition.png)  

The camera is modelled using a point offset from the centre of the screen. The offset is in the direction of the normal vector by some factor k. This models the point of view of the user sitting behind the screen.

![image](https://github.com/Anthony-Gambale/Pygame-3D/blob/main/images/3.2_plane_definition.png)  

Whenever a transformation is made to the camera (i.e. translating the camera, rotating the camera) these transformations are applied to the camera vectors and values.

## Projecting onto virtual screen
The method I use for projecting space onto the virtual screen is as follows.

 - Define ray as parametric line
 - Substitute ray point into plane equation, and solve for t
 - Substitute t back into line equation to get intersection point x

![image](https://github.com/Anthony-Gambale/Pygame-3D/blob/main/images/4_intersections.png)  

## Transforming screen plane to xy plane
Once the intersection point is found, it must be mapped onto the xy plane, giving pixel coordinates for rasterization.

 - Subtract intersection point x from centerpoint s, to get relative distance d
 - Project d onto local basis vectors to get x and y magnitudes  

![image](https://github.com/Anthony-Gambale/Pygame-3D/blob/main/images/5_xy_transform.png)  
