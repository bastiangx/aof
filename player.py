from config import CANVAS_WIDTH, CANVAS_HEIGHT
from assets import (
    PLAYER_IDLE,
    PLAYER_UP,
    PLAYER_DOWN,
    PLAYER_LEFT,
    PLAYER_RIGHT,
    HUD_PLAYER_FULL,
    HUD_PLAYER_HALF,
    HUD_PLAYER_75,
    HUD_PLAYER_25,
)
from vector import Vector


class Player:
    """
    draws, updates and handles player movement
    """

    def __init__(self, hp) -> None:
        self.velocity = Vector(1, 1).normalize()
        self.velocity_modifier = 4.2

        self.sprite = PLAYER_IDLE

        self.frame_height = self.sprite.get_height() // 4
        self.frame_duration = 22
        self.frame_index = 0
        self.frame_timer = 0

        self.gui_full = HUD_PLAYER_FULL
        self.gui_half = HUD_PLAYER_HALF
        self.gui_75 = HUD_PLAYER_75
        self.gui_25 = HUD_PLAYER_25

        # dimensions are uniform
        self.gui_width: int = self.gui_full.get_width()
        self.gui_height: int = self.gui_full.get_height()
        self.margin = 5

        self.max_hp: int = 100
        self.hp: int = hp
        self.dead: bool = False

        self.width = 34
        self.height = 34

        self.x = CANVAS_WIDTH / 2
        self.y = self.height * 6.5

    def wasted(self) -> bool:
        return self.hp <= 0 or self.dead

    def take_damage(self, damage: int) -> None:
        self.hp -= damage

        if self.hp <= 0:
            self.dead = True

    def get_hp(self) -> int:
        return self.hp

    # bottom left corner of screen + padding
    def calculate_gui_position(self) -> tuple:
        return (
            (self.gui_width / 2) + self.margin,
            CANVAS_HEIGHT - (self.gui_height / 2) - self.margin,
        )

    # if not moving, return idle sprite
    def set_idle(self) -> object:
        self.sprite = PLAYER_IDLE

    def is_idle(self) -> bool:
        return self.velocity.x == 0 and self.velocity.y == 0

    def draw_idle(self, canvas: object) -> None:
        self.sprite = PLAYER_IDLE
        self.draw_sprite(canvas)

    def draw_up(self, canvas: object) -> None:
        self.sprite = PLAYER_UP
        self.draw_sprite(canvas)

    def draw_down(self, canvas: object) -> None:
        self.sprite = PLAYER_DOWN
        self.draw_sprite(canvas)

    def draw_left(self, canvas: object) -> None:
        self.sprite = PLAYER_LEFT
        self.draw_sprite(canvas)

    def draw_right(self, canvas: object) -> None:
        self.sprite = PLAYER_RIGHT
        self.draw_sprite(canvas)

    def draw_sprite(self, canvas: object) -> None:
        frame_center_y = (self.frame_index + 0.5) * self.frame_height
        frame_center = (self.sprite.get_width() // 2, frame_center_y)
        frame_size = (self.sprite.get_width(), self.frame_height)

        canvas.draw_image(
            self.sprite,
            frame_center,
            frame_size,
            (self.x, self.y),
            (self.width, self.height),
        )

    def draw_gui(self, canvas: object) -> None:
        gui_x, gui_y = self.calculate_gui_position()

        if not self.wasted():
            if self.hp == self.max_hp:
                canvas.draw_image(
                    self.gui_full,
                    (self.gui_width / 2, self.gui_height / 2),
                    (self.gui_width, self.gui_height),
                    (gui_x, gui_y),
                    (self.gui_width, self.gui_height),
                )

            elif self.hp >= 75:
                canvas.draw_image(
                    self.gui_75,
                    (self.gui_width / 2, self.gui_height / 2),
                    (self.gui_width, self.gui_height),
                    (gui_x, gui_y),
                    (self.gui_width, self.gui_height),
                )
            elif self.hp >= 50:
                canvas.draw_image(
                    self.gui_half,
                    (self.gui_width / 2, self.gui_height / 2),
                    (self.gui_width, self.gui_height),
                    (gui_x, gui_y),
                    (self.gui_width, self.gui_height),
                )
            elif self.hp >= 25:
                canvas.draw_image(
                    self.gui_25,
                    (self.gui_width / 2, self.gui_height / 2),
                    (self.gui_width, self.gui_height),
                    (gui_x, gui_y),
                    (self.gui_width, self.gui_height),
                )
            else:
                canvas.draw_image(
                    self.gui_25,
                    (self.gui_width / 2, self.gui_height / 2),
                    (self.gui_width, self.gui_height),
                    (gui_x, gui_y),
                    (self.gui_width, self.gui_height),
                )

    def update(self, keyboard: object, canvas) -> None:
        direction = Vector(0, 0)
        self.floor_damage_applied = False

        # set direction based on keyboard input
        if keyboard.up:
            direction.y -= 1
        if keyboard.down:
            direction.y += 1
        if keyboard.left:
            direction.x -= 1
        if keyboard.right:
            direction.x += 1

        # normalize diagonal movement
        if direction.x != 0 and direction.y != 0:
            direction.normalize()

        # diagonal animations + idle + normal
        if direction.y < 0:
            self.draw_up(canvas)
        elif direction.y > 0:
            self.draw_down(canvas)
        elif direction.x < 0:
            self.draw_left(canvas)
        elif direction.x > 0:
            self.draw_right(canvas)
        else:
            self.draw_idle(canvas)

        # frame counter
        self.frame_timer += 1
        if self.frame_timer >= self.frame_duration:
            self.frame_timer = 0
            self.frame_index = (self.frame_index + 1) % 4

        # speed initialization
        self.speed_x: float = (
            self.velocity.x * direction.x * self.velocity_modifier
        )
        self.speed_y: float = (
            self.velocity.y * direction.y * self.velocity_modifier
        )

        # movement
        self.x += self.speed_x
        self.y += self.speed_y

        # boundaries
        self.x: float = max(min(self.x, CANVAS_WIDTH - 65), 65)
        self.y: float = max(min(self.y, CANVAS_HEIGHT - 56), 150)

    def get_hitbox(self) -> tuple:
        return (self.x, self.y, self.width, self.height)

    def get_top_left(self) -> tuple:
        return (self.x - self.width / 2, self.y - self.height / 2)

    def reset(self) -> None:
        self.hp = self.max_hp
        self.dead = False
        self.x = CANVAS_WIDTH / 2
        self.y = CANVAS_HEIGHT / 1.1
        self.width = 80
        self.height = 80
