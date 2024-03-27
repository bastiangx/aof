from config import CANVAS_WIDTH, SCORE_FONT, SCORE_FONT_SIZE


class Score:
    """
    Handle & save the scores

    Methods:
    increment_score: increment the score by a certain value
    trigger_update: trigger the score to call increment_score()
    get_current_score: return the current score as an integer
    """

    def __init__(self) -> None:
        self.current_score = 0
        self.old_score = 0

    def increment_score(self, increment_value: int) -> None:
        """increment the score by the increment_value"""
        self.current_score += increment_value

    def trigger_update(self) -> None:
        """Trigger the score to call increment_score()"""
        self.increment_score(1)

    def get_current_score(self) -> int:
        """Return the current score as an integer"""
        return self.current_score

    def get_text_size(self) -> tuple:
        """return width and height of str(current_score)"""
        """ give minimum width and height of 20 and 40, then the str will be centred"""
        return (
            max(40, len(str(self.current_score)) * 60),
            max(40, 40),
        )

    def render(self, canvas: object) -> None:
        # render score, cnetred in the rectangle, top right of screen
        canvas.draw_text(
            str(self.current_score),
            (CANVAS_WIDTH - self.get_text_size()[0], self.get_text_size()[1]),
            SCORE_FONT_SIZE,
            'White',
            SCORE_FONT,
        )

    def reset(self) -> None:
        """Reset the score to 0"""
        self.current_score = 0
        self.old_score = 0
