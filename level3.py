from star import Star
from levelbase import LevelBase
import jngl

class Level(LevelBase):
    def __init__(self):
        LevelBase.__init__(self)
        self.stars = []
        for x in range(170, 770, 160):
            for y in range(250, 430, 160):
                self.stars.append(Star(x, y, "blue"))
    def drawHints(self):
        jngl.Print("Blue stars are worth 10 points.", 180, 170)