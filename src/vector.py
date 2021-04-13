
# Linear algebra arithmetic module
from math import sqrt


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
            return Vec([self.elems[i] + other.elems[i] for i in range(len(self.elems))]) # return a new vector without changing self
        else:
            return "error: in vector addition, vectors did not have the same number of elements"


    def sub(self, other):
        """add Vec self to Vec other, elementwise"""
        if len(self.elems) == len(other.elems):
            return Vec([self.elems[i] - other.elems[i] for i in range(len(self.elems))]) # return a new vector without changing self
        else:
            return "error: in vector addition, vectors did not have the same number of elements"


    def scale(self, k):
        """scale Vec self by Num k"""
        return Vec([e * k for e in self.elems]) # return a new vector, and leave self unchanged


    def dot(self, other):
        """return the dot product of Vec self and Vec other"""
        if len(self.elems) == len(other.elems):
            return sum([self.elems[i] * other.elems[i] for i in range(len(self.elems))])
        else:
            return "error: in vector dot product, vectors did not have the same number of elements"


    def transform(self, matrix):
        """transform self by a matrix. matrix must have enough columns to fit Vec self, and it must be square so that it maps Vec self back into the same space."""
        if not matrix.row_num == matrix.col_num and matrix.col_num == len(self.elems):
            return "error: matrix in transformation must be square, and it must have enough columns to fit the vector"
        
        output_elems = []

        for row in matrix.rows:
            output_elems.append(self.dot(row))
        
        return Vec(output_elems) # return output without changing the current vector


    def cross_product_3D(self, other):
        """return the cross product of self and other (both vectors of the same dimension)"""
        [a, b, c] = self.elems
        [d, e, f] = other.elems

        x = b*f - c*e
        y = c*d - a*f
        z = a*e - b*d

        return Vec3([x, y, z])



    def magnitude(self):
        return sqrt(sum([e*e for e in self.elems]))


class Matrix():

    def __init__(self, vec_list):

        self.rows = vec_list # list of vectors, where each vector represents a row. this way rows can be iterated over
    
    def row_num(self):
        return len(self.rows)

    def col_num(self):
        return len(self.rows[0].elems)

    def shape(self):
        return (self.row_num, self.col_num)


class Vec2(Vec):
    
    def __init__(self, e):
        [x, y] = e # make sure e is 2D
        self.elems = [x, y]


class Vec3(Vec):
    
    def __init__(self, e):
        [x, y, z] = e # make sure e is 3D
        self.elems = [x, y, z]


# unit vectors for testing
i = Vec3([1, 0, 0])
j = Vec3([0, 1, 0])
k = Vec3([1, 0, 0])
