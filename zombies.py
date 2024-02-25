import SimpleGUICS2Pygame.simpleguics2pygame as sg
from user_input import *
from config import *


class Zombie:
    def __init__(self, x, y, velocity, health=100):
        self.velocity = velocity
        self.x = x
        self.y = y
        self.health = health
        self.max_health = health
        self.image = sg.load_image(
            'https://img.itch.zone/aW1nLzE0Mzk3ODY5LnBuZw==/original/6J9fF%2F.png'
        )

    def draw(self, canvas):
        canvas.draw_image(
            self.image,
            (self.image.get_width() / 2, self.image.get_height() / 2),
            (self.image.get_width(), self.image.get_height()),
            (self.x, self.y),
            (80, 80),
        )

    def update(self):
        self.move_down()

    def move_down(self):
        self.y += self.velocity
