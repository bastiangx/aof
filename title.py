from assets import TITLE_LOGO, TITLE_USAGE, TITLE_PROMPT, M_BG_DARK
from config import CANVAS_WIDTH, CANVAS_HEIGHT
from jukebox import UI

sound_click = UI()


class Title:
    """
    Handles title screen rendering and interactions
    Waits for user to click to continue
    shows the title logo, usage, and prompt

    """

    def __init__(self) -> None:
        self.logo: object = TITLE_LOGO
        self.usage: object = TITLE_USAGE
        self.prompt: object = TITLE_PROMPT

        self.logo_width = self.logo.get_width()
        self.logo_height = self.logo.get_height()

        self.usage_width = self.usage.get_width()
        self.usage_height = self.usage.get_height()

        self.prompt_width = self.prompt.get_width()
        self.prompt_height = self.prompt.get_height()

        self.margin_top: int = 300
        self.margin_lower: int = 60

        self.base_x: int = CANVAS_WIDTH // 2
        self.base_y: int = self.margin_top

    def calculate_logo_position(self) -> tuple:
        return (
            self.base_x,
            self.base_y,
        )

    def calculate_prompt_position(self) -> tuple:
        return (
            self.base_x,
            self.base_y + self.usage_height + self.margin_top,
        )

    def calculate_usage_position(self) -> tuple:
        return (
            self.base_x,
            self.calculate_prompt_position()[1]
            + self.usage_height
            + self.margin_lower,
        )

    def render(self, canvas: object) -> None:
        logo_x, logo_y = self.calculate_logo_position()
        usage_x, usage_y = self.calculate_usage_position()
        prompt_x, prompt_y = self.calculate_prompt_position()

        # background
        canvas.draw_image(
            M_BG_DARK,
            (CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2),
            (CANVAS_WIDTH, CANVAS_HEIGHT),
            (CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2),
            (CANVAS_WIDTH, CANVAS_HEIGHT),
        )

        # logo image
        canvas.draw_image(
            self.logo,
            (self.logo_width // 2, self.logo_height // 2),
            (self.logo_width, self.logo_height),
            (logo_x, logo_y),
            (self.logo_width, self.logo_height),
        )

        # usage image
        canvas.draw_image(
            self.usage,
            (self.usage_width // 2, self.usage_height // 2),
            (self.usage_width, self.usage_height),
            (usage_x, usage_y),
            (self.usage_width, self.usage_height),
        )

        # prompt image
        canvas.draw_image(
            self.prompt,
            (self.prompt_width // 2, self.prompt_height // 2),
            (self.prompt_width, self.prompt_height),
            (prompt_x, prompt_y),
            (self.prompt_width, self.prompt_height),
        )

    #   waits for user to click to continue
    def handler(self, mouse: object) -> str:
        action = 'stay'

        if mouse.clicked:
            sound_click.play()
            action = 'continue'
            return action

        return action
