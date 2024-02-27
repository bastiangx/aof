class Mouse:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.position = (self.x, self.y)
        self.clicked = False

    def click_handler(self, sg_position):
        self.x = sg_position[0]
        self.y = sg_position[1]
        self.clicked = True

    def get_position(self, position):
        return position

    def update(self):
        if self.clicked:
            self.clicked = False
