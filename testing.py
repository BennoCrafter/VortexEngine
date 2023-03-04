from ve.ve import GameEngine, GameObject

# Initialize the game engine
game = GameEngine(800, 600)

# Create game objects
player = GameObject(100, 100, 50, 50, 2)
enemy = GameObject(500, 300, 50, 50, 3)
test = GameObject(200, 200, 60, 60, 4)

# Add game objects to the game engine
game.add_object(player)
game.add_object(enemy)
game.add_object(test)
test.move(5, 0)

# Start the game loop
game.start()
