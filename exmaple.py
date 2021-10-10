
import pygame
import pygame3D

# initialize pygame3D scene and models
pygame.init()
scene = pygame3D.Scene(700, 700, title="Pygame3D Example") # new scene

# 3D models
model_location = "example_models/"
cube_model = pygame3D.read_model(model_location + "cube_model.txt")
plane_model = pygame3D.read_model(model_location + "plane_model.txt")
pyramid_model = pygame3D.read_model(model_location + "big_pyramid.txt")
floor_model = pygame3D.read_model(model_location + "floor.txt")

# change the colours of multiple objects in one line
pyramid_model, cube_model, plane_model = map(lambda x: x.set_colour("white"), [pyramid_model, cube_model, plane_model])
floor_model.set_colour("blue")

# add models to scene
scene.add_shape(floor_model)
scene.add_shape(pyramid_model, pygame3D.Vec3([100,0,1000]))
scene.add_shape(cube_model, pygame3D.Vec3([-300, 0, 1000]))
scene.add_shape(cube_model, pygame3D.Vec3([-100, 0, 1000]))
scene.add_shape(plane_model, pygame3D.Vec3([-300, 0, 1000]))

delay_time = 10
v_rot = 0.002 * delay_time # radians per delay tick
v_mov = 0.3 * delay_time # units of movement per delay tick

running = True
while running:

    # small delay between step events. 10 steps per second
    pygame.time.delay(delay_time)

    """ process user input """

    # check all events
    for event in pygame.event.get():

        # user quit the program
        if event.type == pygame.QUIT:
            running = False
    
    """ key presses """
    keys = pygame.key.get_pressed()

    scene.camera.move(keys, v_mov, v_rot)

    """ draw current scene """
    scene.refresh()

pygame.quit()
