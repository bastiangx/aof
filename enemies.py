from assets import HUD_ZOMBIE_HP, ENEMY_SKULL, ENEMY_BEAST, ENEMY_REPTILE
from random import choice as rc


class Enemy:
    """
    Draws and update the zombie spritesheet
    """

    def __init__(self, x, y, velocity) -> None:
        self.image: object = rc([ENEMY_SKULL, ENEMY_BEAST, ENEMY_REPTILE])
        self.velocity = velocity

        self.x = x
        self.y = y
        self.width = 26
        self.height = 26
        self.margin = 10

        self.frame_height = self.image.get_height() // 4
        self.frame_duration = 22
        self.frame_index = 0
        self.frame_timer = 0

        self.gui: object = HUD_ZOMBIE_HP
        self.gui_width: int = self.gui.get_width()
        self.gui_height: int = self.gui.get_height()

        self.max_hp: int = 100
        self.hp: int = self.max_hp
        self.dead: bool = False

    def wasted(self) -> bool:
        return self.hp <= 0 or self.dead

    def take_damage(self, damage: int) -> None:
        self.hp -= damage

        if self.hp <= 0:
            self.hp = 0
            self.dead = True

    def get_hp(self) -> int:
        return self.hp

    def calculate_gui_position(self) -> tuple:
        return (
            self.x,
            self.y - (self.height // 2) - self.margin,
        )

    def draw(self, canvas):
        frame_center_y = (self.frame_index + 0.5) * self.frame_height
        frame_center = (self.image.get_width() // 2, frame_center_y)
        frame_size = (self.image.get_width(), self.frame_height)

        canvas.draw_image(
            self.image,
            frame_center,
            frame_size,
            (self.x, self.y),
            (self.width, self.height),
        )

        if self.hp != self.max_hp:
            canvas.draw_image(
                self.gui,
                (self.gui_width / 2, self.gui_height / 2),
                (self.gui_width, self.gui_height),
                self.calculate_gui_position(),
                (self.gui_width, self.gui_height),
            )

    def update(self):
        self.move_down()

        self.frame_timer += 1
        if self.frame_timer >= self.frame_duration:
            self.frame_timer = 0
            self.frame_index = (self.frame_index + 1) % 4

    def move_down(self):
        self.y += self.velocity

    def get_hitbox(self):
        return (self.x, self.y, self.width, self.height)

    def get_top_left(self):
        return (self.x - self.width / 2, self.y - self.height / 2)

    def reset(self) -> None:
        self.hp = self.max_hp
        self.dead = False
