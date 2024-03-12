from assets import BULLET_IMG
from vector import Vector

class Bullet:
    """
    Draws Bullet, updates its position
    """

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.velocity = Vector(1, 1)
        self.velocity_modifier = 8
        self.velocity.normalize()

        self.image = BULLET_IMG
        self.width = 20
        self.height = 20

    def draw(self, canvas: object) -> None:
        canvas.draw_image(
            self.image,
            (self.image.get_width() / 2, self.image.get_height() / 2),
            (self.image.get_width(), self.image.get_height()),
            (self.x, self.y),
            (self.width, self.height),
        )

    # moves bullet
    def update(self) -> None:
        self.x += self.velocity.x
        self.y += self.velocity.y

    def get_hitbox(self) -> tuple:
        return (self.x, self.y, self.width, self.height)

    def get_top_left(self) -> tuple:
        """
        Returns the top left corner of the bullet as a tuple of (x, y)
        Reason: origin of the bullet is at the center, but we need to check for collision with the top left corner

        Returns:
            tuple: (x, y) of the top left corner of the bullet
        """
        return (self.x - self.width / 2, self.y - self.height / 2)
