# Collision Class:
# Create a Collision class responsible for handling collision detection between various game objects.
# This class can have methods to check for collisions between bullets, zombies, and the player.
# It should use simple bounding boxes  as hitboxes for each object for simplicity and performance.

from config import CANVAS_WIDTH, CANVAS_HEIGHT


class Collision:
    def __init__(self):
        self.name = 'Collision'

    def check_collision(self, obj1, obj2):
        pass

    def check_bullet_collision(self, bullets, zombies):
        pass

    def check_player_collision(self, player, zombies):
        pass

    def check_zombie_collision(self, zombies, player):
        pass

    def check_wall_collision(self, obj):
        # if the object is outside the screen or colliding with walls, return True
        if (
            obj.x <= 0
            or obj.x >= CANVAS_WIDTH
            or obj.y <= 0
            or obj.y >= CANVAS_HEIGHT
        ):
            return True
