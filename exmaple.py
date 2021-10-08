
import pygame
import pygame3D


# initialize pygame3D scene and models
pygame.init()
scene = pygame3D.Scene(700, 700, True) # new scene
cube_model = pygame3D.read_model("example_3D_models/cube_model.txt")
plane_model = pygame3D.read_model("example_3D_models/plane_model.txt")
pyramid_model = pygame3D.read_model("example_3D_models/big_pyramid.txt")
scene.add_shape(pyramid_model, pygame3D.Vec3([100,0,400]))
scene.add_shape(cube_model)
scene.add_shape(cube_model.clone(), pygame3D.Vec3([200, 0, 0]))
scene.add_shape(plane_model)

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
