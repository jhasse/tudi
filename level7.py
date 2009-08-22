from star import Star
from levelbase import LevelBase
import jngl

class Level(LevelBase):
    def __init__(self):
        LevelBase.__init__(self)
        self.stars = []
        for x in range(170, 770, 80):
            for y in range(250, 430, 80):
                if x == 250 and y == 250:
                    self.stars.append(Star(x, y, "red"))
                elif x == 490 and y == 410:
                    self.stars.append(Star(x, y, "red"))
                elif x == 650 and y == 250:
                    self.stars.append(Star(x, y, "red"))
                elif x == 170 and y == 250:
                    self.stars.append(Star(x, y, "blue"))
                else:
                    self.stars.append(Star(x, y))