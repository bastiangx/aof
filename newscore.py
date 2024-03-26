# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 13:03:47 2024

@author: palak
"""

import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
from assets import BACKGROUND_IMG, BARN_IMG

# Constants for window size
WIDTH = 800
HEIGHT = 600

class Game:
    def __init__(self):
        self.background = BACKGROUND_IMG
        self.barn = BARN_IMG
        self.barn_x = WIDTH / 2
        self.barn_y = HEIGHT - 50  # Adjust the barn's position to be at the bottom of the screen
        self.barn_width = 160  # Adjust width and height for a better display
        self.barn_height = 120

    def draw(self, canvas):
        # Draw background image first
        canvas.draw_image(
            self.background,
            (self.background.get_width() / 2, self.background.get_height() / 2),
            (self.background.get_width(), self.background.get_height()),
            (WIDTH / 2, HEIGHT / 2),
            (WIDTH, HEIGHT)
        )

        # Draw barn image on top of the background
        canvas.draw_image(
            self.barn,
            (self.barn.get_width() / 2, self.barn.get_height() / 2),
            (self.barn.get_width(), self.barn.get_height()),
            (self.barn_x, self.barn_y),
            (self.barn_width, self.barn_height)
        )

# Create a frame
frame = simplegui.create_frame("Game", WIDTH, HEIGHT)

# Create a game instance
game = Game()

# Set the draw handler
frame.set_draw_handler(game.draw)

# Start the frame
frame.start()
