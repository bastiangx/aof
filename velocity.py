from random import uniform as ru

class Velocity:
    def regular(self):
        return ru(2, 3)

    def lower(self):
        return ru(1, 2)

    def higher(self):
        return ru(3, 4)
