

# note: see math scratch on github page for context on variable names

from vector import *

class Camera():

    def __init__(self):

        self.c = Vec3([0, 0, 0]) # initialize the c vector to be 0,0,0

        self.n = Vec3([0, 0, 1]) # normal vector, pointing into the x axis from the origin

        self.k = 1 # scalar distance from c to s

        self.s = self.c.add(self.k * self.n) # define centre of screen, offset from the camera point by a scaled version of normal vector