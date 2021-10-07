
"""
Read 3D models in point form from a text file, and convert them into models to be included
in the scene.
"""

import pygame3D.scene

def read_model(source):

    # read data from the source
    with open(source, 'r') as f: data = f.readlines()
    f.close()

    # convert the data into a shape3D object

    # add the shape3D object to the scene

    return None
