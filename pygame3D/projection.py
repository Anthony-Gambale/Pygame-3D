

from pygame3D.scene import Line2D, Line3D, Shape2D
from pygame3D.vector import Vec2


def project_scene(scn):
    """ Take in a scene, and project all shapes onto the camera. Return a list of 2D shape objects. """
    for shape in scn.shapes:
        yield project_shape(shape, scn.camera) # return an iterator object that lists all shapes


def project_shape(shp, cam):
    """ take in Shape3D shp and Camera cam, and project the shape onto the screen. """
    Tlines = [] # transformed lines

    for line in shp.lines:
        Tlines.append(project_line(line, cam))
    
    return Shape2D(Tlines)


def project_line(lin, cam):
    """ take in Line3D lin and Camera cam, and project it to 2D. """
    Tp1 = project_point(lin.p1, cam) # transform each point
    Tp2 = project_point(lin.p2, cam)
    # return a dead line if either point is behind the camera
    # ideally these would be filtered out instead of drawn. fix later
    if cam.isBehind(lin.p1) or cam.isBehind(lin.p2):
        return None
    return Line2D(Tp1, Tp2) # 2D line of Vec2D points


def project_point(p, cam):
    """ project 3D point onto 3D camera plane, then transform intersection point from 3D camera plane into 2D pixel coordinate space. """
    
    s = cam.s
    n = cam.n
    c = cam.c
    bx = cam.bx # basis vectors of screen plane
    by = cam.by
    
    m = Line3D(p, c).gradient()

    # t is the parameter in the parametric equation of the line.
    # this specific t value represents the point in space where the line and screen plane cross
    div = n.dot(m)
    if div == 0: div = 0.001
    t = (n.dot(s.sub(p))) / div

    # extract the point x from t
    x = p.add(m.scale(t)) # since x = p + t*m

    # find the relative distance from the centre to x
    d = s.sub(x)

    # turn the 3D relative distance into a 2D vector, pointing from the centre of the screen
    x = d.project(bx)
    y = d.project(by)

    # return the x and y coords
    return Vec2([x, y])
