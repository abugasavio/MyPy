
# place super_test.py code here

class Character:
    def __init__(self, speed=2, jump=2, power=2):
        self._speed = speed
        self._jump = jump
        self._power = power

    def jump(self):
        return self._jump

    def speed(self):
        return self._speed

    def power(self):
        return self._power


class Mario(Character):
    def speed(self):
        parent = super().speed()
        return parent + 2


class Luigi(Character):
    def speed(self):
        parent = super().speed()
        return parent + 1


# place keyword_test.py code here
