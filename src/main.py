
import pygame
from projection import project_scene
from scene import cube_scene

### debug
# from scene import Line2D
# from vector import Vec2
# test_line = Line2D(Vec2([0, 0]), Vec2([20, 300])) # for testing

pygame.init()

win_width = 700
win_height = win_width
win=pygame.display.set_mode((win_width, win_height))
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

    # debug
    #test_line.draw(win, win_width, win_height)

    # update the display
    pygame.display.update()

pygame.quit()
