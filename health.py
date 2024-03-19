"""
track and manage health, damage, healing and death of Player and Zombies
"""


class PlayerHealth:
    """
    health, damage, healing, dead
    """
    def __init__(self, health, damage, healing, dead):
        self.max_health: int = 100
        self.health: int = self.max_health
        self.damage: int = damage
        self.healing: int = healing
        self.dead: bool = dead

    def take_damage(self, damage: int) -> None:
        self.health -= damage

        if self.health <= 0:
            self.dead = True

    def heal(self, healing: int) -> None:
        # if health is full, do not heal
        if self.health == self.max_health:
            return

        # if healing is greater than max health, set health to max health
        if self.health + healing > self.max_health:
            self.health = self.max_health
        else:
            self.health += healing

    def is_dead(self) -> bool:
        return self.dead

    def is_alive(self) -> bool:
        return not self.dead

    def get_health(self) -> int:
        return self.health

    def get_damage(self) -> int:
        return self.damage

    def get_healing(self) -> int:
        return self.healing

    def get_dead(self) -> bool:
        return self.dead

    def set_health(self, health: int) -> None:
        self.health = health

    def set_damage(self, damage: int) -> None:
        self.damage = damage

    def set_healing(self, healing: int) -> None:
        self.healing = healing

    def set_dead(self, dead: bool) -> None:
        self.dead = dead

    def set_max_health(self) -> None:
        self.health = self.max_health


class ZombieHealth(PlayerHealth):
    def __init__(self, health, damage, healing, dead):
        super().__init__(health, damage, healing, dead)
