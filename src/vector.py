
# Vector arithmetic module

class Vec():

    def __init__(self, e):
        """Initialise Vec self"""
        # list of elements
        self.elems = e

    def __str__(self):
        """behaviour for Vec when print() is called on it"""
        return str(self.elems) # print elements

    def add(self, other):
        """add Vec self to Vec other, elementwise"""
        if len(self.elems) == len(other.elems):
            self.elems = [self.elems[i] + other.elems[i] for i in range(len(self.elems))]
            return self # just in case the user wants to use the sum in some other way
        else:
            return "error: in vector addition, vectors did not have the same number of elements"
    
    def scale(self, k):
        """scale Vec self by Num k"""
        self.elems = [e * k for e in self.elems]
        return self # just in case the user wants to use the vector in some other way

    def dot(self, other):
        """return the dot product of Vec self and Vec other"""
        if len(self.elems) == len(other.elems):
            return sum([self.elems[i] * other.elems[i] for i in range(len(self.elems))])
        else:
            return "error: in vector dot product, vectors did not have the same number of elements"


class Vec2(Vec):
    
    def __init__(self, e):
        [x, y] = e # make sure e is 2D
        self.elems = [x, y]


class Vec3(Vec):
    
    def __init__(self, e):
        [x, y, z] = e # make sure e is 3D
        self.elems = [x, y, z]
