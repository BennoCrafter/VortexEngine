from ve.ve import GameEngine, GameObject

# Initialize the game engine
game = GameEngine(screen_width=800, screen_height=600, screen_name="Demo Game", screen_color="yellow")

# Create game objects
player = GameObject(x=100, y=100, width=50, height=50, color="blue")
enemy = GameObject(x=500, y=300, width=50, height=50, color="red")
test = GameObject(200, 200, 60, 60, "pink")

# Add game objects to the game engine
game.add_object(player)
game.add_object(enemy)
game.add_object(test)
# move game object
test.move(5, 0)
# delete game object
# game.delete_object(enemy)


def update(deltatime):
    if game.key_pressed("d"):
        player.move(dx=player.speed * deltatime, dy=0)
    elif game.key_pressed("a"):
        player.move(dx=-player.speed * deltatime)
    elif game.key_pressed("s"):
        player.move(0, player.speed * deltatime)
    elif game.key_pressed("w"):
        player.move(0, -player.speed + deltatime)

    if player.collided(enemy):
        print("yey")


game.update = update

# Start the game loop
game.start()