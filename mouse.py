class Mouse:
    def __init__(self):
        self.last_position = [0, 0]
        self.clicked = False

    def click_handler(self, pos):
        self.last_position = pos
        self.clicked = True

    def get_position(self):
        return self.last_position

    # reset click state to stop spam
    def update(self):
        if self.clicked:
            self.clicked = False
