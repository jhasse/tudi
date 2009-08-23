from star import Star
from levelbase import LevelBase
from box import Box
import jngl

class Level(LevelBase):
    def __init__(self):
        LevelBase.__init__(self)
        self.stars = []
        for y in range(160, 450, 80):
            self.stars.append(Star(730, y, "red"))
        for x in range(380, 700, 80):
            self.stars.append(Star(x, 100))
            self.stars.append(Star(x, 180))
        self.boxes = [Box(280, 250, 380, 50)]
    def drawHints(self):
        jngl.Print("Jump onto this box.", 350, 320)
        jngl.Print("Well done!", 400, -50)