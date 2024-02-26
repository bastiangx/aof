# mouse class. gets the mouse position and the mouse clicked position and returns it


class Mouse:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.position = (self.x, self.y)
        self.clicked = False

    def click_handler(self, position):
        self.x = position[0]
        self.y = position[1]
        self.clicked = True

    def get_position(self, position):
        return position

    def update(self):
        if self.clicked:
            self.clicked = False
