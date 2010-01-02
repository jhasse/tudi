from star import Star
from levelbase import LevelBase
from box import Box
import jngl

class Level(LevelBase):
    def __init__(self):
        LevelBase.__init__(self)
        self.stars = []
        for x in range(240, 650, 80):
            self.stars.append(Star(x, -500))
            self.stars.append(Star(x, -580, "green"))
        for x in range(240, 650, 80):
            self.stars.append(Star(x, 0, "red"))
            self.stars.append(Star(x, -80, "red"))
            self.stars.append(Star(x, -160, "red"))
            self.stars.append(Star(x, -240, "red"))
        self.boxes = [Box(80, 60, 100, 30), Box(300, -320, 100, 30), Box(80, -170, 100, 30),Box(80, 280, 100, 30), Box(500, 50, 30, 430) ]
        self.movingBoxes = self.boxes[:2]
        self.moveLeft = True
    def step(self):
        for box in self.movingBoxes:
            if self.moveLeft:
                box.xspeed = -1
            else:
                box.xspeed = 1
            if box.x > 500:
                self.moveLeft = True
            if box.x < 50:
                self.moveLeft = False