from star import Star
from levelbase import LevelBase
import jngl

class Level(LevelBase):
    def __init__(self):
        LevelBase.__init__(self)
        self.stars = []
        for x in range(150, 500, 70):
            self.stars.append(Star(x, 170, "blue"))
            self.stars.append(Star(x, 240))
        for x in range(500, 750, 70):
            self.stars.append(Star(x, 170, "red"))
            self.stars.append(Star(x, 240, "red"))
        for x in range(150, 500, 70):
            self.stars.append(Star(x, 350, "red"))
            self.stars.append(Star(x, 420, "red"))
        for x in range(500, 750, 70):
            self.stars.append(Star(x, 350))
            self.stars.append(Star(x, 420, "blue"))