import sdl2.ext
import time
from VortexEngine.GameEngine import scenes
color_dict = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "orange": (255, 165, 0),
    "purple": (128, 0, 128),
    "pink": (255, 192, 203),
    "black": (0, 0, 0),
    "white": (255, 255, 255)
}


class GameScene:
    def __init__(self, screen_width=None, screen_height=None, screen_name="Default", screen_color=None):
        scenes.append(self)
        sdl2.ext.init()
        self.objects = []
        self.screen_width = screen_width
        self.screen_height = screen_height
        if screen_color in color_dict:
            self.screen_color = color_dict[screen_color]
        self.current_key = None
        self.window = sdl2.ext.Window(screen_name, size=(screen_width, screen_height))

    def add_object(self, obj):
        self.objects.append(obj)

    def delete_object(self, obj):
        if obj in self.objects:
            if obj.collider_obj is not None:
                del obj.collider_obj
            self.objects.remove(obj)
            del obj

    def key_pressed(self, key):
        if key == self.current_key:
            return True

    def render(self):
        # background
        sdl2.SDL_SetRenderDrawColor(self.renderer.sdlrenderer, *self.screen_color, 255)
        sdl2.SDL_RenderClear(self.renderer.sdlrenderer)
        for obj in self.objects:
            # objects
            sdl2.SDL_SetRenderDrawColor(self.renderer.sdlrenderer, *obj.color, 255)
            rect = sdl2.rect.SDL_Rect(int(obj.x), int(obj.y), int(obj.width), int(obj.height))
            sdl2.SDL_RenderFillRect(self.renderer.sdlrenderer, rect)

        self.renderer.present()

    def start(self):
        # Create the renderer
        self.renderer = sdl2.ext.Renderer(self.window, flags=sdl2.SDL_RENDERER_ACCELERATED)
        self.window.show()
        # Start the game loop
        self.game_loop()

    def game_loop(self):
        # Get the current time
        last_time = time.monotonic()
        running = True
        while running:
            events = sdl2.ext.get_events()  # Get events from queue
            for event in events:
                if event.type == sdl2.SDL_QUIT:  # If user closes window
                    running = False  # Stop the event loop
                    break
                elif event.type == sdl2.SDL_KEYDOWN:  # If key is pressed
                    self.current_key = self.key_to_text(event.key.keysym.sym)
                elif event.type == sdl2.SDL_KEYUP:
                    self.current_key = None
            current_time = time.monotonic()
            delta_time = current_time - last_time
            last_time = current_time
            self.update(delta_time=delta_time)
            self.render()
        self.window.close()
        sdl2.ext.quit()

    def key_to_text(self, key):
        # Get the name of the key from its code
        key_name = sdl2.SDL_GetKeyName(key).decode("utf-8")

        # If the key name is a single character, return it as text
        if len(key_name) == 1:
            return key_name.lower()
        else:
            return "space"
