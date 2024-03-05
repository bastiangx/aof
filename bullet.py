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
        self.damage = 10

    def draw(self, canvas):
        canvas.draw_image(
            self.image,
            (self.image.get_width() / 2, self.image.get_height() / 2),
            (self.image.get_width(), self.image.get_height()),
            (self.x, self.y),
            (10, 10),
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

    # check if bullet has collided with zombie / +3 creates a useful hitbox
    def is_collided(self, zombies):
        return (
            self.x + 3 > zombies.x
            and self.x - 3 < zombies.x
            and self.y + 3 > zombies.y
            and self.y - 3 < zombies.y
        )
