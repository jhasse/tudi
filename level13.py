from star import Star
from levelbase import LevelBase
import jngl

class MovingStar(Star):
	def __init__(self, x, y, color):
		Star.__init__(self, x, y, color)
		self.moveleft = True

class Level(LevelBase):
    def __init__(self):
        LevelBase.__init__(self)
        self.stars = [MovingStar(170, 200, "red"), MovingStar(750, 440, "red")]
        for x in range(170, 750, 70):
            self.stars.append(Star(x, 280))
            self.stars.append(Star(x, 360))
        self.movingStars = self.stars[:2]
    def step(self):
        for star in self.movingStars:
            if star.moveleft:
                star.x -= 1
            else:
                star.x += 1
            if star.x > 750:
                star.moveleft = True
            if star.x < 170:
                star.moveleft = False