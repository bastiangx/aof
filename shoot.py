from vector import Vector


class Shoot:
    """
    create bullet instance, set velocity to aim direction
    and reset cooldown counter

    Methods:

    fire_rate_iterator: limits the rate of fire - shoot spam
    aim: calculates the direction to shoot based on player[origin] and mouse pos[target]
    start: set aim to velocity, reset cooldown
    """

    def __init__(self) -> None:
        self.cooldown_counter = 0
        self.cooldown = 20

    def fire_rate(self) -> int:
        if self.cooldown_counter >= self.cooldown:
            self.cooldown_counter = 0
        elif self.cooldown_counter > 0:
            self.cooldown_counter += 1

        return self.cooldown_counter

    def aim(self, player_pos: tuple, mouse_pos: tuple) -> Vector:
        aim_direction = Vector(
            mouse_pos[0] - player_pos[0], mouse_pos[1] - player_pos[1]
        )
        return aim_direction.normalize()

    def start(self, bullet: object, player_pos: tuple, mouse_pos: tuple) -> None:
        aim_direction = self.aim(player_pos, mouse_pos)
        bullet.velocity = aim_direction * bullet.velocity_modifier

        self.cooldown_counter = 1
