from star import Star
from levelbase import LevelBase
import jngl

class MovingStar(Star):
    def __init__(self, x, y, toX, toY):
        Star.__init__(self, x, y, "red")
        self.xspeed = 0
        self.yspeed = 0
        self.fromX = x
        self.fromY = y
        self.toX = toX
        self.toY = toY
        if self.toX > self.fromX:
            self.xspeed = -1
        if self.toX < self.fromX:
            self.xspeed = 1
        if self.toY > self.fromY:
            self.yspeed = -1
        if self.toY < self.fromY:
            self.yspeed = 1
    def step(self):
        if self.x == self.toX or self.x == self.fromX:
            self.xspeed = -self.xspeed
        if self.y == self.toY or self.y == self.fromY:
            self.yspeed = -self.yspeed
        self.x += self.xspeed
        self.y += self.yspeed

class Level(LevelBase):
    def __init__(self):
        LevelBase.__init__(self)
        for x in range(170, 750, 70):
            if x != 450 and x != 520:
                self.stars.append(Star(x, 280))
                self.stars.append(Star(x, 360))
        self.stars += [MovingStar(250, 200, 400, 400), MovingStar(750, 440, 500, 300), MovingStar(485, 200, 485, 400)]
        self.movingStars = self.stars[-3:]
    def step(self):
        for star in self.movingStars:
            star.step()