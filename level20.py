from star import Star
from levelbase import LevelBase
from box import Box
import jngl

class Level(LevelBase):
    def __init__(self):
        LevelBase.__init__(self)
        self.stars = []
        for y in range(-360, 450, 80):
            self.stars.append(Star(730, y, "red"))
        for x in range(40, 300, 80):
            self.stars.append(Star(x, -300, "blue"))
            self.stars.append(Star(x, -380))
        self.boxes = [Box(280, 280, 250, 30), Box(490, 60, 170, 30), Box(20, -150, 200, 30)]