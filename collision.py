# class Grid:
#     def __init__(self, width, height, cell_size):
#         self.width = width
#         self.height = height
#         self.cell_size = cell_size
#         self.grid = self.create_grid()
#
#     def create_grid(self):
#         return [
#             [False for _ in range(self.width // self.cell_size)]
#             for _ in range(self.height // self.cell_size)
#         ]
#
#     def set_cell(self, x, y, value):
#         self.grid[y // self.cell_size][x // self.cell_size] = value
#
#     def section_clear(self, x, y, width, height):
#         for i in range(y // self.cell_size, (y + height) // self.cell_size):
#             for j in range(x // self.cell_size, (x + width) // self.cell_size):
#                 if self.grid[i][j]:
#                     return False
#         return True
#
#     def set_section(self, x, y, width, height, value):
#         for i in range(y // self.cell_size, (y + height) // self.cell_size):
#             for j in range(x // self.cell_size, (x + width) // self.cell_size):
#                 self.grid[i][j] = value
#
#     def near_object(self, x, y, width, height):
#         for i in range(
#             y // self.cell_size - 1, (y + height) // self.cell_size + 1
#         ):
#             for j in range(
#                 x // self.cell_size - 1, (x + width) // self.cell_size + 1
#             ):
#                 if (
#                     i >= 0
#                     and j >= 0
#                     and i < len(self.grid)
#                     and j < len(self.grid[0])
#                 ):
#                     if self.grid[i][j]:
#                         return True
#         return False
#
#     def get_cell(self, x, y):
#         return self.grid[y // self.cell_size][x // self.cell_size]
#
#     def get_grid(self):
#         return self.grid
#
#     def get_width(self):
#         return self.width
#
#     def get_height(self):
#         return self.height
#
#     def get_cell_size(self):
#         return self.cell_size
#
#
# class Collision:
# def check_player_to_zombie(self, player, zombies_list):
#     player_hitbox = player.get_hitbox()
#
#     for zombie in zombies_list:
#         zombie_hitbox = zombie.get_hitbox()
#         if (
#             player_hitbox[0] < zombie_hitbox[0] + zombie_hitbox[2]
#             and player_hitbox[0] + player_hitbox[2] > zombie_hitbox[0]
#             and player_hitbox[1] < zombie_hitbox[1] + zombie_hitbox[3]
#             and player_hitbox[1] + player_hitbox[3] > zombie_hitbox[1]
#         ):
#             self.handle_player_to_zombie(player, zombies_list)
#             return True
#
# def handle_player_to_zombie(self, player, zombies_list):
#     if self.check_player_to_zombie(player, zombies_list):
#         if zombies_list.size() > 0:
#             for zombie in zombies_list:
#                 zombies_list.remove(zombie)
#
# def check_bullet_to_zombie(self, zombies_list, bullets_list):
#     for zombie in zombies_list:
#         zombie_hitbox = zombie.get_hitbox()
#         for bullet in bullets_list:
#             bullet_hitbox = bullet.get_hitbox()
#             if (
#                 bullet_hitbox[0] < zombie_hitbox[0] + zombie_hitbox[2]
#                 and bullet_hitbox[0] + bullet_hitbox[2] > zombie_hitbox[0]
#                 and bullet_hitbox[1] < zombie_hitbox[1] + zombie_hitbox[3]
#                 and bullet_hitbox[1] + bullet_hitbox[3] > zombie_hitbox[1]
#             ):
#                 self.handle_bullet_to_zombie(zombies_list, bullets_list)
#                 return True
#
# def handle_bullet_to_zombie(self, zombies_list, bullets_list):
#     if self.check_bullet_to_zombie(zombies_list, bullets_list):
#         if zombies_list.size() > 0:
#             for zombie in zombies_list:
#                 zombies_list.remove(zombie)
#
#         if bullets_list:
#             for bullet in bullets_list:
#                 bullets_list.remove(bullet)
#
# # object hits the bottom of the screen
# def check_base(self, obj):
#     if obj.y >= CANVAS_HEIGHT:
#         return True
#
# def check_wall(self, zombies_list, bullets_list):
#     # object is outside or colliding the screen
#     if zombies_list or bullets_list:
#         for zombie in zombies_list:
#             zombie_hitbox = zombie.get_hitbox()
#             if (
#                 zombie_hitbox[0] < 0
#                 or zombie_hitbox[0] + zombie_hitbox[2] > CANVAS_WIDTH
#                 or zombie_hitbox[1] < 0
#                 or zombie_hitbox[1] + zombie_hitbox[3] > CANVAS_HEIGHT
#             ):
#                 self.handle_wall(zombies_list, bullets_list)
#                 return True
#
#         for bullet in bullets_list:
#             bullet_hitbox = bullet.get_hitbox()
#             if self.check_base(bullet) or (
#                 bullet_hitbox[0] < 0
#                 or bullet_hitbox[0] + bullet_hitbox[2] > CANVAS_WIDTH
#                 or bullet_hitbox[1] < 0
#                 or bullet_hitbox[1] + bullet_hitbox[3] > CANVAS_HEIGHT
#             ):
#                 self.handle_wall(bullets_list, zombies_list)
#                 return True
#     else:
#         return False
#

from config import CANVAS_WIDTH, CANVAS_HEIGHT


class Collision:
    def __init__(self):
        # cache the heavy collision checks to massively improve perf
        self.cache = {}
        self.cahe_cleared = False
        self.canvas_width = CANVAS_WIDTH
        self.canvas_height = CANVAS_HEIGHT

        self.bullets_to_remove = []
        self.zombies_to_remove = []

    def check_player_to_zombie(self, player, zombies_list):
        player_hitbox = player.get_hitbox()
        # clear the list of zombies to remove correct instances
        self.zombies_to_remove.clear()

        for zombie in zombies_list:
            zombie_hitbox = zombie.get_hitbox()

            # if key exists in cache, use the value. saves time and performance
            key = (tuple(player_hitbox), tuple(zombie_hitbox))
            if key in self.cache:
                if self.cache[key]:
                    self.zombies_to_remove.append(zombie)

            else:
                collision = self.is_collision(player_hitbox, zombie_hitbox)
                self.cache[key] = collision
                if collision:
                    self.zombies_to_remove.append(zombie)

        for zombie in self.zombies_to_remove:
            zombies_list.remove(zombie)

    def check_bullet_to_zombie(self, bullets_list, zombies_list):
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
                        self.bullets_to_remove.append(bullet)
                        self.zombies_to_remove.append(zombie)
                else:
                    collision = self.is_collision(bullet_hitbox, zombie_hitbox)
                    self.cache[key] = collision
                    if collision:
                        self.bullets_to_remove.append(bullet)
                        self.zombies_to_remove.append(zombie)

        for bullet in self.bullets_to_remove:
            bullets_list.remove(bullet)
        for zombie in self.zombies_to_remove:
            zombies_list.remove(zombie)

    def check_bullet_to_wall(self, bullets_list):
        self.bullets_to_remove.clear()

        for bullet in bullets_list:
            bullet_hitbox = bullet.get_hitbox()
            # 10px as buffer off the screen
            if (
                bullet_hitbox[0] < -10
                or bullet_hitbox[0] + bullet_hitbox[2] > self.canvas_width + 10
                or bullet_hitbox[1] < -10
                or bullet_hitbox[1] + bullet_hitbox[3]
                > self.canvas_height + 10
            ):
                self.bullets_to_remove.append(bullet)

        for bullet in self.bullets_to_remove:
            bullets_list.remove(bullet)

    # zomb reaching bottom of screen
    def check_zombie_to_base(self, zombies_list):
        self.zombies_to_remove.clear()

        for zombie in zombies_list:
            zombie_hitbox = zombie.get_hitbox()
            if zombie_hitbox[1] + zombie_hitbox[3] > self.canvas_height:
                self.zombies_to_remove.append(zombie)

        for zombie in self.zombies_to_remove:
            zombies_list.remove(zombie)

        # main collision check func

    def is_collision(self, hitbox1, hitbox2):
        return (
            hitbox1[0] < hitbox2[0] + hitbox2[2]
            and hitbox1[0] + hitbox1[2] > hitbox2[0]
            and hitbox1[1] < hitbox2[1] + hitbox2[3]
            and hitbox1[1] + hitbox1[3] > hitbox2[1]
        )

    def reset_cache(self, current_level):
        # maintainance - important to reset
        # reset the cache every 11 levels
        if current_level % 11 == 0 and not self.cahe_cleared:
            print("Cache cleared")
            self.cache.clear()
            self.cahe_cleared = True 

        elif current_level % 11 != 0:
            self.cahe_cleared = False 




# def handle_wall(self, zombies_list, bullets_list):
#     if self.check_wall(zombies_list, bullets_list):
#         if zombies_list.size() > 0:
#             for zombie in zombies_list:
#                 zombies_list.remove(zombie)
#
#         if bullets_list:
#             for bullet in bullets_list:
#                 bullets_list.remove(bullet)
#
# def check_collisions(self, bullets_list, zombies_list, player):
#     for bullet in bullets_list:
#         for zombie in zombies_list:
#             if (
#                 self.check_bullet_to_zombie(zombie, bullet)
#                 or self.check_wall(bullet)
#                 or self.check_player_to_zombie(player, zombie)
#             ):
#                 bullets_list.remove(bullet)
#                 zombies_list.remove(zombie)


# v3 didint work
# class Collision:
#     def check_player_to_zombie(self, player, zombies_list):
#         collided_zombies = []
#         player_hitbox = player.get_hitbox()
#
#         for zombie in zombies_list:
#             zombie_hitbox = zombie.get_hitbox()
#             if self.check_collision(player_hitbox, zombie_hitbox):
#                 collided_zombies.append(zombie)
#
#         return collided_zombies
#
#     def check_bullet_to_zombie(self, bullets_list, zombies_list):
#         collided_pairs = []
#         for bullet in bullets_list:
#             for zombie in zombies_list:
#                 zombie_hitbox = zombie.get_hitbox()
#                 bullet_hitbox = bullet.get_hitbox()
#                 if self.check_collision(bullet_hitbox, zombie_hitbox):
#                     collided_pairs.append((bullet, zombie))
#
#         return collided_pairs
#
#     def check_collision(self, hitbox1, hitbox2):
#         return (
#             hitbox1[0] < hitbox2[0] + hitbox2[2]
#             and hitbox1[0] + hitbox1[2] > hitbox2[0]
#             and hitbox1[1] < hitbox2[1] + hitbox2[3]
#             and hitbox1[1] + hitbox1[3] > hitbox2[1]
#         )
#
#     def check_wall_collision(self, obj):
#         return (
#             obj.x < 0
#             or obj.x + obj.width > CANVAS_WIDTH
#             or obj.y < 0
#             or obj.y + obj.height > CANVAS_HEIGHT
#         )
#
#     def handle_collisions(self, player, bullets_list, zombies_list):
#         # between player and zombies
#         collided_zombies = self.check_player_to_zombie(player, zombies_list)
#
#         # between bullets and zombies
#         collided_pairs = self.check_bullet_to_zombie(bullets_list, zombies_list)
#
#         # walls
#         collided_walls = []
#         for bullet in bullets_list:
#             if self.check_wall_collision(bullet):
#                 collided_walls.append(bullet)
#
#         for zombie in zombies_list:
#             if self.check_wall_collision(zombie):
#                 collided_walls.append(zombie)
#
#         return collided_zombies, collided_pairs, collided_walls
