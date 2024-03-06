import SimpleGUICS2Pygame.simpleguics2pygame as sg
from random import uniform as ru
from user_input import *
from zombies import Zombie
from player import Player
from levels import Level
from config import *

# new imports
from mouse import Mouse
from bullet import Bullet
from shoot import Shoot

# end of new imports

player = Player()
level = Level()
kbd = Keyboard()
zombies_list = []

# new instances
bullet = Bullet(x=player.x, y=player.y)
shoot = Shoot()
mouse = Mouse()

# new lists
bullets_list = []
bullets_to_remove_list = []
# end of new instances and lists


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


def floor_is_hit():
    for zombie in zombies_list:
        if zombie.has_hit_floor():
            player.lose_floor_health()


def remove_zombies():
    zombies_to_remove = [
        zombie for zombie in zombies_list if zombie.has_hit_floor()
    ]
    for zombie in zombies_to_remove:
        zombies_list.remove(zombie)


# new implementation
# remove bullets that are off screen
def remove_bullets():
    bullets_to_remove = [
        bullet for bullet in bullets_list if bullet.off_screen()
    ]
    for bullet in bullets_to_remove:
        bullets_list.remove(bullet)


# next level implementation
def check_next_level():
    if len(zombies_list) == 0:
        level.next_level()
        num_zombies = level.get_num_zombies()
        create_zombies(num_zombies, CANVAS_WIDTH)


def draw(canvas):
    # new implementation
    # mouse stuff
    if mouse.clicked and shoot.fire_rate_iterator() == 0:
        bullet = Bullet(x=player.x, y=player.y)
        bullets_list.append(bullet)

        shoot.start_shooting(
            bullet, [player.x, player.y], mouse.get_position()
        )

        mouse.clicked = False

    # draw bullets
    for bullet in bullets_list:
        bullet.draw(canvas)
        bullet.draw_test_hitbox(bullet.get_top_left(), canvas)
        bullet.update()

    for zombie in zombies_list:
        zombie.draw(canvas)
        zombie.draw_test_hitbox(zombie.get_top_left(), canvas)
        zombie.update()

    shoot.fire_rate_iterator()
    remove_bullets()
    floor_is_hit()
    remove_zombies()
    player.draw(canvas)
    player.drw_test_hitbox(canvas)
    player.update(kbd)
    check_next_level()


frame = sg.create_frame('farmPy', CANVAS_WIDTH, CANVAS_HEIGHT, 0)
frame.set_draw_handler(draw)

frame.set_keydown_handler(kbd.keydown)
frame.set_keyup_handler(kbd.keyup)
frame.set_mouseclick_handler(mouse.click_handler)

frame.start()
