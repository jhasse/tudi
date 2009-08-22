from star import Star
from levelbase import LevelBase
import jngl

class Level(LevelBase):
    def __init__(self):
        LevelBase.__init__(self)
        self.stars = []
        for x in range(170, 770, 320):
            self.stars.append(Star(x, 410))
            self.stars.append(Star(x + 160, 400, "red"))
        for x in range(170, 770, 160):
            self.stars.append(Star(x, 190, "red"))
    def drawHints(self):
        jngl.Print("When your total score drops under 0 you loose.", 170, 110)