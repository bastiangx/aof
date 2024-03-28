from assets import GAME_BULLET
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

        self.image = GAME_BULLET
        self.width = 22
        self.height = 22

        self.frame_height = self.image.get_height() // 2
        self.frame_duration = 10
        self.frame_index = 0
        self.frame_timer = 0

    def draw(self, canvas: object) -> None:
        # current frame's center
        frame_center_y = (self.frame_index + 0.5) * self.frame_height
        frame_center = (self.image.get_width() // 2, frame_center_y) 
        frame_size = (self.image.get_width(), self.frame_height) # final frame size

        canvas.draw_image(
            self.image,
            frame_center,
            frame_size,
            (self.x, self.y),
            (self.width, self.height),
        )

    # moves bullet
    def update(self) -> None:
        self.x += self.velocity.x
        self.y += self.velocity.y

        self.frame_timer += 1
        if self.frame_timer >= self.frame_duration:
            self.frame_timer = 0
            self.frame_index = (self.frame_index + 1) % 2

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
