from assets import BTN_PLAY, BTN_EXIT, BTN_MM, PAUSE_BANNER
from jukebox import UI
from config import CANVAS_WIDTH

click_sound = UI()

class PauseMenu:
    def __init__(self) -> None:
        self.banner = PAUSE_BANNER
        self.play_btn = BTN_PLAY
        self.exit_btn = BTN_EXIT
        self.mm_btn = BTN_MM

        self.buttons_width = self.play_btn.get_width()
        self.buttons_height = self.play_btn.get_height()

        self.banner_width = self.banner.get_width()
        self.banner_height = self.banner.get_height()

        self.margin_top = 260
        self.margin_middle = 160
        self.margin_button = 33

        self.base_x = CANVAS_WIDTH // 2
        self.base_y = self.margin_top

    def calculate_banner_position(self) -> tuple:
        return (
            self.base_x,
            self.base_y,
        )

    def calculate_button_positions(self) -> tuple:
        # x position
        base_x = self.base_x - self.buttons_width / 2

        play_btn_x = base_x
        exit_btn_x = base_x
        mm_btn_x = base_x

        # y position
        base_y = self.margin_top + self.margin_top

        play_btn_y = base_y
        mm_btn_y = play_btn_y + self.buttons_height + self.margin_button
        exit_btn_y = mm_btn_y + self.buttons_height + self.margin_button

        # return the top-left corner of each button
        return (
            play_btn_x,
            play_btn_y,
            exit_btn_x,
            exit_btn_y,
            mm_btn_x,
            mm_btn_y,
        )

    def render(self, canvas: object) -> None:
        # banner position
        (
            banner_x,
            banner_y,
        ) = self.calculate_banner_position()

        # buttons position
        (
            play_btn_x,
            play_btn_y,
            exit_btn_x,
            exit_btn_y,
            mm_btn_x,
            mm_btn_y,
        ) = self.calculate_button_positions()

        # darken overlay
        canvas.draw_polygon(
            [
                (0, 0),
                (CANVAS_WIDTH, 0),
                (CANVAS_WIDTH, 800),
                (0, 800),
            ],
            1,
            'Black',
            'rgba(0, 0, 0, 0.7)',
        )
        # banner image
        canvas.draw_image(
            self.banner,
            (self.banner_width // 2, self.banner_height // 2),
            (self.banner_width, self.banner_height),
            (banner_x, banner_y),
            (self.banner_width, self.banner_height),
        )

        # play button
        canvas.draw_image(
            self.play_btn,
            (self.buttons_width // 2, self.buttons_height // 2),
            (self.buttons_width, self.buttons_height),
            (
                play_btn_x + self.buttons_width // 2,
                play_btn_y + self.buttons_height // 2,
            ),
            (self.buttons_width, self.buttons_height),
        )

        # main menu button
        canvas.draw_image(
            self.mm_btn,
            (self.buttons_width // 2, self.buttons_height // 2),
            (self.buttons_width, self.buttons_height),
            (
                mm_btn_x + self.buttons_width // 2,
                mm_btn_y + self.buttons_height // 2,
            ),
            (self.buttons_width, self.buttons_height),
        )

        # exit button
        canvas.draw_image(
            self.exit_btn,
            (self.buttons_width // 2, self.buttons_height // 2),
            (self.buttons_width, self.buttons_height),
            (
                exit_btn_x + self.buttons_width // 2,
                exit_btn_y + self.buttons_height // 2,
            ),
            (self.buttons_width, self.buttons_height),
        )

    def click(self, position: tuple) -> str:
        x, y = position
        # hitbox check around the buttons
        (
            play_btn_x,
            play_btn_y,
            exit_btn_x,
            exit_btn_y,
            mm_btn_x,
            mm_btn_y,
        ) = self.calculate_button_positions()

        # Play button
        if (
            play_btn_x < x < play_btn_x + self.buttons_width
            and play_btn_y < y < play_btn_y + self.buttons_height
        ):
            click_sound.play()
            return 'play'

        # Main menu button
        if (
            mm_btn_x < x < mm_btn_x + self.buttons_width
            and mm_btn_y < y < mm_btn_y + self.buttons_height
        ):
            click_sound.play_back()
            return 'main_menu'

        # Exit button
        elif (
            exit_btn_x < x < exit_btn_x + self.buttons_width
            and exit_btn_y < y < exit_btn_y + self.buttons_height
        ):
            return 'exit'

        else:
            return None

    def handler(self, mouse: object) -> str:
        action = None

        if mouse.clicked:
            action = self.click(mouse.get_position())
            mouse.clicked = False

        return action
