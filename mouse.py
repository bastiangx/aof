class Mouse:
    """
    handle all click events

    Methods:
    click_handler(pos): set flag to true and store last position
    get_position(): return last reported position
    update(): reset click state to stop spam
    """

    def __init__(self) -> None:
        self.last_position = [0, 0]
        self.clicked = False

    def click_handler(self, pos: tuple) -> None:
        self.last_position = pos
        self.clicked = True

    def get_position(self) -> list:
        return self.last_position

    # reset click state to stop spam
    def update(self) -> None:
        if self.clicked:
            self.clicked = False
