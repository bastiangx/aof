from SimpleGUICS2Pygame.simpleguics2pygame import (
    _load_local_image as get_image,
    _load_local_sound as get_sound,
)

from os.path import join as pj
from os import getcwd


class Pathfinder:
    """
    Defines the defualt paths for various local assets and loads them into cache

    -----------
    Attributes
    -----------
        *_PATH: default paths for every asset type

    --------
    !! Important Note
    --------
        all paths as strings, with the current working directory appended to them
        (cwd: current working directory)
        (pj: os.path.join)

        !! (pj and cwd are used in tandem to get full path always, regardless of OS)
            (cwd might not work on Windows, but pj will always work)

    --------
    Methods
    --------
        load_*: loads the asset into cache via simplegui API
    """

    SPRITE_PATH: str = getcwd() + '/assets/sprite/'
    LOGO_PATH: str = getcwd() + '/assets/logo/'
    HUD_PATH: str = getcwd() + '/assets/hud/'
    BG_PATH: str = getcwd() + '/assets/background/'
    BUTTON_PATH: str = getcwd() + '/assets/button/'

    AUDIO_PATH: str = getcwd() + '/assets/audio/'
    MUSIC_PATH: str = getcwd() + '/assets/music/'

    @staticmethod
    def load_image(name: str) -> object:
        return get_image(pj(Pathfinder.SPRITE_PATH, name))

    @staticmethod
    def load_button(name: str) -> object:
        return get_image(pj(Pathfinder.BUTTON_PATH, name))

    @staticmethod
    def load_logo(name: str) -> object:
        return get_image(pj(Pathfinder.LOGO_PATH, name))

    @staticmethod
    def load_hud(name: str) -> object:
        return get_image(pj(Pathfinder.HUD_PATH, name))

    @staticmethod
    def load_bg(name: str) -> object:
        return get_image(pj(Pathfinder.BG_PATH, name))

    @staticmethod
    def load_sound(name: str) -> object:
        return get_sound(pj(Pathfinder.AUDIO_PATH, name))

    @staticmethod
    def load_music(name: str) -> object:
        return get_sound(pj(Pathfinder.MUSIC_PATH, name))


### cache assets
# splash screen
SPLASH_LOGO = Pathfinder.load_logo('splash-rhu.png')
SPLASH_LOVE = Pathfinder.load_image('splash-love.png')

# title screen
TITLE_LOGO = Pathfinder.load_logo('title-logo.png')
TITLE_USAGE = Pathfinder.load_image('title-usage.png')
TITLE_PROMPT = Pathfinder.load_image('title-prompt.png')

# main Menu
MM_LOGO = Pathfinder.load_logo('mm-logo.png')

# about screen
ABOUT_GITHUB = Pathfinder.load_image('about-github.png')
ABOUT_SOURCE = Pathfinder.load_image('about-source.png')

# Guide screen
GUIDE_BANNER = Pathfinder.load_image('guide-sprite.png')
GUIDE_BG = Pathfinder.load_bg('guide-bg.png')
# guide timer numnbers
GUIDE_NUMBERS = [
    Pathfinder.load_image('number1.png'),
    Pathfinder.load_image('number2.png'),
    Pathfinder.load_image('number3.png'),
    Pathfinder.load_image('number4.png'),
    Pathfinder.load_image('number5.png'),
    Pathfinder.load_image('number6.png'),
    Pathfinder.load_image('number7.png'),
    Pathfinder.load_image('number8.png'),
]

### gameplay
# enemies
ENEMY_SKULL = Pathfinder.load_image('enemy-skull.png')
ENEMY_BEAST = Pathfinder.load_image('enemy-beast.png')
ENEMY_REPTILE = Pathfinder.load_image('enemy-reptile.png')

# player
PLAYER_IDLE = Pathfinder.load_image('player-idle.png')
PLAYER_DOWN = Pathfinder.load_image('player-walk-down.png')
PLAYER_UP = Pathfinder.load_image('player-walk-up.png')
PLAYER_LEFT = Pathfinder.load_image('player-walk-left.png')
PLAYER_RIGHT = Pathfinder.load_image('player-walk-right.png')

# bullet
GAME_BULLET = Pathfinder.load_image('game-bullet.png')

# gameplay HUD
HUD_PLAYER_FULL = Pathfinder.load_hud('hud-player-full.png')
HUD_PLAYER_HALF = Pathfinder.load_hud('hud-player-half.png')
HUD_ZOMBIE_HP = Pathfinder.load_hud('hud-zombie-hp.png')
HUD_PLAYER_75 = Pathfinder.load_hud('hud-player-75.png')
HUD_PLAYER_25 = Pathfinder.load_hud('hud-player-25.png')

# pause menu
PAUSE_BANNER = Pathfinder.load_image('pause-banner.png')

# game over / wasted
WASTED_BANNER = Pathfinder.load_image('wasted-banner.png')
WASTED_BG = Pathfinder.load_bg('wasted-bg.png')

# buttons
BTN_ABOUT = Pathfinder.load_button('btn-about.png')
BTN_PLAY = Pathfinder.load_button('btn-play.png')
BTN_EXIT = Pathfinder.load_button('btn-exit.png')
BTN_BACK = Pathfinder.load_button('btn-back.png')
BTN_MM = Pathfinder.load_button('btn-mm.png')

# background
M_BG = Pathfinder.load_bg('m-bg.png')
M_BG_DARK = Pathfinder.load_bg('m-bg-dark.png')

# music
MUSIC_2 = Pathfinder.load_music('music-2.ogg')
MUSIC_3 = Pathfinder.load_music('music-3.mp3')
MUSIC_4 = Pathfinder.load_music('music-4.mp3')

# entity sound effects
SE_ZOMBIE_WASTED_1 = Pathfinder.load_sound('zombie-dead-1.wav')
SE_ZOMBIE_WASTED_2 = Pathfinder.load_sound('zombie-dead-2.wav')
SE_ZOMBIE_HIT_1 = Pathfinder.load_sound('zombie-hit-1.wav')
SE_ZOMBIE_HIT_2 = Pathfinder.load_sound('zombie-hit-2.wav')
SE_ZOMBIE_HIT_3 = Pathfinder.load_sound('zombie-hit-3.wav')
SE_GUNSHOT = Pathfinder.load_sound('gunshot.wav')
SE_PLAYER_HIT = Pathfinder.load_sound('bite.mp3')

# ui sound effects
UI_CLICK = Pathfinder.load_sound('ui.ogg')
UI_BACK = Pathfinder.load_sound('ui-back.ogg')
