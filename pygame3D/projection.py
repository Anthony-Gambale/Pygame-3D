

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
        Tlines.append(project_line(line, cam, shp.colour))
    
    return Shape2D(Tlines)


def project_line(lin, cam, colour):
    """ take in Line3D lin and Camera cam, and project it to 2D. """

    # copy the line
    l = lin.copy()

    # check if its behind the camera. if so, don't draw it
    if cam.isBehind(l.p1) and cam.isBehind(l.p2):
        return None
    
    # transform each point
    Tp1 = project_point(l.p1, cam)
    Tp2 = project_point(l.p2, cam)
    
    # check if points are behind screen. if so, change transformation
    if cam.isBehind(l.p1):
        Tp1 = get_coords(find_intersection(l.p1, l.p2, cam), cam)
        Tp1 = Tp2.add(Tp1.sub(Tp2).scale(-1))
        return Line2D(Tp1, Tp2, colour).extend(1) # 2D line of Vec2D points
    if cam.isBehind(l.p2):
        Tp2 = get_coords(find_intersection(l.p1, l.p2, cam), cam)
        Tp2 = Tp1.add(Tp2.sub(Tp1).scale(-1))
        return Line2D(Tp1, Tp2, colour).extend(2) # 2D line of Vec2D points

    # return a 2 dimensional line with the transformed points
    return Line2D(Tp1, Tp2, colour) # 2D line of Vec2D points


def find_intersection(front, back, cam):
    """draw a line that connects points p1 and p2. return the point on that line that intersects the virtual screen, if there is one."""
    m = Line3D(front, back).gradient() # gradient of the line
    denom = cam.n.dot(m)
    if denom == 0: denom = 0.001
    t = (cam.n.dot(cam.s.sub(front))) / denom
    x = front.add(m.scale(t)) # since x = p + t*m
    return x


def get_coords(p, cam):
    """take the coordinates of a 3D point that lies on the camera plane, and vector project it onto the basis unit vectors to get 2D
    screen coordinates"""
    d = cam.s.sub(p)
    x = d.project(cam.bx)
    y = d.project(cam.by)
    return Vec2([x, y])


def project_point(p, cam):
    """ project 3D point onto 3D camera plane, then transform intersection point from 3D camera plane into 2D pixel coordinate space. """
    # find the intersection
    x = find_intersection(p, cam.c, cam)
    # turn the 3D relative distance into a 2D vector, pointing from the centre of the screen
    return get_coords(x, cam)
