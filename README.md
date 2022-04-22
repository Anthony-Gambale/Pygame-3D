# Pygame-3D

![image](https://github.com/Anthony-Gambale/Pygame-3D/blob/main/images/1.5_screenshot.png)

Pygame 3D is a 3D rendering package for Pygame. It does perspective-projection onto a 2D plane in the space, representing a virtual screen, and uses Pygame's regular 2D drawing functions to display the result of the projection.

### Install and Use
The `pygame3D` folder is the core package that you can import into your own pygame projects. See `example.py` in this repository for an example of how to use pygame3D.

## Traditional renderer "view space" computation
In a traditional 3D renderer, whenever some transformation R would be applied to the camera, the inverse of that transformation is applied to every model in the scene instead.  

This creates the illusion that R is being applied to the camera, without having to move the screen plane.

This computation is referred to as transforming into "view space."

![image](https://github.com/Anthony-Gambale/Pygame-3D/blob/main/images/2_traditional_rotate.png)  
*Figure 1: Traditional method for rotating camera. Computation scales with complexity of 3D models.*  

## Virtual 2D screen
In this program, the screen is modelled as a 2D plane with rotational and translational motion. This skips the view-space computation, but ends up making perspective projection much more costly, resulting in overall worse performance.

![image](https://github.com/Anthony-Gambale/Pygame-3D/blob/main/images/3.0_my_rotate.png)  
*Figure 2: My method for rotating camera. Computation required is constant, and will never scale.*

A screen plane is defined by local basis vectors and a normal vector, as shown in Figure 3. These vectors are orthonormal.

![image](https://github.com/Anthony-Gambale/Pygame-3D/blob/main/images/3.1_plane_definition.png)  
*Figure 3: Robust definition of a screen. Plane with orthonormal basis.*  

Figure 4 has a screen plane, with an extra point representing the camera position. The camera point is offset from the centre of the screen by a factor k of the normal vector.

![image](https://github.com/Anthony-Gambale/Pygame-3D/blob/main/images/3.2_plane_definition.png)  
*Figure 4: Data required to model virtual screen.*

Whenever a transformation is made to the camera (i.e. translating the camera, rotating the camera) these transformations are applied to the camera vectors and values, rather than to the world around the camera.

## Projecting onto virtual screen
The method I use for projecting space onto the virtual screen is as follows.

 - Define ray as parametric line
 - Substitute ray point into plane equation, and solve for t
 - Substitute t back into line equation to get intersection point x

![image](https://github.com/Anthony-Gambale/Pygame-3D/blob/main/images/4_intersections.png)  
*Figure 5: Calculating the point of intersection of a ray and screen plane.*  

## Transforming screen plane to xy plane
Once the intersection point is found, it must be mapped onto the xy plane, giving pixel coordinates for rasterization.

 - Subtract intersection point x from centerpoint s, to get relative distance d
 - Project d onto local basis vectors to get x and y magnitudes  

![image](https://github.com/Anthony-Gambale/Pygame-3D/blob/main/images/5_xy_transform.png)  
*Figure 6: Projecting relative distance onto local basis vectors.*  
