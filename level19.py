from star import Star
from levelbase import LevelBase
from box import Box
import jngl

class Level(LevelBase):
    def __init__(self):
        LevelBase.__init__(self)
        self.stars = []
        for y in range(-160, 450, 80):
            self.stars.append(Star(730, y, "red"))
        for x in range(380, 700, 80):
            self.stars.append(Star(x, -300))
            self.stars.append(Star(x, -380))
        self.boxes = [Box(350, 300, 300, 50), Box(10, 70, 200, 50), Box(280, -150, 380, 50)]