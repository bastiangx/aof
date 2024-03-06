from bullet import Bullet
from player import Player
from vector import Vector  # Assuming this is the Vector class you provided


class Shoot:
    def __init__(self):
        self.cooldown_counter = 0
        self.cooldown = 30

    # limits the rate of fire - shoot spam
    def fire_rate_iterator(self):
        if self.cooldown_counter >= self.cooldown:
            self.cooldown_counter = 0
        elif self.cooldown_counter > 0:
            self.cooldown_counter += 1

        return self.cooldown_counter

    # set aim to velocity, reset cooldown
    def start_shooting(self, bullet, player_pos, mouse_pos):
        aim_direction = self.aim(player_pos, mouse_pos)
        bullet.velocity = aim_direction * bullet.velocity_modifier

        self.cooldown_counter = 1

    # calculates the direction to shoot based on player and mouse pos
    def aim(self, player_pos, mouse_pos):
        aim_direction = Vector(
            mouse_pos[0] - player_pos[0], mouse_pos[1] - player_pos[1]
        )
        return aim_direction.normalize()
