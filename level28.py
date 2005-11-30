from star import Star
from levelbase import LevelBase
from box import Box
import jngl

class Level(LevelBase):
    def __init__(self):
        LevelBase.__init__(self)
        self.stars = [Star(170,190,"blue"), Star(170, 270, "red"), Star(170, 350, "red"), Star(170, 430, "red"),
                      Star(460, 350, "red"), Star(460, 430, "red"), Star(540, 350, "red"), Star(540, 430, "red"),
                      Star(380, 350, "green"), Star(380, 430, "green")]
        self.boxes = [Box(290, 245, 280, 30)]
        for y in range(-200, 300, 80):
            self.stars.append(Star(720, y, "red"))
        for x in range(320, 650, 80):
            self.stars.append(Star(x, 160))