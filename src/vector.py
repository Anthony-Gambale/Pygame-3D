
# Linear algebra arithmetic module


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
        if not (len(matrix) == len(matrix[0]) and len(matrix) == len(self.elems)):
            return "error: matrix in transformation must be square, and it must have enough columns to fit the vector"
        
        output_elems = []

        for row in matrix.rows:
            output_elems.append(self.dot(row))
        
        return Vec(output_elems) # return output without changing the current vector


class Matrix():

    def __init__(self, vec_list):

        self.rows = vec_list # list of vectors, where each vector represents a row. this way rows can be iterated over


class Vec2(Vec):
    
    def __init__(self, e):
        [x, y] = e # make sure e is 2D
        self.elems = [x, y]


class Vec3(Vec):
    
    def __init__(self, e):
        [x, y, z] = e # make sure e is 3D
        self.elems = [x, y, z]
