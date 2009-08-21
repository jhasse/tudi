from star import Star
from levelbase import LevelBase
import jngl
import math

class Level(LevelBase):
    def __init__(self):
        LevelBase.__init__(self)
        self.stars = []
        self.centerX = 450
        self.centerY = 220
        i = 0
        while i < math.pi * 2:
            self.stars.append(Star(self.centerX + 200 * math.sin(i),
                                   self.centerY + 200 * math.cos(i)))
            i += math.pi / 6
            self.stars.append(Star(self.centerX + 200 * math.sin(i),
                                   self.centerY + 200 * math.cos(i), "blue"))
            i += math.pi / 6
            self.stars.append(Star(self.centerX + 200 * math.sin(i),
                                   self.centerY + 200 * math.cos(i), "red"))
            i += math.pi / 6
    def drawHints(self):
        jngl.Print("You know what to do.", 310, 210)
    def step(self):
        for star in self.stars:
            x = star.x - self.centerX
            y = star.y - self.centerY
            star.x = x * math.cos(0.01) - y * math.sin(0.01) + self.centerX
            star.y = y * math.cos(0.01) + x * math.sin(0.01) + self.centerY