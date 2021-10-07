
"""
Read 3D models in point form from a text file, and convert them into models to be included
in the scene.
"""

from pygame3D.vector import *
from pygame3D.scene import *

def read_model(source):

    # read data from the source
    with open(source, 'r') as f: data = filter(
        lambda line : line[0:2] != "\n" and line[0:2] != "//"
        , f.readlines()
    )
    f.close()

    # convert the data into a shape3D object
    edge_list = []

    for line in data:
        numbers = [int(x) for x in line.split(',')]
        start_point = Vec3(numbers[0:3])
        end_point = Vec3(numbers[3:6])
        line = Line3D(start_point, end_point)
        edge_list.append(line)
    
    return Shape3D(edge_list)
