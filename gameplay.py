"""
Main gameplay logic class
Handles game rendering and all interactions
"""
# logic/factories imports
from factory import ZombieFactory, WaveFactory, FactoryHandler
from collision import Collision

import sys

# objects/entities imports
from pause_menu import PauseMenu
from bullet import Bullet
from player import Player
from shoot import Shoot
from score import Score

# player initialization
player = Player()

# logic system initialization
pause_menu = PauseMenu()
collision = Collision()
shoot = Shoot()
score = Score()

# list instance initialization
bullets_list = []
zombies_list = []

# score incrementer initialization
last_zombie_killed = 0

# pause toggle variable
pause_pressed = False

# timers initialization
ZombieFactory.spawn_cooldown = ZombieFactory().gen_cooldown()
WaveFactory.spawn_cooldown = WaveFactory().gen_cooldown()


class Gameplay:
    @staticmethod
    def reset():
        """
        on new game, reset all values
        """
        global zombies_list, bullets_list, last_zombie_killed, pause_pressed

        zombies_list.clear()
        bullets_list.clear()
        score.current_score = 0
        score.high_score =0

    @staticmethod
    def render(canvas: object, kbd: object, mouse: object) -> None:
        """
        draw and update all gameplay entities
        """
        global zombies_list, bullets_list, last_zombie_killed, pause_pressed

        # draw loops (zombie.py, bullet.py)
        for zombie in zombies_list:
            zombie.draw(canvas)
            if not pause_pressed:
                zombie.update()

        for bullet in bullets_list:
            bullet.draw(canvas)
            if not pause_pressed:
                bullet.update()

        # player update (player.py)
        player.draw(canvas)
        if not pause_pressed:
            player.update(kbd)

        # spawn zombies and waves (factory.py)
        if not pause_pressed:
            FactoryHandler.spawn_zombies(
                score.get_current_score(), zombies_list
            )

        # collision call
        collision.start(player, zombies_list, bullets_list)

        # shooting system (shoot.py)
        if not pause_pressed:
            shoot.fire_rate()   # reset cooldown

        if mouse.clicked and shoot.fire_rate() == 0:
            if not pause_pressed:
                bullet = Bullet(x=player.x, y=player.y)
                bullets_list.append(bullet)

                shoot.start(bullet, [player.x, player.y], mouse.get_position())

                mouse.clicked = False   # reset click

        # score update from bullet collision
        zombies_killed = collision.zombies_killed
        zombies_killed_delta = zombies_killed - last_zombie_killed

        # score rendering
        score.render(canvas)
        # score system, if zombies are killed by bullets
        if zombies_killed_delta > 0:
            score.increment_score(zombies_killed_delta)
            last_zombie_killed = zombies_killed
            print(f'Score: {score.get_current_score()}')

            # pause menu toggle
        if kbd.pause and not pause_pressed:
            # toggle pause, press again to unpause
            print('pause toggled')
            pause_pressed = True

        # pause menu rendering
        if pause_pressed:
            pause_menu.render(canvas)
            action = pause_menu.handler(mouse)

            if action == 'play':
                pause_pressed = False
                print('play')

            elif action == 'options':
                print('options')

            elif action == 'exit':
                print('exit')
                sys.exit()

            else:
                pass

            mouse.clicked = False   # reset click
