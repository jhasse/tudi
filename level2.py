from star import Star
from levelbase import LevelBase
import jngl

class Level(LevelBase):
    def __init__(self):
        LevelBase.__init__(self)
        self.stars = []
        for x in range(170, 770, 80):
            for y in range(250, 430, 80):
                self.stars.append(Star(x, y))
    def drawHints(self):
        jngl.Print("For each star you collect you'll get one point.", 155, 170)