
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

scene = cube_scene


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
    
        # key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass
            elif event.key == pygame.K_RIGHT:
                pass
            elif event.key == pygame.K_UP:
                pass
            elif event.key == pygame.K_DOWN:
                pass
            elif event.key == ord('w'):
                pass
            elif event.key == ord('a'):
                pass
            elif event.key == ord('s'):
                pass
            elif event.key == ord('d'):
                pass
            elif event.key == pygame.K_LSHIFT:
                pass
            elif event.key == pygame.K_SPACE:
                pass

    """ draw current scene """
    #  clear the previous frame
    win.fill((0, 0, 0))

    # add to the display
    for projected_shape in project_scene(scene):
        for projected_line in projected_shape.lines:
            projected_line.draw(win, win_width, win_height)

    # debug
    #test_line.draw(win, win_width, win_height)

    # update the display
    pygame.display.update()

pygame.quit()
