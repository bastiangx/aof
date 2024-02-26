from assets import BULLET_IMG
from vector import Vector
from mouse import Mouse
from config import *


class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.image = BULLET_IMG

        self.velocity = Vector(1, 1)
        self.velocity.normalize()
        self.velocity_modifier = 3
        self.velocity *= self.velocity_modifier

        self.damage = 10

    def draw(self, canvas):
        canvas.draw_image(
            self.image,
            (self.image.get_width() / 2, self.image.get_height() / 2),
            (self.image.get_width(), self.image.get_height()),
            (self.x, self.y),
            (10, 10),
        )

    def update(self):
        clicked_x = Mouse.clicked_x
        clicked_y = Mouse.clicked_y
        self.move_towards(clicked_x, clicked_y)

    def move_towards(self, x, y):
        target_vector = Vector(  # from current position to target
            x - self.x, y - self.y
        )
        target_vector.normalize()

        self.velocity.x = target_vector.x   # point towards target
        self.velocity.y = target_vector.y

        self.x += self.velocity.x * self.velocity.length()
        self.y += self.velocity.y * self.velocity.length()

    def off_screen(self):
        return (
            self.y <= 0
            or self.y >= CANVAS_HEIGHT
            or self.x <= 0
            or self.x >= CANVAS_WIDTH
        )

    def is_collided(self, zombie):
        return (
            self.x + 5 > zombie.x
            and self.x - 5 < zombie.x
            and self.y + 5 > zombie.y
            and self.y - 5 < zombie.y
        )
