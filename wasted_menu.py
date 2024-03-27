from assets import WASTED_BANNER, WASTED_BG, BTN_PLAY, BTN_EXIT, BTN_MM
from config import CANVAS_WIDTH, CANVAS_HEIGHT
from jukebox import UI

sound_click = UI()


class WastedMenu:
    """
    end/wasted menu rendering and interactions
    handler returns the action as a str
    click detects the mouse click on buttons and returns the action
    """

    def __init__(self) -> None:
        self.banner = WASTED_BANNER
        self.bg = WASTED_BG
        self.play_btn = BTN_PLAY
        self.exit_btn = BTN_EXIT
        self.mm_btn = BTN_MM

        self.banner_width = self.banner.get_width()
        self.banner_height = self.banner.get_height()

        self.buttons_width = self.play_btn.get_width()
        self.buttons_height = self.play_btn.get_height()

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
        base_x = CANVAS_WIDTH / 2

        play_btn_x = base_x
        exit_btn_x = base_x
        mm_btn_x = base_x

        base_y = self.margin_top * 2.15

        play_btn_y = base_y
        mm_btn_y = play_btn_y + self.buttons_height + self.margin_button
        exit_btn_y = mm_btn_y + self.buttons_height + self.margin_button

        return (
            play_btn_x,
            play_btn_y,
            exit_btn_x,
            exit_btn_y,
            mm_btn_x,
            mm_btn_y,
        )

    def render(self, canvas: object) -> None:
        (
            banner_x,
            banner_y,
        ) = self.calculate_banner_position()

        (
            play_btn_x,
            play_btn_y,
            exit_btn_x,
            exit_btn_y,
            mm_btn_x,
            mm_btn_y,
        ) = self.calculate_button_positions()

        # background
        canvas.draw_image(
            self.bg,
            (self.bg.get_width() / 2, self.bg.get_height() / 2),
            (self.bg.get_width(), self.bg.get_height()),
            (CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2),
            (CANVAS_WIDTH, CANVAS_HEIGHT),
        )

        # banner image
        canvas.draw_image(
            self.banner,
            (self.banner_width // 2, self.banner_height // 2),
            (self.banner_width, self.banner_height),
            (
                banner_x,
                banner_y,
            ),
            (self.banner_width, self.banner_height),
        )

        # buttons
        canvas.draw_image(
            self.play_btn,
            (self.buttons_width // 2, self.buttons_height // 2),
            (self.buttons_width, self.buttons_height),
            (
                play_btn_x,
                play_btn_y,
            ),
            (self.buttons_width, self.buttons_height),
        )

        canvas.draw_image(
            self.exit_btn,
            (self.buttons_width // 2, self.buttons_height // 2),
            (self.buttons_width, self.buttons_height),
            (
                exit_btn_x,
                exit_btn_y,
            ),
            (self.buttons_width, self.buttons_height),
        )

        canvas.draw_image(
            self.mm_btn,
            (self.buttons_width // 2, self.buttons_height // 2),
            (self.buttons_width, self.buttons_height),
            (
                mm_btn_x,
                mm_btn_y,
            ),
            (self.buttons_width, self.buttons_height),
        )

    def click(self, position: tuple) -> str:
        x, y = position

        (
            play_btn_x,
            play_btn_y,
            exit_btn_x,
            exit_btn_y,
            mm_btn_x,
            mm_btn_y,
        ) = self.calculate_button_positions()

        # play button
        if (
            x >= play_btn_x - self.buttons_width // 2
            and x <= play_btn_x + self.buttons_width // 2
            and y >= play_btn_y - self.buttons_height // 2
            and y <= play_btn_y + self.buttons_height // 2
        ):
            sound_click.play()
            return 'play'

        # mm button
        if (
            x >= mm_btn_x - self.buttons_width // 2
            and x <= mm_btn_x + self.buttons_width // 2
            and y >= mm_btn_y - self.buttons_height // 2
            and y <= mm_btn_y + self.buttons_height // 2
        ):
            sound_click.play_back()
            return 'mm'

        # exit button
        elif (
            x >= exit_btn_x - self.buttons_width // 2
            and x <= exit_btn_x + self.buttons_width // 2
            and y >= exit_btn_y - self.buttons_height // 2
            and y <= exit_btn_y + self.buttons_height // 2
        ):
            return 'exit'

        return None

    def handler(self, mouse: object) -> str:
        """
        Interface for state-machines to call the click method.
        """
        action = None

        if mouse.clicked:
            action = self.click(mouse.get_position())
            mouse.update()
        return action
