import SimpleGUICS2Pygame.simpleguics2pygame as sg

from config import CANVAS_WIDTH, CANVAS_HEIGHT
from assets import BACKGROUND_IMG

class Background:

    def __init__(self, image_path, canvas_width, canvas_height):
        self.image = BACKGROUND_IMG
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.canvas_width = CANVAS_WIDTH
        self.canvas_height = CANVAS_HEIGHT
        self.x = 0
        self.y = 0

    def draw(self, canvas, player_x, player_y):
        self.x = self.canvas_width - player_x
        self.y = self.canvas_height - player_y

        canvas.draw_image(self.image,(self.width/2, self.height/2), 
                          (self.width, self.height), (self.x, self.y),
                          (self.canvas_width, self.canvas_height))
