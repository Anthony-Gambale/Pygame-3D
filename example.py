
import pygame
import pygame3D


# initialize pygame3D scene and models
pygame.init()
scene = pygame3D.Scene(700, 700) # new scene
with open("models/cube_model.txt", 'r') as f: data = f.readlines()
f.close()
cube_model = pygame3D.Shape3D(data)
scene.add_shape(cube_model)


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
    
    keys = pygame.key.get_pressed()

    scene.camera.move(keys, v_mov, v_rot)

    """ draw current scene """
    scene.refresh()

    # update the display
    pygame.display.update()

pygame.quit()