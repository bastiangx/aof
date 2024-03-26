from SimpleGUICS2Pygame.simpleguics2pygame import KEY_MAP as map
import sys


class Keyboard:
    """
    Handles all keyboard input
    """

    def __init__(self) -> None:
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.leader = False
        self.pause = False

        # dbg / quit app quick / remove later
        self.z = False

    def keydown(self, key: int) -> None:
        """
        Pressing down a key
        """
        if key == map['d'] or key == map['right']:
            self.right = True

        if key == map['a'] or key == map['left']:
            self.left = True

        if key == map['w'] or key == map['up']:
            self.up = True

        if key == map['s'] or key == map['down']:
            self.down = True

        if key == map['p']:
            self.pause = True

        if key == map['space']:
            self.leader = True

            # dbg / quit app quick / remove later
        if key == map['z']:
            self.z = True
            sys.exit()

    def keyup(self, key: int) -> None:
        """
        Releasing a key
        """
        if key == map['d'] or key == map['right']:
            self.right = False

        if key == map['a'] or key == map['left']:
            self.left = False

        if key == map['w'] or key == map['up']:
            self.up = False

        if key == map['s'] or key == map['down']:
            self.down = False

        if key == map['p']:
            self.pause = False

        if key == map['space']:
            self.leader = False
