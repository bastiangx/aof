from config import CANVAS_WIDTH, SCORE_FONT, SCORE_FONT_SIZE

class HighScore:
    """
    Handle saving and loading high scores to/from a file

    Methods:
    save_high_score: Save the high score to a file
    load_high_score: Load the high score from a file
    """

    def __init__(self) -> None:
        self.high_score = 0

    def save_high_score(self) -> None:
        """Save the high score to a file"""
        try:
            with open("high_score.txt", "w") as file:
                file.write(str(self.high_score))
        except Exception as e:
            print(f"Error saving high score: {e}")

    def load_high_score(self) -> None:
        """Load the high score from a file"""
        try:
            with open("high_score.txt", "r") as file:
                content = file.read().strip()
                if content:
                    self.high_score = int(content)
                else:
                    self.high_score = 0
        except FileNotFoundError:
            # Handle case where file does not exist
            self.high_score = 0
        except Exception as e:
            print(f"Error loading high score: {e}")

    def update_high_score(self, new_score: int) -> None:
        """Update the high score if new score is higher"""
        if new_score > self.high_score:
            self.high_score = new_score
            self.save_high_score()



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
            max(20, len(str(self.current_score)) * 20),
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

    # dbg
    def print_if_changed(self):
        """Print the score if it has changed"""
        if self.current_score != self.old_score:
            print(f'Score: {self.current_score}')
            self.old_score = self.current_score

# Usage example
# Create an instance of HighScore
high_score_manager = HighScore()

# Load the high score from file
high_score_manager.load_high_score()

# Create an instance of Score
score_manager = Score()

# Update the score (example: score is obtained from gameplay)
game_score = 120
score_manager.increment_score(game_score)

# Update the high score if needed
high_score_manager.update_high_score(score_manager.get_current_score())

# Render the current score
# canvas.draw_text("Score: " + str(score_manager.get_current_score()), (10, 20), 20, "White")
