from config import CANVAS_WIDTH, CANVAS_HEIGHT
from jukebox import SoundEffect
import time

sound = SoundEffect()


class Collision:
    """
    Handle all entity collision checks

    Methods:
    player_to_zombie: check if player is colliding with any zombies and remove them
    bullet_to_zombie: check if bullets are colliding with zombies and remove them, += zombies_killed
    bullet_to_wall: check if bullets are off the screen and remove them
    zombie_to_base: check if zombies have reached the bottom of screen and remove them
    is_collision: main collision check function
    start: calls all the collision methods

    Attributes:
    cache: saves the heavy collision computation results to skip potential redundant checks
    zombies_killed: score tracking via bullet_to_zombie

    """

    def __init__(self) -> None:
        # cache the heavy collision checks to massively improve perf
        self.cache = {}
        self.cache_cleared = False

        self.bullets_to_remove = []
        self.zombies_to_remove = []

        self.damage_PZ = 10  # for player to zombie collision
        self.damage_BZ = 50  # for bullet to zombie collision
        self.damage_ZB = 15  # for zombie to base collision

        # for score tracking
        self.zombies_killed: int = 0

    def player_to_zombie(self, player: object, zombies_list) -> None:
        player_hitbox = player.get_hitbox()

        # clear the list of zombies to remove correct instances
        self.zombies_to_remove.clear()

        for zombie in zombies_list:
            zombie_hitbox = zombie.get_hitbox()

            # if key exists in cache, use the value. saves time and performance
            key = (tuple(player_hitbox), tuple(zombie_hitbox))
            if key in self.cache:
                if self.cache[key]:
                    sound.play_player_hit()
                    self.zombies_to_remove.append(zombie)
                    player.take_damage(self.damage_PZ)

            else:
                collision = self.is_collision(player_hitbox, zombie_hitbox)
                self.cache[key] = collision
                if collision:
                    sound.play_player_hit()
                    self.zombies_to_remove.append(zombie)
                    player.take_damage(self.damage_PZ)

        for zombie in self.zombies_to_remove:
            zombies_list.remove(zombie)

    def bullet_to_zombie(self, bullets_list: list, zombies_list: list) -> None:

        self.bullets_to_remove.clear()
        self.zombies_to_remove.clear()

        # nested loop, needs optimization later
        for bullet in bullets_list:
            bullet_hitbox = bullet.get_hitbox()
            for zombie in zombies_list:
                zombie_hitbox = zombie.get_hitbox()

                key = (tuple(bullet_hitbox), tuple(zombie_hitbox))
                if key in self.cache:
                    if self.cache[key]:
                        try:
                            sound.play_zombie_hit()
                            zombie.take_damage(self.damage_BZ)
                            self.bullets_to_remove.append(bullet)

                            # only remove zombie if it's wasted
                            if zombie.wasted():
                                sound.play_zombie_wasted()
                                self.zombies_to_remove.append(zombie)
                                self.zombies_killed += 1

                        except ValueError:
                            print('Two bullets hit the same zombie')

                else:
                    collision = self.is_collision(bullet_hitbox, zombie_hitbox)
                    self.cache[key] = collision
                    if collision:
                        try:
                            sound.play_zombie_hit()
                            zombie.take_damage(self.damage_BZ)
                            self.bullets_to_remove.append(bullet)

                            if zombie.wasted():
                                sound.play_zombie_wasted()
                                self.zombies_to_remove.append(zombie)
                                self.zombies_killed += 1

                        except ValueError:
                            print('Two bullets hit the same zombie')

        for bullet in self.bullets_to_remove:
            try:
                bullets_list.remove(bullet)
            except ValueError:
                print('Two bullets hit the same zombie')

        for zombie in self.zombies_to_remove:
            try:
                zombies_list.remove(zombie)
            except ValueError:
                print('Two bullets hit the same zombie')

    # zomb reaching bottom of screen
    def zombie_to_base(self, zombies_list: list, player: object) -> None:
        self.zombies_to_remove.clear()

        for zombie in zombies_list:
            zombie_hitbox = zombie.get_hitbox()
            if zombie_hitbox[1] + zombie_hitbox[3] > CANVAS_HEIGHT:
                sound.play_player_hit()
                player.take_damage(self.damage_ZB)
                self.zombies_to_remove.append(zombie)

        for zombie in self.zombies_to_remove:
            zombies_list.remove(zombie)

    def bullet_to_wall(self, bullets_list: list) -> None:
        self.bullets_to_remove.clear()

        for bullet in bullets_list:
            bullet_hitbox = bullet.get_hitbox()
            # 10px as buffer off the screen
            if (
                bullet_hitbox[0] < -10
                or bullet_hitbox[0] + bullet_hitbox[2] > CANVAS_WIDTH + 10
                or bullet_hitbox[1] < -10
                or bullet_hitbox[1] + bullet_hitbox[3] > CANVAS_HEIGHT + 10
            ):
                self.bullets_to_remove.append(bullet)

        for bullet in self.bullets_to_remove:
            bullets_list.remove(bullet)

    # main collision check func
    def is_collision(self, hitbox1: list, hitbox2: list) -> bool:
        return (  # check if corners of hitbox1 are inside hitbox2
            hitbox1[0] < hitbox2[0] + hitbox2[2]
            and hitbox1[0] + hitbox1[2] > hitbox2[0]
            and hitbox1[1] < hitbox2[1] + hitbox2[3]
            and hitbox1[1] + hitbox1[3] > hitbox2[1]
        )

    def reset_cache(self) -> None:
        # clear every 120 seconds
        # maintainance - important to reset
        current_time = time.time()
        if current_time % 120 == 0 and not self.cache_cleared:
            self.cache.clear()
            self.cache_cleared = True

        elif current_time % 60 != 0:
            self.cache_cleared = False

    def start(
        self, player: object, zombies_list: list, bullets_list: list
    ) -> None:
        """
        calls all the collision methods
        housekeeping
        """
        self.player_to_zombie(player, zombies_list)
        self.bullet_to_zombie(bullets_list, zombies_list)
        self.bullet_to_wall(bullets_list)
        self.zombie_to_base(zombies_list, player)
        self.reset_cache()
