

from vector import Vec3, Vec2


class Line2D():

    def __init__(self, p1, p2):
        self.p1 = p1 # p1 and p2 are Vec2 objects, indicating the start and end points of the line
        self.p2 = p2


class Line3D():

    def __init__(self, p1, p2):
        self.p1 = p1 # p1 and p2 are Vec3 objects, indicating the start and end points of the line
        self.p2 = p2
    
    def m(self):
        """return a vector-gradient of the line. I.e., in the x = p + mt form, the m vector."""
        return self.p1.sub(self.p2) # difference between two points known to lie on line
    

class Shape3D():

    def __init__(self, edges):

        self.points = edges # list of Line3D objects


unit_cube = Shape3D([
    # bottom face
    Line3D(Vec3([0, 0, 2]), Vec3([1, 0, 2])),
    Line3D(Vec3([1, 0, 2]), Vec3([1, 0, 3])),
    Line3D(Vec3([1, 0, 3]), Vec3([0, 0, 3])),
    Line3D(Vec3([0, 0, 3]), Vec3([0, 0, 2])),
    # edges connecting bottom and top face
    Line3D(Vec3([0, 1, 2]), Vec3([0, 0, 2])),
    Line3D(Vec3([1, 1, 2]), Vec3([1, 0, 2])),
    Line3D(Vec3([1, 1, 3]), Vec3([1, 0, 3])),
    Line3D(Vec3([0, 1, 3]), Vec3([0, 0, 3])),
    # top face
    Line3D(Vec3([0, 1, 2]), Vec3([1, 1, 2])),
    Line3D(Vec3([1, 1, 2]), Vec3([1, 1, 3])),
    Line3D(Vec3([1, 1, 3]), Vec3([0, 1, 3])),
    Line3D(Vec3([0, 1, 3]), Vec3([0, 1, 2]))
])
