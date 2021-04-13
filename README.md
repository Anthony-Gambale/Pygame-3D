# Pygame-3D

Pygame 3D is an API for Pygame that allows for the rendering of simple 3D objects.

I've used an experimental mathematical technique to avoid the "view/camera space" phase of a traditional 3D renderer, saving a large chunk of computation time.

## Install and Run

Download Pygame
Run the main file
```
python src/main.py
```

## Experimental Projection Technique

This demo program uses a different method for traditional perspective projection, to completely avoid all computation necessary in the traditional "view space" step.
