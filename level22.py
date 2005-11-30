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
        for x in range(40, 650, 80):
            self.stars.append(Star(x, -300))
            self.stars.append(Star(x, -380, "green"))
        for x in range(40, 650, 80):
            self.stars.append(Star(x, -80, "green"))
            self.stars.append(Star(x, 0,))
        self.boxes = [Box(480, 280, 200, 30), Box(490, 60, 170, 30), Box(20, -170, 200, 30)]
        self.movingBox = self.boxes[1]
        self.moveLeft = True
    def step(self):
        if self.moveLeft:
            self.movingBox.xspeed = -1
        else:
            self.movingBox.xspeed = 1
        if self.movingBox.x > 500:
            self.moveLeft = True
        if self.movingBox.x < 50:
            self.moveLeft = False
    def drawHints(self):
        jngl.Print("Let's increase our score\nafter all this work!", 20, 220)