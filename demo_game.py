import VortexEngine.VortexEngine
from VortexEngine.GameScene import GameScene
from VortexEngine.GameObject import GameObject

game_scene = GameScene(screen_width=400, screen_height=400, screen_name="Cool Scene")

player = GameObject(x=10, y=10, width=200, height=100, shape="rect", color="blue")
game_scene.add_object(player)


def update():
    if game_scene.get_current_key() == b'w':
        player.y +=1
    if game_scene.get_current_key() == b's':
        player.y -=1
    if game_scene.get_current_key() == b'd':
        player.x +=1
    if game_scene.get_current_key() == b'a':
        player.x -=1


game_scene.update = update
game_scene.start_game_loop()
