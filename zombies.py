from assets import ZOMBIE_IMG
from user_input import *
from config import *


class Zombie:
    def __init__(self, x, y, velocity, health=100):
        self.velocity = velocity

        self.x = x
        self.y = y
        self.width = 50
        self.height = 50

        self.health = health
        self.max_health = health

        self.image = ZOMBIE_IMG

    def draw(self, canvas):
        canvas.draw_image(
            self.image,
            (self.image.get_width() / 2, self.image.get_height() / 2),
            (self.image.get_width(), self.image.get_height()),
            (self.x, self.y),
            (self.width, self.height),
        )

    def draw_test_hitbox(self, top_left, canvas):
        canvas.draw_polygon(
            [
                (top_left[0], top_left[1]),
                (top_left[0] + self.width, top_left[1]),
                (
                    top_left[0] + self.width,
                    top_left[1] + self.height,
                ),
                (top_left[0], top_left[1] + self.height),
            ],
            2,
            'Red',
        )

    def update(self):
        self.move_down()

    def move_down(self):
        self.y += self.velocity

    def get_hitbox(self):
        return (self.x, self.y, self.width, self.height)

    def get_top_left(self):
        return (self.x - self.width / 2, self.y - self.height / 2)

    def get_health(self):
        return self.health

    def get_max_health(self):
        return self.max_health

    def lose_health(self, damage):
        self.health -= damage

    def has_hit_floor(self):
        return self.y - 50 >= CANVAS_HEIGHT
