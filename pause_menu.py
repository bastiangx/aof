from assets import PLAY_BTN, OPTIONS_BTN, EXIT_BTN
from config import CANVAS_WIDTH, CANVAS_HEIGHT


class PauseMenu:
    def __init__(self) -> None:
        self.play_btn_img = PLAY_BTN
        self.options_btn_img = OPTIONS_BTN
        self.exit_btn_img = EXIT_BTN

        self.buttons_width = 300
        self.buttons_height = 150
        self.margin = 275

        self.midpoint_width = CANVAS_WIDTH // 2
        self.midpoint_height = CANVAS_HEIGHT // 2

    def handler(self, mouse: object) -> str:
        action = None

        if mouse.clicked:
            action = self.click(mouse.get_position())
            mouse.clicked = False

        return action

    def calculate_button_positions(self) -> tuple:
        play_btn_x = self.midpoint_width - self.buttons_width / 2
        options_btn_x = self.midpoint_width - self.buttons_width / 2
        exit_btn_x = self.midpoint_width - self.buttons_width / 2

        play_btn_y = (
            self.midpoint_height - self.margin - self.buttons_height / 2
        )
        options_btn_y = self.midpoint_height - self.buttons_height / 2
        exit_btn_y = (
            self.midpoint_height + self.margin - self.buttons_height / 2
        )

        # Return the top-left corner of each button
        return (
            play_btn_x,
            play_btn_y,
            options_btn_x,
            options_btn_y,
            exit_btn_x,
            exit_btn_y,
        )

    def render(self, canvas: object) -> None:
        (
            play_btn_x,
            play_btn_y,
            options_btn_x,
            options_btn_y,
            exit_btn_x,
            exit_btn_y,
        ) = self.calculate_button_positions()

        # semi_transparent background
        canvas.draw_polygon(
            [
                (0, 0),
                (CANVAS_WIDTH, 0),
                (CANVAS_WIDTH, CANVAS_HEIGHT),
                (0, CANVAS_HEIGHT),
            ],
            1,
            'Black',
            'rgba(27, 21, 30, 0.7)',
        )
        # Play button
        canvas.draw_image(
            self.play_btn_img,
            (
                self.play_btn_img.get_width() / 2,
                self.play_btn_img.get_height() / 2,
            ),
            (self.play_btn_img.get_width(), self.play_btn_img.get_height()),
            (
                play_btn_x + self.buttons_width / 2,
                play_btn_y + self.buttons_height / 2,
            ),
            (self.buttons_width, self.buttons_height),
        )
        # Options button
        canvas.draw_image(
            self.options_btn_img,
            (
                self.options_btn_img.get_width() / 2,
                self.options_btn_img.get_height() / 2,
            ),
            (
                self.options_btn_img.get_width(),
                self.options_btn_img.get_height(),
            ),
            (
                options_btn_x + self.buttons_width / 2,
                options_btn_y + self.buttons_height / 2,
            ),
            (self.buttons_width, self.buttons_height),
        )
        # Exit button
        canvas.draw_image(
            self.exit_btn_img,
            (
                self.exit_btn_img.get_width() / 2,
                self.exit_btn_img.get_height() / 2,
            ),
            (self.exit_btn_img.get_width(), self.exit_btn_img.get_height()),
            (
                exit_btn_x + self.buttons_width / 2,
                exit_btn_y + self.buttons_height / 2,
            ),
            (self.buttons_width, self.buttons_height),
        )

    def click(self, position: tuple) -> str:
        x, y = position
        # hitbox check around the buttons
        (
            play_btn_x,
            play_btn_y,
            options_btn_x,
            options_btn_y,
            exit_btn_x,
            exit_btn_y,
        ) = self.calculate_button_positions()

        # Play button
        if (
            play_btn_x < x < play_btn_x + self.buttons_width
            and play_btn_y < y < play_btn_y + self.buttons_height
        ):
            print('play')
            return 'play'

        # Options button
        elif (
            options_btn_x < x < options_btn_x + self.buttons_width
            and options_btn_y < y < options_btn_y + self.buttons_height
        ):
            print('options')
            return 'options'

        # Exit button
        elif (
            exit_btn_x < x < exit_btn_x + self.buttons_width
            and exit_btn_y < y < exit_btn_y + self.buttons_height
        ):
            print('exit')
            return 'exit'

        else:
            return None
