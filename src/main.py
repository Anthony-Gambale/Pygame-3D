
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

delay_time = 10

v_rot = 0.005 * delay_time # radians per delay tick
v_mov = 0.3 * delay_time # units of movement per delay tick

run = True

while run:

    # small delay between step events. 10 steps per second
    pygame.time.delay(delay_time)

    """ process user input """

    # check all events
    for event in pygame.event.get():

        # user quit the program
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        scene.camera.turn_y(-v_rot)
    if keys[pygame.K_RIGHT]:
        scene.camera.turn_y(v_rot)
    if keys[pygame.K_UP]:
        scene.camera.turn_x(v_rot)
    if keys[pygame.K_DOWN]:
        scene.camera.turn_x(-v_rot)
    if keys[ord('w')]:
        scene.camera.move_forward(v_mov)
    if keys[ord('a')]:
        scene.camera.move_left(v_mov)
    if keys[ord('s')]:
        scene.camera.move_backward(v_mov)
    if keys[ord('d')]:
        scene.camera.move_right(v_mov)
    if keys[pygame.K_LSHIFT]:
        scene.camera.translate(Vec3([0, -v_mov, 0]))
    if keys[pygame.K_SPACE]:
        scene.camera.translate(Vec3([0, v_mov, 0]))

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
