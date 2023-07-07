from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
from VortexEngine.forms import Forms


class GameScene:
    def __init__(self, screen_width=None, screen_height=None, screen_name="Default"):
        self.width = screen_width
        self.height = screen_height
        self.screen_name = screen_name
        self.objects = []
        self.update_scheduled = False
        self.current_key = ""
        self.forms = Forms()

        # Init OpenGL
        glutInit()
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
        glutInitWindowSize(self.width, self.height)
        glutInitWindowPosition(0, 0)
        self.window = glutCreateWindow(self.screen_name)
        glutDisplayFunc(self.draw)
        glutIdleFunc(self.scene_update)
        glutKeyboardFunc(self.process_normal_keys)
        glutKeyboardUpFunc(self.process_normal_keys_up)
        self.refresh2d(self.width, self.height)

    def refresh2d(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def process_normal_keys(self, key, x, y):
        self.current_key = key
        if key == b'\x1b':  # Escape key
            self.close_window()

    def process_normal_keys_up(self, key, x, y):
        self.current_key = ""

    def close_window(self):
        glutDestroyWindow(self.window)
        sys.exit(0)

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        self.refresh2d(self.width, self.height)

        # Draw custom sprites
        for obj in self.objects:
            self.forms.draw_sprite(obj.x, obj.y, obj.width, obj.height, obj.shape)

        glutSwapBuffers()

    def add_object(self, obj):
        self.objects.append(obj)

    def scene_update(self):
        self.update()
        glutPostRedisplay()

    def get_current_key(self):
        return self.current_key

    def start_game_loop(self):
        glutMainLoop()
