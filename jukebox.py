from assets import (
    MUSIC_2,
    MUSIC_3,
    MUSIC_4,
    SE_ZOMBIE_WASTED_1,
    SE_ZOMBIE_WASTED_2,
    SE_ZOMBIE_HIT_1,
    SE_ZOMBIE_HIT_2,
    SE_ZOMBIE_HIT_3,
    SE_GUNSHOT,
    SE_PLAYER_HIT,
    UI_CLICK,
    UI_BACK,
)

from config import VOLUME, APP_MUTED
from random import choice as rc


class Jukebox:
    """
    handles music playback

    -----------
    KNOWN ISSUE: music does not loop seamlessly
        Reason: simplegui api limitation. cannot track music length
    -----------
    """

    def __init__(self) -> None:
        self.music = None
        self.volume = VOLUME

        self.music2 = MUSIC_2
        self.music3 = MUSIC_3
        self.music4 = MUSIC_4

    def play(self):
        if self.music is not None:
            self.music.pause()

        if APP_MUTED:
            self.volume = 0

        self.music = rc([self.music2, self.music3, self.music4])
        self.music.set_volume(self.volume)
        self.music.play()


class UI:
    """
    handles UI sound effects

    -----------
    KNOWN ISSUE: rapid sound effect playback may cause sound to cut off
        Reason: simplegui api limitation. cannot play multiple sounds simultaneously
    -----------
    """

    def __init__(self) -> None:
        self.sound = None
        self.volume = VOLUME

        self.click = UI_CLICK
        self.back = UI_BACK

    def play(self):
        if APP_MUTED:
            self.volume = 0
            return

        else:
            self.sound = self.click
            self.sound.set_volume(self.volume)
            self.sound.play()

    def play_back(self):
        if APP_MUTED:
            self.volume = 0
            return

        else:
            self.sound = self.back
            self.sound.set_volume(self.volume)
            self.sound.play()


class SoundEffect:
    """
    handles entity sound effects

    -----------
    KNOWN ISSUE: rapid sound effect playback may cause sound to cut off
        Reason: simplegui api limitation. cannot play multiple sounds simultaneously
    -----------
    """

    def __init__(self) -> None:
        self.sound = None
        self.volume = VOLUME

        self.zombie_wasted_1 = SE_ZOMBIE_WASTED_1
        self.zombie_wasted_2 = SE_ZOMBIE_WASTED_2
        self.zombie_hit_1 = SE_ZOMBIE_HIT_1
        self.zombie_hit_2 = SE_ZOMBIE_HIT_2
        self.zombie_hit_3 = SE_ZOMBIE_HIT_3
        self.gunshot = SE_GUNSHOT
        self.player_hit = SE_PLAYER_HIT

    def play_zombie_wasted(self):
        if APP_MUTED:
            self.volume = 0
            return

        else:
            self.sound = rc([self.zombie_wasted_1, self.zombie_wasted_2])
            self.sound.set_volume(self.volume)
            self.sound.play()

    def play_zombie_hit(self):
        if APP_MUTED:
            self.volume = 0
            return

        else:
            self.sound = rc(
                [self.zombie_hit_1, self.zombie_hit_2, self.zombie_hit_3]
            )
            self.sound.set_volume(self.volume)
            self.sound.play()

    def play_player_hit(self):
        if APP_MUTED:
            self.volume = 0
            return

        else:
            self.sound = self.player_hit
            self.sound.set_volume(self.volume)
            self.sound.play()

    def play_gunshot(self):
        if APP_MUTED:
            self.volume = 0
            return

        else:
            self.sound = self.gunshot
            self.sound.set_volume(self.volume)
            self.sound.play()
