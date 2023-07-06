from VortexEngine.VortexEngine import *

# Initialize the game engine
game = GameScene(screen_width=800, screen_height=600, screen_name="Demo Game", screen_color="yellow")
speed = 400
coins = 0
# Create game objects
player_rect = Collider(x=100, y=100, width=50, height=50)
player = GameObject(x=101, y=100, width=50, height=50, color="blue", collider_obj=player_rect)

enemy = GameObject(x=500, y=300, width=50, height=50, color="red", collider_obj=Collider(x=500, y=300, width=50, height=50))

coin_rect = Collider(200, 200, 60, 60)
coin = GameObject(200, 200, 60, 60, "pink", collider_obj=coin_rect)

# Add game objects to the game engine
game.add_object(player)
game.add_object(enemy)
game.add_object(coin)
# move game object
# coin.move(5, 0)


def update(delta_time):
    global coins
    if game.key_pressed("d"):
        player.move(dx=speed * delta_time, dy=0)
    elif game.key_pressed("a"):
        player.move(dx=-speed * delta_time)
    elif game.key_pressed("s"):
        player.move(0, speed * delta_time)
    elif game.key_pressed("w"):
        player.move(0, -speed * delta_time)

    if player.collided(coin):
        # delete game object
        game.delete_object(coin)
        coins += 1
    # if player.collided(enemy):
    #     exit(0)
    print(coins)


game.update = update

# Start the game loop
game.start()
