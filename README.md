# Pygame-3D

![image](https://github.com/Anthony-Gambale/Pygame-3D/blob/main/images/1_screenshot.png)

Pygame 3D is an extension on Pygame, an API for python which renders 2D shapes. It uses Pygame's 2D functions to render 3D models.

This project is a demo implementation of an experimental mathematical technique that I came up with. This method allows the renderer to entirely skip the "view space" transformation step of a traditional 3D renderer. This saves a significant chunk of computation time.

## Install and Run

Download Pygame
```
python -m pip install pygame
```

Run the main file
```
python src/main.py
```

## Experimental Perspective-Projection Technique

This demo program uses a different method for traditional perspective projection, to completely avoid all computation necessary in the traditional "view space" step.
