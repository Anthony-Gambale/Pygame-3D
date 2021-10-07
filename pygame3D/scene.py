

from camera import Camera
import projection
import pygame


"""Lines"""
class Line():
    def __init__(self, p1, p2):
        self.p1 = p1 # p1 and p2 are either Vec2 or Vec3 objects, indicating the start and end points of the line
        self.p2 = p2

class Line2D(Line):
    def gradient(self):
        """return constant gradient of the line."""
        return (self.p1.sub(self.p2)).magnitude() # does not modify self.p1 or self.p2

    def draw(self, window, ww, wh):
        """take pygame window as input, and draw self onto it as a white line"""
        [x1, y1] = self.p1.elems # split vectors into raw coords
        [x2, y2] = self.p2.elems

        # calibrate such that 0,0 will be at the centre of the screen
        # using ww and wh (window width and window height)
        x1 = ww/2 + x1 # I want positive x to go right (no change)
        x2 = ww/2 + x2
        y1 = wh/2 - y1 # I want positive y to go up (flip pygame's definition)
        y2 = wh/2 - y2

        # draw the line
        pygame.draw.line(window, (255, 255, 255), (x1,y1), (x2,y2), 2)

class Line3D(Line):
    def gradient(self):
        """return a vector-gradient of the line. I.e., in the x = p + mt form, the m vector."""
        return self.p1.sub(self.p2) # difference between two points known to lie on line


"""Shapes"""
class Shape():
    def __init__(self, edges):
        self.lines = edges # list of line2D or line3D objects

class Shape2D(Shape):
    def draw(self, window):
        """take pygame window as input, and draw self onto it as a collection of line edges"""
        for edge in self.lines:
            edge.draw(window)

class Shape3D(Shape):
    pass


"""Scene (shapes + camera)"""
class Scene():

    def __init__(self, width, height, title="Pygame 3D Demo", initial_shapes=[]):
        self.camera = Camera()
        self.shapes = initial_shapes # list of shapes in the scene
        self.width = width
        self.height = height
        self.pygame_window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Pygame 3D Demo")

    def add_shape(self, shape):
        self.shapes.append(shape)
        return self # in case this is called on a dummy scene which isn't saved

    def refresh(self):
        # clear the previous frame
        self.pygame_window.fill((0, 0, 0))
        # draw all objects in scene
        for projected_shape in projection.project_scene(self):
            for projected_line in projected_shape.lines:
                projected_line.draw(self.pygame_window, self.width, self.height)