from ve.ve import GameEngine, GameObject

# Initialize the game engine
game = GameEngine(800, 600, "Demo Game")

# Create game objects
player = GameObject(100, 100, 50, 50, 2)
enemy = GameObject(500, 300, 50, 50, 3)
test = GameObject(200, 200, 60, 60, 4)

# Add game objects to the game engine
game.add_object(player)
game.add_object(enemy)
game.add_object(test)
# move game object
test.move(5, 0)
# delete game object
game.delete_object(player)


def update():
    if game.key_pressed("d"):
        enemy.move(1)
    elif game.key_pressed("a"):
        enemy.move(-1)


game.update = update

# Start the game loop
game.start()