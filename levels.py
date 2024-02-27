from random import randint as rn, choice as rc


class Level:
    def __init__(self):
        self.initial_level = 1
        self.final_level = 100
        self.current_level = self.initial_level

        self.initial_phase = 1
        self.final_phase = 10
        self.current_phase = self.initial_phase

    def get_num_zombies(self):
        return {
            1: rn(3, 5),
            2: rn(4, 6),
            3: rn(6, 9),
            4: rn(6, 12),
            5: rn(8, 13),
            6: rn(9, 14),
            7: rn(10, 15),
            8: rn(12, 17),
            9: rn(12, 19),
            10: rn(15, 20),
        }.get(self.current_phase, 0)

    def get_velocity_range(self, num_zombies):
        midpoint = (self.get_num_zombies() + 1) // 2

        if num_zombies <= midpoint:
            return rc(['higher', 'regular'])
        else:
            return 'lower'

    def status(self):
        return self.current_level

    def next_level(self):
        print(f'Level {self.current_level} completed!')

        self.current_level += 1
        self.current_phase = (self.current_level - 1) // 10 + 1

        if self.current_level % 10 == 0:
            Wave().trigger()

        if self.current_level >= self.final_level:
            self.last_level_reached()

    def last_level_reached(self):
        pass


class Wave(Level):
    def __init__(self):
        super().__init__()
        self.current_wave = 1
        self.final_wave = 10

    def get_num_zombies(self):
        return {
            1: rn(8, 11),
            2: rn(10, 12),
            3: rn(11, 14),
            4: rn(12, 16),
            5: rn(14, 18),
            6: rn(16, 20),
            7: rn(18, 23),
            8: rn(20, 25),
            9: rn(22, 27),
            10: rn(28, 40),
        }.get(self.current_wave, 0)

    def get_velocity_range(self, num_zombies):
        return rc(['higher', 'regular'])

    def next(self):
        print(f'Wave {self.current_wave} triggered!')
        self.current_wave += 1

        if self.current_wave > self.final_wave:
            pass

    def trigger(self):
        print('Wave triggered!')

    def status(self):
        return self.current_wave
