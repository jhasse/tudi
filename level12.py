from star import Star
from levelbase import LevelBase
import jngl

class Level(LevelBase):
    def __init__(self):
        LevelBase.__init__(self)
        self.stars = [Star(350, 200, "red"), Star(550, 200, "red"), Star(750, 200, "red")]
        for y in range(170, 440, 70):
            self.stars.append(Star(150, y))
            self.stars.append(Star(250, y))
            self.stars.append(Star(450, y))
            self.stars.append(Star(650, y))
        self.moveup = False
        self.movingStars = self.stars[:3]
    def step(self):
        for star in self.movingStars:
            if self.moveup:
                star.y -= 1
            else:
                star.y += 1
            if star.y > 390:
                self.moveup = True
            if star.y < 170:
                self.moveup = False