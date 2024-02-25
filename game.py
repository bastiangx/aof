import SimpleGUICS2Pygame.simpleguics2pygame as sg
from random import uniform as ru
from user_input import *
from player import *
from config import *
from zombies import *
from levels import Level
from velocity import Velocity

player = Player()
kbd = Keyboard()
level = Level()
zomb_vel = Velocity()
zombies = []

num_zombies = level.get_num_zombies()
velocity_range = level.get_velocity_range(num_zombies)


def create_zombies(num_zombies, CANVAS_WIDTH):
    for _ in range(num_zombies):
        x = ru(50, CANVAS_WIDTH - 50)
        y = ru(200, 900) * -1
        velocity_range = level.get_velocity_range(num_zombies)
        zombie_velocity = get_zombie_velocity(velocity_range)()
        zombie = Zombie(x, y, zombie_velocity, health=100)
        zombies.append(zombie)


def get_zombie_velocity(velocity_range):
    if velocity_range == 'higher':
        return zomb_vel.higher
    elif velocity_range == 'regular':
        return zomb_vel.regular
    else:
        return zomb_vel.lower


if level.current_level <= level.final_level:
    create_zombies(num_zombies, CANVAS_WIDTH)


def remove_zombies():
    zombies_to_remove = []

    for zombie in zombies:
        if zombie.y >= CANVAS_HEIGHT:
            zombies_to_remove.append(zombie)
            print('Zombie staged for removal')

    for zombie in zombies_to_remove:
        zombies.remove(zombie)
        print('Zombie removed')


def draw(canvas):
    for zombie in zombies:
        zombie.draw(canvas)
        zombie.update()

    remove_zombies()
    player.draw(canvas)
    player.update(kbd)


for zombie in zombies:
    print(f'Zombie velocity: {zombie.velocity}')

print(f'Velocity range: {velocity_range}')
print(f'Number of zombies: {num_zombies}')
print(f'Level {level.current_level}:')

frame = sg.create_frame('farmPy', CANVAS_WIDTH, CANVAS_HEIGHT, 0)
frame.set_draw_handler(draw)
frame.set_keydown_handler(kbd.keydown)
frame.set_keyup_handler(kbd.keyup)

frame.start()
