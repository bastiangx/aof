from SimpleGUICS2Pygame.simpleguics2pygame import KEY_MAP as map


class Keyboard:
    """
    Handles all keyboard input

    -----------
    Known Issues
    -----------
        * No support for Escape key
        * Random and non registered keys impact the game

        SimpleGUICS2Pygame does not support all keys -> no escape key
        unmaintained library -> any keys can affect the runtime -> no fix

    """

    def __init__(self) -> None:
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.pause = False

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
