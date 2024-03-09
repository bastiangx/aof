from config import CANVAS_WIDTH, CANVAS_HEIGHT
from assets import PLAYER_IMG
from vector import Vector


class Player:
    """
    draws, updates and handles player movement
    """

    def __init__(self) -> None:
        self.velocity = Vector(1, 1)
        self.velocity.normalize()
        self.velocity_modifier = 8

        self.image = PLAYER_IMG

        self.x = CANVAS_WIDTH / 2
        self.y = CANVAS_HEIGHT / 1.1
        self.width = 80
        self.height = 80

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
        # defines the vectorial direction

        if keyboard.up:
            direction.y -= 1
        if keyboard.down:
            direction.y += 1
        if keyboard.left:
            direction.x -= 1
        if keyboard.right:
            direction.x += 1

        self.x += self.velocity.x * direction.x * self.velocity_modifier
        self.y += self.velocity.y * direction.y * self.velocity_modifier

        self.x = max(min(self.x, CANVAS_WIDTH - 40), 40)
        self.y = max(min(self.y, CANVAS_HEIGHT - 40), 40)

    def get_hitbox(self):
        return (self.x, self.y, self.width, self.height)

    def get_top_left(self):
        return (self.x - self.width / 2, self.y - self.height / 2)
