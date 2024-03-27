# logic/factories imports
from factory import ZombieFactory, WaveFactory, FactoryHandler
from jukebox import SoundEffect, UI
from collision import Collision

# objects/entities imports
from pause_menu import PauseMenu
from player import Player
from bullet import Bullet
from shoot import Shoot
from score import Score

sound = SoundEffect()
sound_click = UI()


class Gameplay:
    """
    Handles game rendering and all interactions
    """

    def __init__(self) -> None:
        self.reset()

    def reset(self):
        """
        On new game, reset all entities, flags, and variables.
        """
        self.player = Player(hp=100)
        self.pause_menu = PauseMenu()
        self.collision = Collision()
        self.shoot = Shoot()
        self.score = Score()

        # Lists for managing dynamic game entities
        self.bullets_list = []
        self.zombies_list = []

        # Additional game state variables
        self.last_zombie_killed = 0
        self.pause_pressed = False
        ZombieFactory.spawn_cooldown = ZombieFactory().gen_cooldown()
        WaveFactory.spawn_cooldown = WaveFactory().gen_cooldown()

    # handle puasing, wasted, and main menu actions for sm
    def handler(self, mouse: object, canvas) -> str:
        if self.player.wasted():
            self.reset()
            return 'wasted'

        if self.pause_pressed:
            sound_click.play_back()
            self.pause_menu.render(canvas)

            action = self.pause_menu.handler(mouse)
            if action == 'play':
                self.pause_pressed = False
                return 'play'

            elif action == 'main_menu':
                self.reset()
                return 'main_menu'

            elif action == 'exit':
                return 'exit'

        mouse.clicked = False
        return 'continue'

    def render(self, canvas: object, kbd: object, mouse: object) -> None:
        # draw loops (zombie.py, bullet.py)
        for zombie in self.zombies_list:
            zombie.draw(canvas)
            if not self.pause_pressed:
                zombie.update()

        for bullet in self.bullets_list:
            bullet.draw(canvas)
            if not self.pause_pressed:
                bullet.update()

        # player update (player.py)
        if not self.pause_pressed:
            self.player.update(kbd, canvas)
            # self.player.move(kbd)

        # self.player.draw_sprite(canvas)
        self.player.draw_gui(canvas)

        # spawn zombies and waves (factory.py)
        if not self.pause_pressed and not self.player.wasted():
            FactoryHandler.spawn_zombies(
                self.score.get_current_score(), self.zombies_list
            )

        # collision call
        self.collision.start(self.player, self.zombies_list, self.bullets_list)

        # shooting system (shoot.py)
        if not self.pause_pressed:
            self.shoot.fire_rate()   # reset cooldown

        if mouse.clicked and self.shoot.fire_rate() == 0:
            if not self.pause_pressed and not self.player.wasted():
                bullet = Bullet(x=self.player.x, y=self.player.y)
                self.bullets_list.append(bullet)

                self.shoot.start(
                    bullet,
                    [self.player.x, self.player.y],
                    mouse.get_position(),
                )

                sound.play_gunshot()
                mouse.update()
                mouse.clicked = False   # reset click

        # score update from bullet collision
        zombies_killed = self.collision.zombies_killed
        zombies_killed_delta = zombies_killed - self.last_zombie_killed

        # score rendering
        if not self.player.wasted():
            self.score.render(canvas)

        # score system, if zombies are killed by bullets
        if zombies_killed_delta > 0:
            self.score.increment_score(zombies_killed_delta)
            self.last_zombie_killed = zombies_killed

        # pause menu toggle
        if kbd.pause and not self.pause_pressed:
            # toggle pause, press again to unpause
            self.pause_pressed = True
