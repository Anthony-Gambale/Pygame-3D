
import pygame
from projection import project_scene
from scene import cube_scene

pygame.init()

win=pygame.display.set_mode((500, 500))
pygame.display.set_caption("Pygame 3D")

Scene = cube_scene

run = True

while run:

    # small delay between step events. 10 steps per second
    pygame.time.delay(100)

    """ process user input """

    # check all events
    for event in pygame.event.get():

        # user quit the program
        if event.type == pygame.QUIT:
            run = False
        

    """ draw current scene """

    # add to the display
    
    # update the display
    pygame.display.update()

pygame.quit()