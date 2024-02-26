from player import Player
from bullet import Bullet
from zombies import Zombie
from mouse import Mouse
from user_input import Keyboard


class Shoot:
    def __init__(self):
        self.bullets = []
        self.bullets_to_remove = []
        self.cooldown_counter = 0
        self.cooldown = 30

    def fire_rate(self):
        if self.cooldown_counter >= self.cooldown:
            self.cooldown_counter = 0
        elif self.cooldown_counter > 0:
            self.cooldown_counter += 1

    def shoot(self):
        if self.cooldown_counter == 0 and Keyboard.leader:
            self.bullets.append(Bullet(Player.x, Player.y))
            self.cooldown_counter = 1

    def draw(self, canvas):
        for bullet in self.bullets:
            bullet.draw(canvas)

    def update(self):
        for bullet in self.bullets:
            bullet.update()
            if bullet.off_screen():
                self.bullets_to_remove.append(bullet)

        for bullet in self.bullets_to_remove:
            self.bullets.remove(bullet)

    def damage_zombies(self, zombies):
        for bullet in self.bullets:
            for zombie in zombies:
                if bullet.is_collided(zombie):
                    bullet_index = self.bullets.index(bullet)
                    self.bullets.pop(bullet_index)
                    zombie.lose_health(Bullet.damage)
