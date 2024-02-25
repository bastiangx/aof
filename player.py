from config import *
from user_input import *
import SimpleGUICS2Pygame.simpleguics2pygame as sg


class Player:
    def __init__(self, health=100):
        self.velocity = 8
        self.x = CANVAS_WIDTH / 2
        self.y = CANVAS_HEIGHT / 1.1
        self.image = sg.load_image(
            'https://img.itch.zone/aW1nLzE0Mzk3ODY5LnBuZw==/original/6J9fF%2F.png'
        )
        self.health = health
        self.max_health = health
        

    def draw(self, canvas):
        canvas.draw_image(
            self.image,
            (self.image.get_width() / 2, self.image.get_height() / 2),
            (self.image.get_width(), self.image.get_height()),
            (self.x, self.y),
            (80, 80),
        )

    def update(self, keyboard):
        self.move_right(keyboard)
        self.move_left(keyboard)
        self.move_up(keyboard)
        self.move_down(keyboard)

    def move_right(self, keyboard):
        if keyboard.right and self.x < CANVAS_WIDTH - 50:
            self.x += self.velocity

    def move_left(self, keyboard):
        if keyboard.left and self.x - 50 > 0:
            self.x -= self.velocity

    def move_up(self, keyboard):
        if keyboard.up and self.y - 50 > 0:
            self.y -= self.velocity

    def move_down(self, keyboard):
        if keyboard.down and self.y + 50 < CANVAS_HEIGHT:
            self.y += self.velocity
