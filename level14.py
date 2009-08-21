from star import Star
from levelbase import LevelBase
import jngl

class Level(LevelBase):
    def __init__(self):
        LevelBase.__init__(self)
        self.stars = []
        for x in range(170, 770, 160):
            self.stars.append(Star(x, 410))
            self.stars.append(Star(x + 80, 400))
        for x in range(170, 770, 320):
            self.stars.append(Star(x + 80, 190, "red"))
            self.stars.append(Star(x + 160, 190, "red"))
            self.stars.append(Star(x + 160, 270, "red"))
            self.stars.append(Star(x + 240, 190, "red"))