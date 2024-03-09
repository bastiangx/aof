import SimpleGUICS2Pygame.simpleguics2pygame as sg
from config import CANVAS_WIDTH, CANVAS_HEIGHT
from user_input import Keyboard
from collision import Collision
from score import Score

from factory import ZombieFactory, WaveFactory, FactoryHandler
from bullet import Bullet
from player import Player
from mouse import Mouse
from shoot import Shoot

# entities initialization
player = Player()

# input initialization
kbd = Keyboard()
mouse = Mouse()

# logic initialization
collision = Collision()
shoot = Shoot()
score = Score()

# instance lists initialization
bullets_list = []
zombies_list = []

# timers initialization
ZombieFactory.spawn_cooldown = ZombieFactory().gen_cooldown()
WaveFactory.spawn_cooldown = WaveFactory().gen_cooldown()

# score initialization
last_zombie_killed = 0


def draw(canvas):
    global zombies_list, bullets_list, last_zombie_killed

    # shooting 
    shoot.fire_rate() # update fire rate
    if mouse.clicked and shoot.fire_rate() == 0:
        bullet = Bullet(x=player.x, y=player.y)
        bullets_list.append(bullet)
        shoot.start(bullet, [player.x, player.y], mouse.get_position())

        mouse.clicked = False # reset click

    # draw loops
    for zombie in zombies_list:
        zombie.draw(canvas)
        zombie.update()

    for bullet in bullets_list:
        bullet.draw(canvas)
        bullet.update()

    # player 
    player.draw(canvas)
    player.update(kbd)

    # spawn zombies and waves
    FactoryHandler.spawn_zombies(score.get_current_score(), zombies_list)

    # collision call
    collision.start(player, zombies_list, bullets_list)

    # score update from bullet collision
    zombies_killed = collision.zombies_killed
    zombies_killed_delta = zombies_killed - last_zombie_killed

    # if zombies are killed, increment score by the number of zombies killed
    if zombies_killed_delta > 0:
        score.increment_score(zombies_killed_delta)
        last_zombie_killed = zombies_killed
        print(f'Score: {score.get_current_score()}')


# sg initialization
frame = sg.create_frame('farmPy', CANVAS_WIDTH, CANVAS_HEIGHT, 0)
frame.set_draw_handler(draw)

frame.set_keydown_handler(kbd.keydown)
frame.set_keyup_handler(kbd.keyup)
frame.set_mouseclick_handler(mouse.click_handler)

frame.start()
