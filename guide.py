from assets import GUIDE_BANNER, GUIDE_BG, GUIDE_NUMBERS
from config import CANVAS_WIDTH, CANVAS_HEIGHT

counter = 0
frames = 480  # 5 seconds


class Guide:
    def __init__(self) -> None:
        self.prompt = GUIDE_BANNER
        self.bg = GUIDE_BG
        self.numbers = GUIDE_NUMBERS

        self.current_number = 7

        self.numbers_width = 20
        self.numbers_height = 19

        self.prompt_width = self.prompt.get_width()
        self.prompt_height = self.prompt.get_height()

        self.x = CANVAS_WIDTH // 2
        self.y = CANVAS_HEIGHT // 2

        self.margin_top: int = 66
        self.margin_side: int = 100

    def calculate_prompt_position(self) -> tuple:
        return (self.x, self.y)

    def calculate_numbers_position(self) -> tuple:
        return (self.x + self.margin_side, self.margin_top)

    def count_down(self, canvas: object) -> str:
        global counter, frames

        if counter < frames:
            counter += 1

        if counter % 60 == 0 and counter != 0:
            self.next_number()

        if counter >= frames:
            counter = 0
            return 'continue'
        return 'stay'

    def next_number(self) -> None:
        self.current_number -= 1

        if self.current_number < 0:
            self.current_number = 0

    def get_current_number(self) -> object:
        return self.numbers[self.current_number]

    def render(self, canvas: object) -> None:
        prompt_x, prompt_y = self.calculate_prompt_position()
        numbers_x, numbers_y = self.calculate_numbers_position()

        # background
        canvas.draw_image(
            self.bg,
            (CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2),
            (CANVAS_WIDTH, CANVAS_HEIGHT),
            (CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2),
            (CANVAS_WIDTH, CANVAS_HEIGHT),
        )

        # # prompt image
        canvas.draw_image(
            self.prompt,
            (self.prompt_width // 2, self.prompt_height // 2),
            (self.prompt_width, self.prompt_height),
            (prompt_x, prompt_y),
            (self.prompt_width, self.prompt_height),
        )
        # numbers
        canvas.draw_image(
            self.get_current_number(),
            (self.numbers_width // 2, self.numbers_height // 2),
            (self.numbers_width, self.numbers_height),
            (numbers_x, numbers_y),
            (self.numbers_width, self.numbers_height),
        )
