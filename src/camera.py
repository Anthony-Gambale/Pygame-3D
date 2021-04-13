

# note: see math sketch on github page for context on variable names

from vector import *
from math import cos, sin


class Camera():


    def __init__(self):

        self.c = Vec3([0, 0, 0]) # initialize the c vector to be 0,0,0
        self.n = Vec3([0, 0, 1]) # normal vector, pointing into the z axis from the origin. this is the direction the camera faces
        self.k = -500 # scalar distance from c to s
        self.s = self.c.add(self.n.scale(self.k)) # define centre of screen, offset from the camera point by a scaled version of normal vector

        # local basis vectors of the plane in 3D are just i and j for now
        # since the plane is initialised to be the xy plane, only translated in the z direction
        # when the user rotates the camera, the basis vectors must be rotated
        # when the user translates the camera, the basis vectors remain the same
        self.bx = Vec3([1, 0, 0])
        self.by = Vec3([0, 1, 0])


    def update(self):
        """re-define s from new k, n and c values (if they change, this function is called)"""
        self.s = self.c.add(self.n.scale(self.k)) # define centre of screen, offset from the camera point by a scaled version of normal vector


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


    def turn_x(self, a):
        """take some angle a in radians, and rotate the normal vector about the basis vector, bx.
        https://math.stackexchange.com/questions/3130813/rotating-a-vector-perpendicular-to-another"""
        
        self.n = (self.n.scale(cos(a))).add(self.by.scale(sin(a)))

        self.by = self.bx.cross_product_3D(self.n)

        self.update() # update the screen position


    def turn_y(self, a):
        """take some angle a in radians, and rotate the normal vector about the basis vector, by.
        https://math.stackexchange.com/questions/3130813/rotating-a-vector-perpendicular-to-another"""

        self.n = (self.n.scale(cos(a))).add(self.bx.scale(sin(a)))

        self.bx = self.n.cross_product_3D(self.by)

        self.update() # update the screen position
