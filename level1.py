from star import Star
from levelbase import LevelBase
import jngl

class Level(LevelBase):
    def __init__(self):
        LevelBase.__init__(self)
        self.stars = []
    def drawHints(self):
        jngl.Print("Welcome to Tudi!\nUse the left and right arrow keys to move.", 10, 100)
        jngl.Print("GO -->", 680, 270)