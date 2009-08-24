from star import Star
from levelbase import LevelBase
import jngl

class Level(LevelBase):
    def __init__(self):
        LevelBase.__init__(self)
        self.stars = [Star(450, 420), Star(450, 360), Star(370, 360), Star(530, 360), Star(370, 280), Star(530, 280), Star(290, 280), Star(610, 280),
                      Star(290, 200), Star(610, 200),
                      Star(370, 200, "red"), Star(530, 200, "red"), Star(450, 280, "red"),
                      Star(370, 420, "red"), Star(530, 440, "red"), Star(610, 360, "red"), Star(290, 360, "red")]