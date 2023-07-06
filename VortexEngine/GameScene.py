from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from forms import Forms


class GameScene:
    def __init__(self, screen_width=None, screen_height=None, screen_name="Default", screen_color=None):
        self.width = screen_width
        self.height = screen_height
        self.screen_name = screen_name
        self.forms = Forms()

    def refresh2d(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def process_normal_keys(self, key, x, y):
        if key == b'\x1b':  # Escape key
            close_window()

    def close_window(self):
        glutDestroyWindow(window)
        sys.exit(0)

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        self.refresh2d(self.width, self.height)

        self.forms.rect(10, 10, 200, 100)
        # todo add all objects
        glutSwapBuffers()


if __name__ == "__main__":
    # Initialization
    example = GameScene(400, 400)
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(example.width, example.height)
    glutInitWindowPosition(0, 0)
    window = glutCreateWindow(example.screen_name)
    glutDisplayFunc(example.draw)
    glutIdleFunc(example.draw)
    glutKeyboardFunc(example.process_normal_keys)  # Register keyboard callback
    glutMainLoop()