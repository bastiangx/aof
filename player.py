from config import CANVAS_WIDTH, CANVAS_HEIGHT
from assets import PLAYER_IMG
from vector import Vector
from user_input import *


class Player:
    def __init__(self, health=100):
        self.velocity = Vector(1, 1)
        self.velocity.normalize()
        self.velocity_modifier = 8
        # self.has_hit_wall = False

        self.image = PLAYER_IMG

        self.x = CANVAS_WIDTH / 2
        self.y = CANVAS_HEIGHT / 1.1
        self.width = 80
        self.height = 80

        self.health = health
        self.max_health = 100

        self.floor_damage = 2

    def draw(self, canvas):
        canvas.draw_image(
            self.image,
            (self.image.get_width() / 2, self.image.get_height() / 2),
            (self.image.get_width(), self.image.get_height()),
            (self.x, self.y),
            (self.width, self.height),
        )

    def update(self, keyboard):
        self.move(keyboard)
        self.floor_damage_applied = False

    def move(self, keyboard):
        direction = Vector(0, 0)

        if keyboard.up:
            direction.y -= 1
        if keyboard.down:
            direction.y += 1
        if keyboard.left:
            direction.x -= 1
        if keyboard.right:
            direction.x += 1

        # self.has_hit_wall = False

        self.x += self.velocity.x * direction.x * self.velocity_modifier
        self.y += self.velocity.y * direction.y * self.velocity_modifier

        # boundary check, if hit wall, bouce
        # if self.x < 0 or self.x > CANVAS_WIDTH:
        #     self.velocity.x *= -0.8
        #     self.has_hit_wall = True
        #
        # if self.y < 0 or self.y > CANVAS_HEIGHT:
        #     self.velocity.y *= -0.8
        #     self.has_hit_wall = True

        self.x = max(min(self.x, CANVAS_WIDTH - 40), 40)
        self.y = max(min(self.y, CANVAS_HEIGHT - 40), 40)

    def get_hitbox(self):
        return (self.x, self.y, self.width, self.height)

    def get_top_left(self):
        return (self.x - self.width / 2, self.y - self.height / 2)

    def drw_test_hitbox(self, canvas):
        sprite_top_left = (self.x - self.width / 2, self.y - self.height / 2)
        canvas.draw_polygon(
            [
                (sprite_top_left[0], sprite_top_left[1]),
                (sprite_top_left[0] + self.width, sprite_top_left[1]),
                (
                    sprite_top_left[0] + self.width,
                    sprite_top_left[1] + self.height,
                ),
                (sprite_top_left[0], sprite_top_left[1] + self.height),
            ],
            2,
            'blue',
        )

    def get_health(self):
        return self.health

    def get_max_health(self):
        return self.max_health

    def lose_floor_health(self):
        if 0 < self.health <= self.max_health:
            self.health -= self.floor_damage

    def gain_health(self, heal):
        self.health += heal

    def is_dead(self):
        return self.health <= 0
