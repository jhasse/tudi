from star import Star
from levelbase import LevelBase
import jngl

class Level(LevelBase):
    def __init__(self):
        LevelBase.__init__(self)
        self.stars = []
        for x in range(170, 770, 320):
            self.stars.append(Star(x, 400))
            self.stars.append(Star(x + 160, 400, "blue"))
        for x in range(170, 770, 160):
            self.stars.append(Star(x, 200, "red"))
        for y in range(200, 401, 100):
            self.stars.append(Star(750, y, "red"))