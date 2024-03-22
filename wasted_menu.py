from assets import PLAY_BTN, EXIT_BTN
from config import CANVAS_WIDTH, CANVAS_HEIGHT


class WastedMenu:
    """
    end/wasted menu rendering and interactions
    handler returns the action as a str
    click detects the mouse click on buttons and returns the action
    """

    def __init__(self) -> None:
        self.play_btn_img = PLAY_BTN
        self.exit_btn_img = EXIT_BTN

        self.buttons_width = 200
        self.buttons_height = 100
        self.margin = 20

        self.midpoint_width = CANVAS_WIDTH // 2
        self.midpoint_height = CANVAS_HEIGHT // 2

    # def handler(self, mouse: object) -> str:
    def handler(self, mouse: object) -> str:
        """
        interface for other classes to call the click method
        return None if no click is present
        """
        action = None

        if mouse.clicked:
            action = self.click(mouse.get_position())
            mouse.clicked = False

        return action

    def calculate_button_positions(self) -> tuple:
        """
        Calculate the x and y positions of the buttons_width
        return the top-left corner of each button for click detection
        """
        # x positions
        play_btn_x = self.midpoint_width - self.buttons_width / 2
        exit_btn_x = play_btn_x

        # y positions
        base_y = self.midpoint_height + self.margin + self.buttons_height

        play_btn_y = base_y
        exit_btn_y = play_btn_y + self.buttons_height + self.margin

        # Return the top-left corner of each button
        return (
            play_btn_x,
            play_btn_y,
            exit_btn_x,
            exit_btn_y,
        )

    def render(self, canvas: object) -> None:
        """
        Render the buttons on canvas
        """
        (
            play_btn_x,
            play_btn_y,
            exit_btn_x,
            exit_btn_y,
        ) = self.calculate_button_positions()

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
        """
        Detection based on the position of the mouse click on canvas
        returns the action as a str for handler to use
        """
        x, y = position
        # hitbox check around the buttons
        (
            play_btn_x,
            play_btn_y,
            exit_btn_x,
            exit_btn_y,
        ) = self.calculate_button_positions()

        # Play button
        if (
            play_btn_x < x < play_btn_x + self.buttons_width
            and play_btn_y < y < play_btn_y + self.buttons_height
        ):
            return 'play'

        # Exit button
        elif (
            exit_btn_x < x < exit_btn_x + self.buttons_width
            and exit_btn_y < y < exit_btn_y + self.buttons_height
        ):
            return 'exit'

        else:
            return None
