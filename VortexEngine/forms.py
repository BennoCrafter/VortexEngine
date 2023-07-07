from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class Forms:
    def __init__(self):
        pass

    def draw_sprite(self, x, y, width, height, shape):
        self.shape = shape
        if hasattr(self, shape):
            func = getattr(self, shape)
            func(x, y, width, height)
        else:
            raise ValueError("Invalid Shape!")

    def rect(self, x, y, width, height):
        glColor3f(0.0, 0.0, 1.0)
        glBegin(GL_QUADS)
        glVertex2f(x, y)
        glVertex2f(x + width, y)
        glVertex2f(x + width, y + height)
        glVertex2f(x, y + height)
        glEnd()
