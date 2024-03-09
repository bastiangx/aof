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

    def increment_score(self, increment_value):
        """increment the score by the increment_value"""
        self.current_score += increment_value

    def trigger_update(self):
        """Trigger the score to call increment_score()"""
        self.increment_score(1)

    def get_current_score(self):
        """Return the current score as an integer"""
        return self.current_score

    def print_if_changed(self):
        """Print the score if it has changed"""
        if self.current_score != self.old_score:
            print(f'Score: {self.current_score}')
            self.old_score = self.current_score
