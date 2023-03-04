import sdl2.ext
import time


class GameEngine:
    def __init__(self, screen_width, screen_height):
        sdl2.ext.init()
        self.objects = []
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.window = sdl2.ext.Window("Game Engine", size=(screen_width, screen_height))
        self.window.show()

    def add_object(self, obj):
        self.objects.append(obj)

    def update(self, dt):
        for obj in self.objects:
            # Update the position of the object
            obj.move(10*dt, 0)

    def render(self):
        sdl2.SDL_SetRenderDrawColor(self.renderer.sdlrenderer, 255, 255, 255, 255)
        sdl2.SDL_RenderClear(self.renderer.sdlrenderer)
        sdl2.SDL_SetRenderDrawColor(self.renderer.sdlrenderer, 0, 0, 255, 255)

        for obj in self.objects:
            rect = sdl2.rect.SDL_Rect(int(obj.x), int(obj.y), int(obj.width), int(obj.height))
            sdl2.SDL_RenderFillRect(self.renderer.sdlrenderer, rect)

        sdl2.SDL_RenderPresent(self.renderer.sdlrenderer)

        self.window.refresh()

    def close_window(self):
        sdl2.ext.quit()

    def start(self):
        # Create the renderer
        self.renderer = sdl2.ext.Renderer(self.window)

        # Start the game loop
        self.game_loop()

    def game_loop(self):
        # Get the current time
        current_time = time.time()

        running = True
        while running:
            events = sdl2.ext.get_events()  # Get events from queue
            for event in events:
                if event.type == sdl2.SDL_QUIT:  # If user closes window
                    running = False  # Stop the event loop
                    break
            self.update(time.time() - current_time)
            self.render()
        self.window.close()
        sdl2.ext.quit()

        # Draw the game objects
        # Cap the frame rate to 60 fps
        elapsed_time = time.time() - current_time
        if elapsed_time < 1/60:
            time.sleep((1/60) - elapsed_time)

        # Schedule the next frame
        sdl2.SDL_Delay(1)
        self.game_loop()


class GameObject:
    def __init__(self, x, y, width, height, color):
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)
        self.color = color
        self.velocity = (0, 0)

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
