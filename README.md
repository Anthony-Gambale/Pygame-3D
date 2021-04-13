# Pygame-3D

![image](https://github.com/Anthony-Gambale/Pygame-3D/blob/main/images/1_screenshot.png)

Pygame 3D is a 3D model renderer built with Pygame, a 2D rendering API for python.

This project is a demo of an experimental mathematical technique that I came up with. This method allows the renderer to entirely skip the "view space" phase of traditional 3D rendering, saving a significant chunk of computation time.

### Install and Run
```
$ python -m pip install pygame
$ python src/main.py
```

## Experimental Technique

The main feature of this program is perspective projection. It takes the vertices of a 3D model, plus information about a camera situated in 3D space, and 'projects' the vertices of each shape onto the screen plane.

#### The difference from a traditional renderer

#### Finding intersection points

#### Transforming intersection points to xy plane

#### The consequences of this method
