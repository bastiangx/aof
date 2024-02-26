import SimpleGUICS2Pygame.simpleguics2pygame as sg
from random import uniform as ru
from user_input import *
from zombies import Zombie
from player import Player
from levels import Level
from config import *

player = Player()
level = Level()
kbd = Keyboard()
zombies = []


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
        zombies.append(zombie)


def floor_is_hit():
    for zombie in zombies:
        if zombie.has_hit_floor():
            player.lose_floor_health()


def remove_zombies():
    zombies_to_remove = [
        zombie for zombie in zombies if zombie.has_hit_floor()
    ]

    for zombie in zombies_to_remove:
        zombies.remove(zombie)


# next level implementation
def check_next_level():
    if len(zombies) == 0:
        level.next_level()
        num_zombies = level.get_num_zombies()
        create_zombies(num_zombies, CANVAS_WIDTH)


def draw(canvas):
    for zombie in zombies:
        zombie.draw(canvas)
        zombie.update()

    floor_is_hit()
    remove_zombies()
    player.draw(canvas)
    player.update(kbd)
    check_next_level()


frame = sg.create_frame('farmPy', CANVAS_WIDTH, CANVAS_HEIGHT, 0)
frame.set_draw_handler(draw)

frame.set_keydown_handler(kbd.keydown)
frame.set_keyup_handler(kbd.keyup)

frame.start()
