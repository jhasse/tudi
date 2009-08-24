from star import Star
from levelbase import LevelBase
import jngl

class Level(LevelBase):
    def __init__(self):
        LevelBase.__init__(self)
        self.stars = [Star(280, 190, "red"), Star(480, 190, "red"), Star(680, 190, "red")]
        for x in range(170, 770, 80):
            self.stars.append(Star(x, 400))