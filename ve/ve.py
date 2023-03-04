import sdl2.ext
# Load the script as a module


class GameEngine:
    def __init__(self, screen_width, screen_height, name):
        sdl2.ext.init()
        self.objects = []
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.current_key = int
        self.window = sdl2.ext.Window(name, size=(screen_width, screen_height))
        self.window.show()

    def add_object(self, obj):
        self.objects.append(obj)

    def delete_object(self, obj):
        self.objects.remove(obj)

    def key_pressed(self, key):
        if key == self.current_key:
            return True

    def render(self):
        sdl2.SDL_SetRenderDrawColor(self.renderer.sdlrenderer, 255, 255, 255, 255)
        sdl2.SDL_RenderClear(self.renderer.sdlrenderer)
        sdl2.SDL_SetRenderDrawColor(self.renderer.sdlrenderer, 0, 0, 255, 255)

        for obj in self.objects:
            rect = sdl2.rect.SDL_Rect(int(obj.x), int(obj.y), int(obj.width), int(obj.height))
            sdl2.SDL_RenderFillRect(self.renderer.sdlrenderer, rect)

        sdl2.SDL_RenderPresent(self.renderer.sdlrenderer)

    def close_window(self):
        sdl2.ext.quit()

    def start(self):
        # Create the renderer
        self.renderer = sdl2.ext.Renderer(self.window)

        # Start the game loop
        self.game_loop()

    def game_loop(self):
        # Get the current time

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
            self.update()
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


class GameObject:
    def __init__(self, x, y, width, height, color):
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)
        self.color = color

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
