# Pygame-3D

![image](https://github.com/Anthony-Gambale/Pygame-3D/blob/main/images/1_screenshot.png)

Pygame 3D is an extension on Pygame, a 2D rendering API. It allows for the rendering of 3D models.

This project is an implementation of an experimental mathematical technique that I came up with. It allows the renderer to completely skip the "view space" transformation step of a traditional 3D renderer, saving a significant chunk of computation time.

## Install and Run

Download Pygame
Run the main file
```
python src/main.py
```

## Experimental Projection Technique

This demo program uses a different method for traditional perspective projection, to completely avoid all computation necessary in the traditional "view space" step.
