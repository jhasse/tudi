from star import Star
from levelbase import LevelBase
from box import Box
import jngl

class Level(LevelBase):
    def __init__(self):
        LevelBase.__init__(self)
        self.stars = [Star(50, -75, "blue")]
        for x in range(240, 650, 80):
            self.stars.append(Star(x, -500))
        for x in range(240, 650, 80):
            self.stars.append(Star(x, -280, "red"))
        for y in range(-160, 50, 80):
            self.stars.append(Star(470, y, "red"))
        self.boxes = [Box(80, -350, 20, 40), Box(300, -350, 20, 40), Box(0, -30, 110, 30), Box(50, 280, 80, 30), Box(400, 50, 30, 430), Box(0, -150, 100, 30) ]
        self.movingBoxes = self.boxes[:2]
        self.moveLeft = True
        for x in range(500, 750, 80):
            for y in range(260, 430, 80):
                self.stars.append(Star(x, y, "blue"))
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
    def drawHints(self):
        jngl.print("Last level!", 170, 285)