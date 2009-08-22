from star import Star
from levelbase import LevelBase
import jngl

class Level(LevelBase):
    def __init__(self):
        LevelBase.__init__(self)
        self.stars = [Star(300, 300, "red"), Star(220, 400), Star(300, 400, "red"), Star(390, 400),
		              Star(550, 300, "red"), Star(470, 400), Star(550, 400, "red"), Star(640, 400),]
    def drawHints(self):
        jngl.Print("Don't touch red stars!", 280, 150)