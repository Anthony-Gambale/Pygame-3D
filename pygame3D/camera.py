

# note: see math sketches on github page for context on variable names

from pygame3D.vector import *
from math import cos, sin
import pygame

class Camera():


    def __init__(self, gravity=True, height=20):

        self.c = Vec3([0, height, 0]) # initialize the c vector to be 0,0,0
        self.n = Vec3([0, 0, 1]) # normal vector, pointing into the z axis from the origin. this is the direction the camera faces
        self.k = -500 # scalar distance from c to s
        self.s = self.c.add(self.n.scale(self.k)) # define centre of screen, offset from the camera point by a scaled version of normal vector

        # local basis vectors of the plane in 3D are just i and j for now
        # since the plane is initialised to be the xy plane, only translated in the z direction
        # when the user rotates the camera, the basis vectors must be rotated
        # when the user translates the camera, the basis vectors remain the same
        self.bx = Vec3([1, 0, 0])
        self.by = Vec3([0, 1, 0])

        # gravitation
        self.gravity = gravity
        self.fallspeed = 0
        self.height = height


    def apply_gravity(self):
        if self.gravity:
            self.fallspeed += 0.08
            if self.c.elems[1] - self.fallspeed <= self.height: self.c.elems[1] = self.height
            else: self.move_down(self.fallspeed)


    def update(self):
        """re-define s from new k, n and c values (if they change, this function is called)"""
        self.s = self.c.add(self.n.scale(self.k)) # define centre of screen, offset from the camera point by a scaled version of normal vector


    def move(self, keys, v_mov, v_rot):
        if keys[pygame.K_LEFT]:
            self.turn_y(-v_rot)
        if keys[pygame.K_RIGHT]:
            self.turn_y(v_rot)
        if keys[pygame.K_UP]:
            self.turn_x(v_rot)
        if keys[pygame.K_DOWN]:
            self.turn_x(-v_rot)
        if keys[ord('w')]:
            self.move_forward(v_mov)
        if keys[ord('a')]:
            self.move_left(v_mov)
        if keys[ord('s')]:
            self.move_backward(v_mov)
        if keys[ord('d')]:
            self.move_right(v_mov)
        if keys[pygame.K_LSHIFT]:
            if not self.gravity: self.move_down(v_mov)
        if keys[pygame.K_SPACE]:
            if self.gravity:
                if self.c.elems[1] == self.height: self.fallspeed = -4.5
            else:
                self.move_up(v_mov)


    def translate(self, m):
        """translate the camera with some velocity, Vec3 m"""
        self.c = self.c.add(m) # translate the camera
        self.update() # update the screen position
    

    def move_forward(self, velocity):
        """move the camera 'forward' relatiev to normal vector"""
        self.translate(self.n.scale(velocity))
    
    
    def move_backward(self, velocity):
        """move the camera 'backward' relative to normal vector"""
        self.translate(self.n.scale(-velocity))


    def move_right(self, velocity):
        """move the camera 'right' relative to basis vector"""
        self.translate(self.bx.scale(velocity))


    def move_left(self, velocity):
        """move the camera 'left' relative to basis vector"""
        self.translate(self.bx.scale(-velocity))


    def move_up(self, velocity):
        """move the camera directly up in the scene, irrespective of basis vector"""
        self.translate(Vec3([0, velocity, 0]))

    
    def move_down(self, velocity):
        """move the camera directly down in the scene, irrespective of basis vector"""
        self.translate(Vec3([0, -velocity, 0]))


    def turn_x(self, a):
        """take some angle a in radians, and rotate the normal vector about the basis vector, bx.
        https://math.stackexchange.com/questions/3130813/rotating-a-vector-perpendicular-to-another"""
        
        self.n = (self.n.scale(cos(a))).add(self.by.scale(sin(a)))

        self.by = self.n.cross_product_3D(self.bx)

        self.update() # update the screen position


    def turn_y(self, a):
        """take some angle a in radians, and rotate the normal vector about the basis vector, by.
        https://math.stackexchange.com/questions/3130813/rotating-a-vector-perpendicular-to-another"""

        # self.n = (self.n.scale(cos(a))).add(self.bx.scale(sin(a)))
        # self.bx = self.by.cross_product_3D(self.n)

        rotation_matrix = Matrix([
            Vec3([cos(a), 0, sin(a)]),
            Vec3([0, 1, 0]),
            Vec3([-sin(a), 0, cos(a)])
        ])

        self.n = self.n.transform(rotation_matrix)
        self.bx = self.bx.transform(rotation_matrix)
        self.by = self.by.transform(rotation_matrix)

        self.update() # update the screen position


    def isBehind(self, point):
        """check if the given point is behind the view plane"""
        diff = self.c.sub(point) # difference between player position and point
        diff_proj = diff.project(self.n) # get the component of the difference pointing in the direction of the normal vector
        if diff_proj >= 0: print("something is behind the view plane")
        return diff_proj >= 0
