
"""from assets import PLAY_BTN, OPTIONS_BTN, EXIT_BTN
from config import CANVAS_WIDTH, CANVAS_HEIGHT


class MainMenu:
    def __init__(self) -> None:
        self.play_btn_img = PLAY_BTN
        self.options_btn_img = OPTIONS_BTN
        self.exit_btn_img = EXIT_BTN

        self.buttons_width = 200
        self.buttons_height = 100
        self.margin = 20
        self.menu_offset = 1.4

        self.midpoint_width = CANVAS_WIDTH // 2
        self.midpoint_height = CANVAS_HEIGHT // 2

    # def handler(self, mouse: object) -> str:
    def handler(self, mouse: object) -> str:
        
     
        action = None

        if mouse.clicked:
            action = self.click(mouse.get_position())
            mouse.clicked = False

        return action

    def calculate_button_positions(self) -> tuple:
        
      
    
        # x positions
        play_btn_x = self.midpoint_width - self.buttons_width / 2
        options_btn_x = play_btn_x
        exit_btn_x = play_btn_x

        # y positions
        base_y = self.midpoint_height + self.margin

        play_btn_y = base_y
        options_btn_y = base_y + self.buttons_height + self.margin
        exit_btn_y = options_btn_y + self.buttons_height + self.margin

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
            return 'play'

        # Options button
        elif (
            options_btn_x < x < options_btn_x + self.buttons_width
            and options_btn_y < y < options_btn_y + self.buttons_height
        ):
            return 'options'

        # Exit button
        elif (
            exit_btn_x < x < exit_btn_x + self.buttons_width
            and exit_btn_y < y < exit_btn_y + self.buttons_height
        ):
            return 'exit'

        else:
            return None
        

"""
from assets import PLAY_BTN, OPTIONS_BTN, EXIT_BTN
from config import CANVAS_WIDTH, CANVAS_HEIGHT



class MainMenu:
    def __init__(self, high_scores:list) -> None:
        self.play_btn_img = PLAY_BTN
        self.options_btn_img = OPTIONS_BTN
        self.exit_btn_img = EXIT_BTN

        self.buttons_width = 200
        self.buttons_height = 100
        self.margin = 20
        self.menu_offset = 1.4

        self.midpoint_width = CANVAS_WIDTH // 2
        self.midpoint_height = CANVAS_HEIGHT // 2
        self.high_scores=[]
        self.high_scores = high_scores  # Example high scores

    def handler(self, mouse: object) -> str:
        action = None

        if mouse.clicked:
            action = self.click(mouse.get_position())
            mouse.clicked = False

        return action

    def calculate_button_positions(self) -> tuple:
        play_btn_x = self.midpoint_width - self.buttons_width / 2
        options_btn_x = play_btn_x
        exit_btn_x = play_btn_x

        base_y = self.midpoint_height + self.margin

        play_btn_y = base_y
        options_btn_y = base_y + self.buttons_height + self.margin
        exit_btn_y = options_btn_y + self.buttons_height + self.margin

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

        # Drawing high score table
        table_x = play_btn_x + self.buttons_width + self.margin
        table_y = play_btn_y
        table_width = 200
        table_height = len(self.high_scores) * 30 + 30  # Adjust according to the number of scores

        # Drawing table background
        table_points = [
            (table_x, table_y),
            (table_x + table_width, table_y),
            (table_x + table_width, table_y + table_height),
            (table_x, table_y + table_height)
        ]
        canvas.draw_polygon(
            table_points,
            fill_color="white",
            line_color="black",
            line_width=2  # Add line_width argument
        )

        # Drawing table header
        canvas.draw_text(
            "High Scores",
            (table_x + 10, table_y + 20),
            20,
            "black",
        )
        canvas.draw_line(
            (table_x, table_y + 30),
            (table_x + table_width, table_y + 30),
            2,
            "black",
        )

        # Drawing scores
        for i, (player, score) in enumerate(self.high_scores):
            canvas.draw_text(
                f"{player}: {score}",
                (table_x + 10, table_y + 50 + i * 30),
                16,
                "black",
            )

    def click(self, position: tuple) -> str:
        x, y = position
        (
            play_btn_x,
            play_btn_y,
            options_btn_x,
            options_btn_y,
            exit_btn_x,
            exit_btn_y,
        ) = self.calculate_button_positions()

        if (
            play_btn_x < x < play_btn_x + self.buttons_width
            and play_btn_y < y < play_btn_y + self.buttons_height
        ):
            return "play"
        elif (
            options_btn_x < x < options_btn_x + self.buttons_width
            and options_btn_y < y < options_btn_y + self.buttons_height
        ):
            return "options"
        elif (
            exit_btn_x < x < exit_btn_x + self.buttons_width
            and exit_btn_y < y < exit_btn_y + self.buttons_height
        ):
            return "exit"
        else:
            return None
