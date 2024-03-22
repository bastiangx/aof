from assets import PLAY_BTN, EXIT_BTN, GUIDE_IMG, TITLE_IMG, MAIN_BG
from config import CANVAS_WIDTH, CANVAS_HEIGHT


class MainMenu:
    """
    Main menu rendering and interactions
    handler returns the action as a str
    click detects the mouse click on buttons and returns the action
    """

    def __init__(self) -> None:
        self.play_btn_img = PLAY_BTN
        self.exit_btn_img = EXIT_BTN
        self.guide_img = GUIDE_IMG
        self.title_img = TITLE_IMG
        self.main_bg = MAIN_BG

        self.buttons_width = 225
        self.buttons_height = 130

        self.guide_width = 600
        self.guide_height = 400

        self.title_width = 900
        self.title_height = 500

        self.margin = 20
        self.menu_offset = 1.18

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
        base_x = (
            self.midpoint_width - self.buttons_width - (self.margin * 8)
        ) / 2

        play_btn_x = base_x
        exit_btn_x = base_x

        # y positions
        base_y = (self.midpoint_height + self.margin) * self.menu_offset

        play_btn_y = base_y
        exit_btn_y = play_btn_y + self.buttons_height + (self.margin * 2)

        # Return the top-left corner of each button
        return (
            play_btn_x,
            play_btn_y,
            exit_btn_x,
            exit_btn_y,
        )

    def calculate_guide_position(
        self, buttons_x: int, buttons_y: int
    ) -> tuple:
        """
        Calculate the x and y positions of the guide image
        based on a margin from the buttons x and y positions
        """
        # x position
        guide_x = buttons_x + self.buttons_width + (self.margin * 4)

        # y position
        guide_y = buttons_y - self.margin - 50
        return (guide_x, guide_y)

    def calculate_title_position(self) -> tuple:
        """
        Calculate the x and y positions of the title image
        """
        # x position
        title_x = self.midpoint_width - self.title_width / 2

        # y position
        title_y = self.margin / 2
        return (title_x, title_y)

    def render(self, canvas: object) -> None:
        """
        Render stuff on canvas
        """
        # get the x and y positions of the buttons
        (
            play_btn_x,
            play_btn_y,
            exit_btn_x,
            exit_btn_y,
        ) = self.calculate_button_positions()

        # get the x and y positions of the guide image
        (guide_x, guide_y) = self.calculate_guide_position(
            play_btn_x, play_btn_y
        )

        # get the x and y positions of the title image
        (title_x, title_y) = self.calculate_title_position()

        # main background
        canvas.draw_image(
            self.main_bg,
            (
                self.main_bg.get_width() / 2,
                self.main_bg.get_height() / 2,
            ),
            (self.main_bg.get_width(), self.main_bg.get_height()),
            (
                CANVAS_WIDTH / 2,
                CANVAS_HEIGHT / 2,
            ),
            (CANVAS_WIDTH, CANVAS_HEIGHT),
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

        # Guide image
        canvas.draw_image(
            self.guide_img,
            (
                self.guide_img.get_width() / 2,
                self.guide_img.get_height() / 2,
            ),
            (self.guide_img.get_width(), self.guide_img.get_height()),
            (
                guide_x + self.guide_width / 2,
                guide_y + self.guide_height / 2,
            ),
            (self.guide_width, self.guide_height),
        )

        # Title image
        canvas.draw_image(
            self.title_img,
            (
                self.title_img.get_width() / 2,
                self.title_img.get_height() / 2,
            ),
            (self.title_img.get_width(), self.title_img.get_height()),
            (
                title_x + self.title_width / 2,
                title_y + self.title_height / 2,
            ),
            (self.title_width, self.title_height),
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
