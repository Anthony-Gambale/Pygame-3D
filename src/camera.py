

# note: see math sketch on github page for context on variable names

from vector import *
from math import cos, sin


class Camera():

    def __init__(self):

        self.c = Vec3([0, 0, 0]) # initialize the c vector to be 0,0,0
        self.n = Vec3([0, 0, 1]) # normal vector, pointing into the x axis from the origin
        self.k = 1 # scalar distance from c to s
        self.s = self.c.add(self.k * self.n) # define centre of screen, offset from the camera point by a scaled version of normal vector


    def translate(self, m):
        """translate the camera with some velocity, Vec3 m"""
        self.c = self.c.add(m)
        self.s = self.s.add(m)
    

    def turn_x(self, a):
        """take some angle a in radians and rotate the normal vector. see https://en.wikipedia.org/wiki/Rotation_matrix#In_three_dimensions"""
        
        self.s = self.c.add(self.k * self.n) # define centre of screen, offset from the camera point by a scaled version of normal vector


    def turn_y(self, a):
        """take some angle a in radians and rotate the normal vector. see Camera.turn_x for source."""
    
        self.s = self.c.add(self.k * self.n) # define centre of screen, offset from the camera point by a scaled version of normal vector


    def turn_z(self, a):
        """take some angle a in radians and rotate the normal vector. see Camera.turn_x for source."""

        self.s = self.c.add(self.k * self.n) # define centre of screen, offset from the camera point by a scaled version of normal vector
