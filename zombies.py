from assets import ZOMBIE_IMG


class Zombie:
    """
    Draws and update the zombie
    """

    def __init__(self, x, y, velocity) -> None:
        self.velocity = velocity

        self.x = x
        self.y = y
        self.width = 50
        self.height = 50

        self.image = ZOMBIE_IMG

    def draw(self, canvas):
        canvas.draw_image(
            self.image,
            (self.image.get_width() / 2, self.image.get_height() / 2),
            (self.image.get_width(), self.image.get_height()),
            (self.x, self.y),
            (self.width, self.height),
        )

    def update(self):
        self.move_down()

    def move_down(self):
        self.y += self.velocity

    def get_hitbox(self):
        return (self.x, self.y, self.width, self.height)

    def get_top_left(self):
        return (self.x - self.width / 2, self.y - self.height / 2)
