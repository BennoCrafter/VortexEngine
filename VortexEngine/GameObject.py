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
    def __init__(self, x, y, width, height, color, speed=int):
        self.x = x
        self.y = y
        self.width = int(width)
        self.height = int(height)
        self.speed = speed  # pixel per second
        if color in color_dict:
            self.color = color_dict[color]

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def collided(self, other):
        # Check if the two game objects intersect
        return (self.x < other.x + other.width and
                self.x + self.width > other.x and
                self.y < other.y + other.height and
                self.y + self.height > other.y)