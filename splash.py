from assets import SPLASH_LOGO, SPLASH_LOVE
from config import CANVAS_WIDTH, CANVAS_HEIGHT

counter = 0
frames = 200   # 3.3 seconds

class Splash:
    """
    shows a logo and a banner
    lasts for 200 frames / 3.3 seconds before moving on
    """
    def __init__(self) -> None:
        self.logo: object = SPLASH_LOGO
        self.love: object = SPLASH_LOVE

        self.logo_width = self.logo.get_width()
        self.logo_height = self.logo.get_height()

        self.love_width = self.love.get_width()
        self.love_height = self.love.get_height()

        self.margin_top: int = 350
        self.margin_between: int = 250

        self.base_x: int = CANVAS_WIDTH / 2
        self.base_y: int = CANVAS_HEIGHT / 2 - self.logo_height / 2

    def calculate_logo_position(self) -> tuple:
        return (
            self.base_x,
            self.base_y,
        )

    def calculate_love_position(self) -> tuple:
        return (
            self.base_x,
            self.base_y + self.logo_height + self.margin_between,
        )

    # count down the frames for 3.3 seconds
    def count_down(self) -> str:
        global counter, frames

        if counter < frames:
            counter += 1

        if counter >= frames:
            counter = 0
            return 'continue'
        return 'stay'

    def render(self, canvas: object) -> None:
        logo_x, logo_y = self.calculate_logo_position()
        love_x, love_y = self.calculate_love_position()

        # logo image
        canvas.draw_image(
            self.logo,
            (self.logo_width // 2, self.logo_height // 2),
            (self.logo_width, self.logo_height),
            (logo_x, logo_y),
            (self.logo_width, self.logo_height),
        )

        # love banner
        canvas.draw_image(
            self.love,
            (self.love_width // 2, self.love_height // 2),
            (self.love_width, self.love_height),
            (love_x, love_y),
            (self.love_width, self.love_height),
        )
