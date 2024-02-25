import SimpleGUICS2Pygame.simpleguics2pygame as sg
import sys


class Keyboard:
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.leader = False

    def keydown(self, key):
        if key == sg.KEY_MAP['d'] or key == sg.KEY_MAP['right']:
            self.right = True

        if key == sg.KEY_MAP['a'] or key == sg.KEY_MAP['left']:
            self.left = True

        if key == sg.KEY_MAP['w'] or key == sg.KEY_MAP['up']:
            self.up = True

        if key == sg.KEY_MAP['s'] or key == sg.KEY_MAP['down']:
            self.down = True

        if key == sg.KEY_MAP['space']:
            self.leader = True

            # dbg / quit app quick / remove later
        if key == sg.KEY_MAP['z']:
            sys.exit()

    def keyup(self, key):
        if key == sg.KEY_MAP['d'] or key == sg.KEY_MAP['right']:
            self.right = False

        if key == sg.KEY_MAP['a'] or key == sg.KEY_MAP['left']:
            self.left = False

        if key == sg.KEY_MAP['w'] or key == sg.KEY_MAP['up']:
            self.up = False

        if key == sg.KEY_MAP['s'] or key == sg.KEY_MAP['down']:
            self.down = False

        if key == sg.KEY_MAP['space']:
            self.leader = False
