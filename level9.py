from star import Star
from levelbase import LevelBase
import jngl

class Level(LevelBase):
    def __init__(self):
        LevelBase.__init__(self)
        self.stars = []
        for y in range(270, 480, 80):
            self.stars.append(Star(250, y, "red"))
            self.stars.append(Star(650, y, "red"))
            self.stars.append(Star(330, y))
            self.stars.append(Star(410, y))
            self.stars.append(Star(490, y))
            self.stars.append(Star(570, y))