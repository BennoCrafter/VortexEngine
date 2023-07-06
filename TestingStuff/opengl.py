from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys


class Basic:
    def __init__(self):
        self.x = 10
        self.y = 10
        self.speed = 1
        self.width, self.height = 400, 400  # window size

    def draw_rect(self, x, y, width, height):
        glBegin(GL_QUADS)
        glVertex2f(x, y)
        glVertex2f(x + width, y)
        glVertex2f(x + width, y + height)
        glVertex2f(x, y + height)
        glEnd()

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        self.refresh2d(self.width, self.height)

        glColor3f(0.0, 0.0, 1.0)
        self.draw_rect(self.x, self.y, 200, 100)
        self.x += self.speed
        self.y += self.speed
        if self.x >= self.width or self.x <= 0:
            self.speed *= -1
        glutSwapBuffers()

    def refresh2d(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def close_window(self):
        glutDestroyWindow(window)
        sys.exit(0)

    def process_normal_keys(self, key, x, y):
        if key == b'\x1b':  # Escape key
            close_window()


basic = Basic()
# Initialization
glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(basic.width, basic.height)
glutInitWindowPosition(0, 0)
window = glutCreateWindow(b"noobtuts.com")
glutDisplayFunc(basic.draw)
glutIdleFunc(basic.draw)
glutKeyboardFunc(basic.process_normal_keys)  # Register keyboard callback
glutMainLoop()
