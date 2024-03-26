from random import uniform as ru, choice as rc, randint as rn
from config import CANVAS_WIDTH
from zombies import Zombie
import time


class FactoryHandler:
    """
    Handles the wave event and the regular zombie spawn
    Interface for the ZombieFactory and WaveFactory classes

    Methods:

    score_check(score) -> str: checks if the score is within the wave range
    can_preserve(score) -> bool: checks if the wave event can be preserved
    preserve() -> bool: timer for the wave event. remains true for a random duration
    spawn_zombies(score, zombies_list) -> None: spawns zombies based on the score

    @staticmethod: do not require instantiation, do not require specific class instance/attribute
    @classmethod: do not require instantiation, require specific class instance/attribute to change
    """

    @staticmethod
    def score_check(score: int) -> str:
        if 8 <= score <= 18:
            return str('wave')
        return str('regular')

    @staticmethod
    def can_preserve(score: int) -> bool:
        spawn_type = FactoryHandler.score_check(score)   # get the spawn type

        if spawn_type == 'wave':
            return FactoryHandler.preserve()

        return False

    @staticmethod
    def preserve() -> bool:
        current_time = time.time()   # get initial time
        elapsed_time = (
            current_time - WaveFactory.last_spawn_time
        )   # get elapsed time
        duration = rn(10, 45)

        if elapsed_time < duration:
            WaveFactory.last_spawn_time = (
                current_time  # reset the last spawn time
            )
            return True

        else:
            WaveFactory.last_spawn_time = time.time()
            return False

    @staticmethod
    def spawn_zombies(score: int, zombies_list: list) -> None:
        spawn_type = FactoryHandler.score_check(score)   # get the spawn type

        if spawn_type == 'wave' and WaveFactory.can_spawn():
            if FactoryHandler.can_preserve(
                score
            ):   # for the duration of preserve
                zombie = WaveFactory.spawner()
                zombies_list.append(zombie)
                print('wave zombie spawned')

        elif ZombieFactory.can_spawn():
            if spawn_type != 'wave':   # regular spawn during normal gameplay
                zombie = ZombieFactory.spawner()
                zombies_list.append(zombie)
                print('zombie spawned')


class ZombieFactory:
    """
    Factory for the regular zombie spawn_type
    Non-wave event handler

    Methods:
        gen_velocity_range() -> float: generates a random velocity for the zombie
        gen_cooldown() -> float: generates a random cooldown for the zombie
        can_spawn() -> bool: checks if the zombie can spawn within the cooldown timer
        cooldown_calculation() -> float: adds randomness & ranges to the cooldown timer
        spawner() -> Zombie: returns a zombie object with a random position and velocity
    """

    last_spawn_time = time.time()
    last_adjustment_time = time.time()
    spawn_cooldown = 2

    @staticmethod
    def gen_velocity_range() -> float:
        choice = rc(['higher', 'regular', 'lower'])
        return {
            'higher': ru(1.4, 2.4),
            'regular': ru(1, 1.7),
            'lower': ru(0.8, 1.2),
        }.get(choice, 1.25)

    @staticmethod
    def gen_cooldown() -> float:
        return rn(2, 6)

    @staticmethod
    def can_spawn() -> bool:
        current_time = time.time()
        elapsed_time = current_time - ZombieFactory.last_spawn_time
        cooldown = ZombieFactory.cooldown_calculation()

        if elapsed_time >= cooldown:
            ZombieFactory.last_spawn_time = current_time
            return True
        return False

    @classmethod
    def cooldown_calculation(cls: object) -> float:
        current_time = time.time()  # get the current time
        elapsed_time = (
            current_time - cls.last_adjustment_time
        )  # calculate the elapsed time

        # decrease cooldown by 1% every 30 seconds
        if elapsed_time >= 30:
            cls.spawn_cooldown *= 0.999
            cls.last_adjustment_time = current_time  # reset the start time

        random_factor = ru(0.8, 1.2)  # randomize cooldown by 20%
        return cls.spawn_cooldown * random_factor

    @staticmethod
    def spawner() -> Zombie:
        y = ru(400, 1400) * -1
        x = ru(50, CANVAS_WIDTH - 50)
        velocity = ZombieFactory.gen_velocity_range()

        return Zombie(x, y, velocity)


class WaveFactory:
    """
    Overrides the regular zombie spawn_type
    Faster, more aggressive, and more frequent
    """

    last_spawn_time = time.time()
    last_adjustment_time = time.time()
    spawn_cooldown = 1

    @staticmethod # override: no slow velocity
    def gen_velocity_range() -> float:
        choice = rc(['higher', 'regular'])
        return {
            'higher': ru(2, 2.8),
            'regular': ru(1.3, 2),
        }.get(choice, 1.5)

    @staticmethod
    def gen_cooldown() -> float:
        return rn(2, 3)

    @staticmethod
    def can_spawn() -> bool:
        current_time = time.time()
        elapsed_time = current_time - WaveFactory.last_spawn_time
        cooldown = WaveFactory.cooldown_calculation()

        if elapsed_time >= cooldown:
            WaveFactory.last_spawn_time = current_time
            return True
        return False

    @classmethod
    def cooldown_calculation(cls: object) -> float:
        current_time = time.time()
        elapsed_time = current_time - cls.last_adjustment_time

        # for 22 seconds, decrease cooldown by 5%
        if elapsed_time >= 22:
            cls.spawn_cooldown *= 0.95
            cls.last_adjustment_time = current_time

        random_factor = ru(0.8, 1.2)
        return cls.spawn_cooldown * random_factor

    @staticmethod
    def spawner() -> Zombie:
        y = ru(300, 1000) * -1
        # override: closer spawn to screen and together
        x = ru(50, CANVAS_WIDTH - 50)
        velocity = WaveFactory.gen_velocity_range()

        return Zombie(x, y, velocity)
