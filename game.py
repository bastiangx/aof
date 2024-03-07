import SimpleGUICS2Pygame.simpleguics2pygame as sg
from random import uniform as ru
from collision import Collision
from user_input import *
from zombies import Zombie
from player import Player
from levels import Level
from config import *

from mouse import Mouse
from bullet import Bullet
from shoot import Shoot


player = Player()
level = Level()
kbd = Keyboard()
zombies_list = []

shoot = Shoot()
mouse = Mouse()

collision = Collision()

bullets_list = []
zombies_list = []


def get_zombie_velocity(velocity_range):
    if velocity_range == 'higher':
        return ru(1, 2.2)
    elif velocity_range == 'regular':
        return ru(1, 1.5)
    else:
        return ru(0.4, 0.8)


def create_zombies(num_zombies, CANVAS_WIDTH):
    num_zombies = level.get_num_zombies()
    velocity_range = level.get_velocity_range(num_zombies)

    for _ in range(num_zombies):
        x = ru(50, CANVAS_WIDTH - 50)
        y = ru(50, 60) * -1
        zombie_velocity = get_zombie_velocity(velocity_range)
        zombie = Zombie(x, y, zombie_velocity, health=100)
        zombies_list.append(zombie)


# next level implementation
def check_next_level():
    if len(zombies_list) == 0:
        level.next_level()
        num_zombies = level.get_num_zombies()
        create_zombies(num_zombies, CANVAS_WIDTH)


def draw(canvas):
    if mouse.clicked and shoot.fire_rate_iterator() == 0:
        bullet = Bullet(x=player.x, y=player.y)
        bullets_list.append(bullet)

        shoot.start_shooting(
            bullet, [player.x, player.y], mouse.get_position()
        )
        mouse.clicked = False

    for zombie in zombies_list:
        zombie.draw(canvas)
        zombie.draw_test_hitbox(zombie.get_top_left(), canvas)
        zombie.update()

    for bullet in bullets_list:
        bullet.draw(canvas)
        bullet.draw_test_hitbox(bullet.get_top_left(), canvas)
        bullet.update()

    player.draw(canvas)
    player.drw_test_hitbox(canvas)
    player.update(kbd)
    shoot.fire_rate_iterator()
    check_next_level()

    # collision stuff
    collision.check_player_to_zombie(player, zombies_list)
    collision.check_bullet_to_zombie(bullets_list, zombies_list)
    collision.check_bullet_to_wall(bullets_list)
    collision.check_zombie_to_base(zombies_list)
    collision.reset_cache(level.current_level)


frame = sg.create_frame('farmPy', CANVAS_WIDTH, CANVAS_HEIGHT, 0)
frame.set_draw_handler(draw)

frame.set_keydown_handler(kbd.keydown)
frame.set_keyup_handler(kbd.keyup)
frame.set_mouseclick_handler(mouse.click_handler)

frame.start()
