# Pygame-3D

![image](https://github.com/Anthony-Gambale/Pygame-3D/blob/main/images/1_screenshot.png)

Pygame 3D is a 3D model renderer built with Pygame, a 2D rendering API for python.

This project is a demo of an experimental mathematical technique that I came up with. This method allows the renderer to entirely skip the "view space" phase of traditional 3D rendering, saving a significant chunk of computation time.

### Install and Run
```
$ git clone https://github.com/Anthony-Gambale/Pygame-3D.git
$ python -m pip install pygame
$ python Pygame-3D/src/main.py
```

## Experimental Technique

The main feature of this program is *perspective projection.* It takes the vertices of a 3D model, plus information about a camera in 3D space, and 'projects' the vertices of each shape onto the screen plane.

### A traditional renderer
In a 3D renderer, whenever the camera is moved or rotated, a transformation matrix is applied to it. In Figure 1, transformation R is applied to rotate the camera. In a traditional 3D renderer, R inverse is calculated and applied to every single vertex in the scene. This is very computationally expensive, especially for intricate models, and scales with the detail in the scene.

![image](https://github.com/Anthony-Gambale/Pygame-3D/blob/main/images/2_traditional_rotate.png)  
*Figure 1: Traditional method for rotating camera. Computation scales with complexity of 3D models.*

### The main difference - plane modelling
Using this method, the screen plane is modelled in a more robust way. In a traditional 3D renderer, the screen plane is accepted to be parallel to the xy plane, shifted by some constant in the z direction. However, if the plane is modelled more robustly, it is possible to perform matrix transformations on its components, as shown in Figure 2.

![image](https://github.com/Anthony-Gambale/Pygame-3D/blob/main/images/3_my_rotate.png)  
*Figure 2: My method for rotating camera. Computation required is constant, and will never scale.*



### Finding intersection points

### Screen plane to xy plane transformation

### The consequences of this method
