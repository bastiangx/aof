from SimpleGUICS2Pygame.simpleguics2pygame import (
    _load_local_image as get_image,
    _load_local_sound as get_sound,
)
from os.path import join as pj
from os import getcwd


class Pathfinder:

    """
    Defines the paths for various assets and loads them
    """

    IMAGE_PATH = getcwd() + '/assets/images/'
    BUTTON_PATH = getcwd() + '/assets/buttons/'
    ANIMATION_PATH = getcwd() + 'assets/animations/'
    AUDIO_PATH = getcwd() + 'assets/audio/'
    FONT_PATH = getcwd() + 'assets/fonts/'

    @staticmethod
    def load_image(name: str) -> object:
        return get_image(pj(Pathfinder.IMAGE_PATH, name))

    @staticmethod
    def load_button(name: str) -> object:
        return get_image(pj(Pathfinder.BUTTON_PATH, name))

    @staticmethod
    def load_sound(name: str) -> object:
        return pj(Pathfinder.AUDIO_PATH, name)


# Sprites
PLAYER_IMG = Pathfinder.load_image('player.png')
ZOMBIE_IMG = Pathfinder.load_image('enemy-1.png')
BULLET_IMG = Pathfinder.load_image('bullet.png')

# Buttons
PLAY_BTN = Pathfinder.load_button('PlayBtn.png')
OPTIONS_BTN = Pathfinder.load_button('OptBtn.png')
EXIT_BTN = Pathfinder.load_button('ExitBtn.png')
