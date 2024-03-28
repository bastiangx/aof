from assets import (
    M_BG,
    M_BG_DARK,
    MM_LOGO,
    BTN_PLAY,
    BTN_EXIT,
    BTN_ABOUT,
    BTN_BACK,
    TITLE_USAGE,
    ABOUT_GITHUB,
    ABOUT_SOURCE,
)
from webbrowser import open_new_tab as open_link
from config import CANVAS_WIDTH, CANVAS_HEIGHT
from jukebox import UI


ui_click = UI()
about_pressed = False


class MainMenu:
    """
    for rendering the main menu of a game and handling user interactions.

    responsible for displaying the main menu of a game, including play, about, and exit buttons,
    as well as the game's logo and background. handles user clicks on these buttons, performing the appropriate
    action, such as starting the game, opening an external link to the game's GitHub page, or exiting the game.

    -----------
    Attributes
    -----------
        *_img (object): The image object for the play and exit buttons.
        hyperlink (function): opens the team's GitHub page in a browser.

    -----------
    Methods
    -----------
        calculate_*: position of the logo and buttons on the canvas.

        render: draws all elements of the main menu on the canvas.

        click: detects user clicks on the play, about, and exit buttons.

        handler: interface for other classes/state-machines to call the click method.
    """

    def __init__(self) -> None:
        self.logo = MM_LOGO
        self.about_github = ABOUT_GITHUB
        self.about_source = ABOUT_SOURCE
        self.about_usage = TITLE_USAGE

        self.play_btn_img = BTN_PLAY
        self.about_btn_img = BTN_ABOUT
        self.back_btn_img = BTN_BACK
        self.exit_btn_img = BTN_EXIT

        self.bg = M_BG
        self.bg_dark = M_BG_DARK

        # all buttons are uniform
        self.buttons_width = self.play_btn_img.get_width()
        self.buttons_height = self.play_btn_img.get_height()

        self.logo_width = self.logo.get_width()
        self.logo_height = self.logo.get_height()

        # margins mm
        self.margin_top = 60
        self.margin_button = 45

        # margins about
        self.margin_middle_github = 118
        self.margin_middle_source = 150
        self.margin_middle_usage = 64

    def calculate_logo_position(self) -> tuple:
        return (
            CANVAS_WIDTH / 2 - self.logo_width / 2,
            self.margin_top,
        )

    def calculate_button_positions(self) -> tuple:
        # x position
        base_x = CANVAS_WIDTH / 2 - self.buttons_width / 2

        play_btn_x = base_x
        about_btn_x = base_x
        exit_btn_x = base_x

        # y position
        base_y = (CANVAS_HEIGHT / 2) + self.margin_top

        play_btn_y = base_y
        about_btn_y = base_y + self.buttons_height + self.margin_button
        exit_btn_y = about_btn_y + self.buttons_height + self.margin_button

        # return the top-left corner of each button
        return (
            play_btn_x,
            play_btn_y,
            about_btn_x,
            about_btn_y,
            exit_btn_x,
            exit_btn_y,
        )

    def calculate_button_back_position(self) -> tuple:
        return (
            CANVAS_WIDTH / 2 - self.back_btn_img.get_width() / 2,
            self.margin_top,
        )

    def calculate_about_github_position(self) -> tuple:
        return (
            (CANVAS_WIDTH / 2) - (self.about_github.get_width() / 2),
            (CANVAS_HEIGHT / 2)
            - (self.about_github.get_height() / 2)
            - self.margin_top,
        )

    def calculate_about_source_position(self) -> tuple:
        return (
            (CANVAS_WIDTH / 2) - (self.about_source.get_width() / 2),
            (CANVAS_HEIGHT / 2)
            + (self.about_source.get_height() / 2)
            + self.margin_middle_source,
        )

    def calculate_about_usage_position(self) -> tuple:
        return (
            (CANVAS_WIDTH / 2) - (self.about_usage.get_width() / 2),
            CANVAS_HEIGHT
            - self.about_usage.get_height()
            - self.margin_middle_usage,
        )

    def render(self, canvas: object) -> None:
        global about_pressed

        if not about_pressed:
            # logo position
            (
                logo_x,
                logo_y,
            ) = self.calculate_logo_position()

            # buttons position
            (
                play_btn_x,
                play_btn_y,
                about_btn_x,
                about_btn_y,
                exit_btn_x,
                exit_btn_y,
            ) = self.calculate_button_positions()

            # main background
            canvas.draw_image(
                self.bg,
                (
                    self.bg.get_width() / 2,
                    self.bg.get_height() / 2,
                ),
                (self.bg.get_width(), self.bg.get_height()),
                (
                    CANVAS_WIDTH / 2,
                    CANVAS_HEIGHT / 2,
                ),
                (CANVAS_WIDTH, CANVAS_HEIGHT),
            )

            # logo
            canvas.draw_image(
                self.logo,
                (
                    self.logo.get_width() / 2,
                    self.logo.get_height() / 2,
                ),
                (self.logo.get_width(), self.logo.get_height()),
                (
                    logo_x + self.logo_width / 2,
                    logo_y + self.logo_height / 2,
                ),
                (self.logo_width, self.logo_height),
            )

            # play button
            canvas.draw_image(
                self.play_btn_img,
                (
                    self.play_btn_img.get_width() / 2,
                    self.play_btn_img.get_height() / 2,
                ),
                (
                    self.play_btn_img.get_width(),
                    self.play_btn_img.get_height(),
                ),
                (
                    play_btn_x + self.buttons_width / 2,
                    play_btn_y + self.buttons_height / 2,
                ),
                (self.buttons_width, self.buttons_height),
            )

            # about button
            canvas.draw_image(
                self.about_btn_img,
                (
                    self.about_btn_img.get_width() / 2,
                    self.about_btn_img.get_height() / 2,
                ),
                (
                    self.about_btn_img.get_width(),
                    self.about_btn_img.get_height(),
                ),
                (
                    about_btn_x + self.buttons_width / 2,
                    about_btn_y + self.buttons_height / 2,
                ),
                (self.buttons_width, self.buttons_height),
            )

            # exit button
            canvas.draw_image(
                self.exit_btn_img,
                (
                    self.exit_btn_img.get_width() / 2,
                    self.exit_btn_img.get_height() / 2,
                ),
                (
                    self.exit_btn_img.get_width(),
                    self.exit_btn_img.get_height(),
                ),
                (
                    exit_btn_x + self.buttons_width / 2,
                    exit_btn_y + self.buttons_height / 2,
                ),
                (self.buttons_width, self.buttons_height),
            )
        # about screen
        elif about_pressed:
            # buttons position
            (
                back_btn_x,
                back_btn_y,
            ) = self.calculate_button_back_position()

            (
                github_x,
                github_y,
            ) = self.calculate_about_github_position()

            (
                source_x,
                source_y,
            ) = self.calculate_about_source_position()

            (
                usage_x,
                usage_y,
            ) = self.calculate_about_usage_position()

            # dark background
            canvas.draw_image(
                self.bg_dark,
                (
                    self.bg_dark.get_width() / 2,
                    self.bg_dark.get_height() / 2,
                ),
                (self.bg_dark.get_width(), self.bg_dark.get_height()),
                (
                    CANVAS_WIDTH / 2,
                    CANVAS_HEIGHT / 2,
                ),
                (CANVAS_WIDTH, CANVAS_HEIGHT),
            )
            # back button
            canvas.draw_image(
                self.back_btn_img,
                (
                    self.back_btn_img.get_width() / 2,
                    self.back_btn_img.get_height() / 2,
                ),
                (
                    self.back_btn_img.get_width(),
                    self.back_btn_img.get_height(),
                ),
                (
                    back_btn_x + self.back_btn_img.get_width() / 2,
                    back_btn_y + self.back_btn_img.get_height() / 2,
                ),
                (
                    self.back_btn_img.get_width(),
                    self.back_btn_img.get_height(),
                ),
            )
            # about github
            canvas.draw_image(
                self.about_github,
                (
                    self.about_github.get_width() / 2,
                    self.about_github.get_height() / 2,
                ),
                (
                    self.about_github.get_width(),
                    self.about_github.get_height(),
                ),
                (
                    github_x + self.about_github.get_width() / 2,
                    github_y + self.about_github.get_height() / 2,
                ),
                (
                    self.about_github.get_width(),
                    self.about_github.get_height(),
                ),
            )
            # about source
            canvas.draw_image(
                self.about_source,
                (
                    self.about_source.get_width() / 2,
                    self.about_source.get_height() / 2,
                ),
                (
                    self.about_source.get_width(),
                    self.about_source.get_height(),
                ),
                (
                    source_x + self.about_source.get_width() / 2,
                    source_y + self.about_source.get_height() / 2,
                ),
                (
                    self.about_source.get_width(),
                    self.about_source.get_height(),
                ),
            )
            # about usage
            canvas.draw_image(
                self.about_usage,
                (
                    self.about_usage.get_width() / 2,
                    self.about_usage.get_height() / 2,
                ),
                (
                    self.about_usage.get_width(),
                    self.about_usage.get_height(),
                ),
                (
                    usage_x + self.about_usage.get_width() / 2,
                    usage_y + self.about_usage.get_height() / 2,
                ),
                (
                    self.about_usage.get_width(),
                    self.about_usage.get_height(),
                ),
            )

    def click(self, position: tuple) -> str:
        # mouse click position
        x, y = position

        # hitbox check around the buttons
        (
            play_btn_x,
            play_btn_y,
            about_btn_x,
            about_btn_y,
            exit_btn_x,
            exit_btn_y,
        ) = self.calculate_button_positions()

        # back button hitbox
        back_btn_x, back_btn_y = self.calculate_button_back_position()

        # about github hitbox
        github_x, github_y = self.calculate_about_github_position()

        # about source hitbox
        source_x, source_y = self.calculate_about_source_position()

        if not about_pressed:
            # Play button
            if (
                play_btn_x < x < play_btn_x + self.buttons_width
                and play_btn_y < y < play_btn_y + self.buttons_height
            ):
                ui_click.play()
                return 'play'

            # About button
            elif (
                about_btn_x < x < about_btn_x + self.buttons_width
                and about_btn_y < y < about_btn_y + self.buttons_height
            ):
                ui_click.play()
                return 'about'

            # Exit button
            elif (
                exit_btn_x < x < exit_btn_x + self.buttons_width
                and exit_btn_y < y < exit_btn_y + self.buttons_height
            ):
                return 'exit'

        elif about_pressed:

            # back button
            if (
                back_btn_x < x < back_btn_x + self.back_btn_img.get_width()
                and back_btn_y
                < y
                < back_btn_y + self.back_btn_img.get_height()
            ):
                ui_click.play_back()
                return 'back'

            # GitHub link
            elif (
                github_x < x < github_x + self.about_github.get_width()
                and github_y < y < github_y + self.about_github.get_height()
            ):
                ui_click.play()
                open_link('https://github.com/bastiangx/aof')

            # source git link
            elif (
                source_x < x < source_x + self.about_source.get_width()
                and source_y < y < source_y + self.about_source.get_height()
            ):
                ui_click.play()
                open_link('https://github.com/bastiangx/aof')

        else:
            return None

    def handler(self, mouse: object) -> str:
        """
        Interface for state-machines to call the click method.
        """
        action = None

        if mouse.clicked:
            action = self.click(mouse.get_position())
            mouse.update()

            if action == 'about':
                global about_pressed
                about_pressed = True
                mouse.update()

            if action == 'back':
                about_pressed = False
                mouse.update()

        return action
