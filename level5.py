from star import Star
from levelbase import LevelBase
import jngl

class Level(LevelBase):
    def __init__(self):
        LevelBase.__init__(self)
        self.stars = []
        for y in range(250, 450, 80):
            self.stars.append(Star(200, y, "blue"))
            self.stars.append(Star(280, y, "blue"))
            self.stars.append(Star(500, y, "red"))
            self.stars.append(Star(580, y, "red"))
    def drawHints(self):
        jngl.print("<-- Your points collected\n    in this level", 195, 10)
        jngl.print("If you have at least 10 points left\nyou can afford to touch a red star.", 155, 135)