# Pygame-3D

![image](https://github.com/Anthony-Gambale/Pygame-3D/blob/main/images/1_screenshot.png)

Pygame 3D is a 3D model renderer for Pygame. It uses Pygame's 2D rendering functions to display 3D models.

This project is an experimental demo of a mathematical technique that I came up with. Using this technique, the renderer can skip the "view space" phase of traditional 3D rendering in its entirety, saving a significant chunk of computation time.

### Install and Run
```
$ git clone https://github.com/Anthony-Gambale/Pygame-3D.git
$ python -m pip install pygame
$ python Pygame-3D/src/main.py
```

## Perspective-Projection Technique

The mathematical technique that I've come up with is in optimizing perspective projection.

### How a traditional renderer works
In a 3D renderer, whenever the camera is moved or rotated, a transformation matrix is applied to it. In Figure 1, transformation R is applied to rotate the camera.  

In a traditional 3D renderer, R inverse is calculated, and applied to every single vertex in the scene. This creates the illusion that R is being applied to the camera, while letting the screen plane remain in place.  

This is very computationally expensive, especially for intricate models, and scales with the detail in the scene.

![image](https://github.com/Anthony-Gambale/Pygame-3D/blob/main/images/2_traditional_rotate.png)  
*Figure 1: Traditional method for rotating camera. Computation scales with complexity of 3D models.*

### The main difference: plane modelling
In my method, the screen plane is modelled in a more robust way.  

In a traditional 3D renderer, the screen plane must remain parallel to the xy plane, shifted by some constant in the z direction. However, if the plane is modelled more robustly, it is possible to perform matrix transformations on its components, as shown in Figure 2. This saves a large chunk of computation time.

![image](https://github.com/Anthony-Gambale/Pygame-3D/blob/main/images/3.0_my_rotate.png)  
*Figure 2: My method for rotating camera. Computation required is constant, and will never scale.*

The plane is modelled by a normal vector, local basis vectors, and a point at its centre, as shown in Figure 3. There is also a focal point for the camera, which is distanced from the plane by a factor of n.

![image](https://github.com/Anthony-Gambale/Pygame-3D/blob/main/images/3.1_plane_definition.png)  
*Figure 3: Robust plane definition.*

When the program starts, the camera position c is initialized to 0,0,0. The normal vector is initialized to a unit in the z direction, and the local basis vectors are units in the x and y direction. The k constant is just some number of units to separate c from s.  

Whenever a transformation is 'requested' from the user (i.e. moving the camera, rotating the camera) these transformations are all applied to the camera vectors and values, rather than to the world around the camera.

### Finding intersection points

### Transforming screen plane to xy plane

### The consequences of this method
