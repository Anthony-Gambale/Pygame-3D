

from scene import Scene, Line2D, Line3D, Shape2D
from vector import Vec2


def project_scene(scn):
    """ Take in a scene, and project all shapes onto the camera. Return a list of 2D shape
    objects. """
    for shape in scn.shapes:
        yield project_shape(shape, scn.camera) # return an iterator object that lists all shapes


def project_shape(shp, cam):
    """ take in Shape3D shp and Camera cam, and project the shape onto the screen.
    1. project each line in the shape
    2. make sure all new lines are grouped together in a Shape2D object """
    Tlines = [] # transformed lines

    for line in shp.lines:
        Tlines.append(project_line(line, cam))
    
    return Shape2D(Tlines)
        


def project_line(lin, cam):
    """ take in Line3D lin and Camera cam, and project it to 2D.
    1. project the first point
    2. project the second point
    3. output the two points together in a Line2D object """
    Tp1 = project_point(lin.p1, cam) # transform each point
    Tp2 = project_point(lin.p2, cam)

    return Line2D(Tp1, Tp2) # 2D line of Vec2D points


def project_point(p, cam):
    """ take in a Vec3 point p, and project it to 2D with respect to the input Camera cam.
    1. find the line that crosses through the point p, and the camera location c
    2. define the plane of the camera screen
    3. find where the line and plane cross, and call this point x
    4. find the relative distance from the centre of the screen s to the point x, and use
    that relative distance to draw the point on the user's screen.
    5. project the relative distance onto the basis vectors of the screen. these magnitudes
    are the necessary pixel coords."""
    
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
    x = (bx.dot(d)) / (bx.dot(bx))
    y = (by.dot(d)) / (by.dot(by))

    # return the x and y coords
    return Vec2([x, y])
