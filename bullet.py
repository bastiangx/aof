from assets import BULLET_IMG
from vector import Vector
from config import *

# draws bullets, updates their position, and checks for collisions
class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = Vector(1, 1)
        self.velocity_modifier = 8
        self.velocity.normalize()

        self.image = BULLET_IMG
        self.width = 20
        self.height = 20

        self.damage = 10

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
                (top_left[0] + self.width, top_left[1] + self.height),
                (top_left[0], top_left[1] + self.height),
            ],
            1,
            'orange',
        )

    # moves bullet
    def update(self):
        self.x += self.velocity.x
        self.y += self.velocity.y

    # detect bullet if off screen
    def off_screen(self):
        return (
            self.y <= 0
            or self.y >= CANVAS_HEIGHT
            or self.x <= 0
            or self.x >= CANVAS_WIDTH
        )

    def get_hitbox(self):
        return (self.x, self.y, self.width, self.height)

    def get_top_left(self):
        return (self.x - self.width / 2, self.y - self.height / 2)
