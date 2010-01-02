from star import Star
from levelbase import LevelBase
import math

class Level(LevelBase):
    def __init__(self):
        LevelBase.__init__(self)
        self.stars = []
        self.centerX = 650
        self.centerY = 230
        cnt = 0
        i = 0
        while i < math.pi * 2:
            self.stars.append(Star(self.centerX + 200 * math.sin(i),
                                   self.centerY + 200 * math.cos(i)))
            i += math.pi / 6
            self.stars.append(Star(self.centerX + 200 * math.sin(i),
                                   self.centerY + 200 * math.cos(i), "red"))
            i += math.pi / 6
            cnt += 1
            if cnt == 2 or cnt == 4:
                self.stars.append(Star(self.centerX + 200 * math.sin(i),
                                       self.centerY + 200 * math.cos(i)))
            elif cnt == 1:
                self.stars.append(Star(self.centerX + 200 * math.sin(i),
                                       self.centerY + 200 * math.cos(i), "green"))
            else:
                self.stars.append(Star(self.centerX + 200 * math.sin(i),
                                       self.centerY + 200 * math.cos(i), "red"))
            i += math.pi / 6
        self.stars1 = self.stars[::]
        self.centerX = 450
        self.centerY = 220
        i = 0
        while i < math.pi * 2:
            self.stars.append(Star(self.centerX + 200 * math.sin(i),
                                   self.centerY + 200 * math.cos(i), "red"))
            i += math.pi / 6
            self.stars.append(Star(self.centerX + 200 * math.sin(i),
                                   self.centerY + 200 * math.cos(i), "red"))
            i += math.pi / 6
            self.stars.append(Star(self.centerX + 200 * math.sin(i),
                                   self.centerY + 200 * math.cos(i), "green"))
            i += math.pi / 6
        self.stars2 = self.stars[len(self.stars1)::]
    def step(self):
        for star in self.stars1:
            x = star.x - self.centerX
            y = star.y - self.centerY
            star.x = x * math.cos(0.01) - y * math.sin(0.01) + self.centerX
            star.y = y * math.cos(0.01) + x * math.sin(0.01) + self.centerY
        for star in self.stars2:
            x = star.x - self.centerX
            y = star.y - self.centerY
            star.x = x * math.cos(-0.01) - y * math.sin(-0.01) + self.centerX
            star.y = y * math.cos(-0.01) + x * math.sin(-0.01) + self.centerY