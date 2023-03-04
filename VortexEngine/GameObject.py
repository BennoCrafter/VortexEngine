from VortexEngine.Collider import Collider
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


class GameObject:
    def __init__(self, x, y, width, height, color, speed=int, collider_obj=None):
        self.x = x
        self.y = y
        self.width = int(width)
        self.height = int(height)
        self.speed = speed  # pixel per second
        self.collider_obj = collider_obj
        if color in color_dict:
            self.color = color_dict[color]

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
        if self.collider_obj is not None:
            self.collider_obj.x = self.x
            self.collider_obj.y = self.y

    def collided(self, other):
        # check if object has a collider
        if self in scenes[0].objects and other in scenes[0].objects:
            if self.collider_obj is not None:
                if other.collider_obj is not None:
                    # Check if the two game objects intersect
                    return (self.collider_obj.x < other.collider_obj.x + other.collider_obj.width and
                            self.collider_obj.x + self.collider_obj.width > other.collider_obj.x and
                            self.collider_obj.y < other.collider_obj.y + other.collider_obj.height and
                            self.collider_obj.y + self.collider_obj.height > other.collider_obj.y)
                else:
                    print("exception error: object 2 has no collider")
            else:
                print("exception error: object 1 has no collider")
