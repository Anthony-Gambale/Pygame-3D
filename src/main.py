
import pygame
from projection import project_scene
from scene import cube_scene
from vector import Vec3

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
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        pass
    if keys[pygame.K_RIGHT]:
        pass
    if keys[pygame.K_UP]:
        pass
    if keys[pygame.K_DOWN]:
        pass
    if keys[ord('w')]:
        pass
    if keys[ord('a')]:
        scene.camera.translate(Vec3([-5, 0, 0]))
    if keys[ord('s')]:
        pass
    if keys[ord('d')]:
        pass
    if keys[pygame.K_LSHIFT]:
        pass
    if keys[pygame.K_SPACE]:
        pass

    """ draw current scene """
    #  clear the previous frame
    win.fill((0, 0, 0))

    # add to the display
    for projected_shape in project_scene(scene):
        for projected_line in projected_shape.lines:
            projected_line.draw(win, win_width, win_height)

    # update the display
    pygame.display.update()

pygame.quit()
