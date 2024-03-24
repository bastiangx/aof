import SimpleGUICS2Pygame.simpleguics2pygame as sg
from assets import PLAYER_HEALTH_IMG
from config import CANVAS_WIDTH, CANVAS_HEIGHT

class heart:
    def __init__(self):
        self.max_health = 100 #assumed 
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.SPRITE_SHEET_COLS = 2
        self.SPRITE_SHEET_ROWS = 1
        self.canvas_width = CANVAS_WIDTH
        self.canvas_height = CANVAS_HEIGHT

        self.player_health = self.max_health
        self.heart_in = 0 #starting at 0
        self.image = PLAYER_HEALTH_IMG

    def draw(self, canvas):
        heart_x = (self.heart_in % self.SPRITE_SHEET_COLS) * self.width
        heart_y = (self.heart_in // self.SPRITE_SHEET_COLS) * self.height
        heart_pos = (self.canvas_width - self.width, 0)


        canvas.draw_image(self.image,
                          (heart_x + self.width/2, heart_y + self.height/2),
                          (self.width, self.height),
                          (self.width/2, self.height/2),
                          (self.width, self.height))
    
    def decrease_playerhealth(self):
        if self.player_health > 0:
            self.player_health -= 5# player losses health by 5 (assumed)
            self.heart_in = min(self.SPRITE_SHEET_COLS - 1, self.heart_in + 1) # moving to next picture
    
    def player_zombie_collision(self):
        self.decrease_playerhealth()
    
