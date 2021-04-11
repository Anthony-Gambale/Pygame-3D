

from vector import Vec3, Vec2
from camera import Camera


"""Lines"""
class Line():
    def __init__(self, p1, p2):
        self.p1 = p1 # p1 and p2 are either Vec2 or Vec3 objects, indicating the start and end points of the line
        self.p2 = p2

class Line2D(Line):
    def gradient(self):
        """return constant gradient of the line."""
        return (self.p1.sub(self.p2)).magnitude() # does not modify self.p1 or self.p2

class Line3D(Line):
    def gradient(self):
        """return a vector-gradient of the line. I.e., in the x = p + mt form, the m vector."""
        return self.p1.sub(self.p2) # difference between two points known to lie on line


"""Shapes"""
class Shape2D():
    def __init__(self, edges):
        self.points = edges # list of line2D objects

class Shape3D():
    def __init__(self, edges):
        self.points = edges # list of Line3D objects


"""Scene (shapes + camera)"""
class Scene():

    def __init__(self):
        self.camera = Camera()
        self.shapes = [] # empty list of shapes

    def add_shape(self, shape):
        self.shapes.append(shape)
        return self # in case this is called on a dummy scene which isn't saved



cube_100 = Shape3D([
    # bottom face
    Line3D(Vec3([0, 0, 200]), Vec3([100, 0, 200])),
    Line3D(Vec3([100, 0, 200]), Vec3([100, 0, 300])),
    Line3D(Vec3([100, 0, 300]), Vec3([0, 0, 300])),
    Line3D(Vec3([0, 0, 300]), Vec3([0, 0, 200])),
    # edges connecting bottom and top face
    Line3D(Vec3([0, 100, 200]), Vec3([0, 0, 200])),
    Line3D(Vec3([1, 100, 200]), Vec3([100, 0, 200])),
    Line3D(Vec3([1, 100, 300]), Vec3([100, 0, 300])),
    Line3D(Vec3([0, 100, 300]), Vec3([0, 0, 300])),
    # top face
    Line3D(Vec3([0, 100, 200]), Vec3([100, 100, 200])),
    Line3D(Vec3([100, 100, 200]), Vec3([100, 100, 300])),
    Line3D(Vec3([100, 100, 300]), Vec3([0, 100, 300])),
    Line3D(Vec3([0, 100, 300]), Vec3([0, 100, 200]))
])

cube_scene = Scene().add_shape(cube_100)
