from star import Star
from levelbase import LevelBase
import jngl

class Level(LevelBase):
    def __init__(self):
        LevelBase.__init__(self)
        self.stars = []
        for x in range(170, 770, 320):
            self.stars.append(Star(x, 250))
            self.stars.append(Star(x + 160, 250, "blue"))
        for x in range(170, 770, 160):
            self.stars.append(Star(x, 400, "red"))
    def drawHints(self):
        jngl.Print("Be careful. You can't proceed to the next\nlevel with a negative score.", 180, 170)