from star import Star
from levelbase import LevelBase
import jngl

class MovingStarH(Star):
	def __init__(self, x, y):
		Star.__init__(self, x, y, "red")
		self.moveleft = True

class MovingStarV(Star):
	def __init__(self, x, y):
		Star.__init__(self, x, y, "red")
		self.moveup = True

class Level(LevelBase):
    def __init__(self):
        LevelBase.__init__(self)
        self.stars = [MovingStarH(250, 200), MovingStarH(750, 440), MovingStarV(190, 190), MovingStarV(485, 400)]
        for x in range(310, 750, 70):
            if x != 450 and x != 520:
                self.stars.append(Star(x, 280))
                self.stars.append(Star(x, 360))
        self.movingStarsH = self.stars[:2]
        self.movingStarsV = self.stars[2:4]
    def step(self):
        for star in self.movingStarsH:
            if star.moveleft:
                star.x -= 1
            else:
                star.x += 1
            if star.x > 750:
                star.moveleft = True
            if star.x < 250:
                star.moveleft = False
        for star in self.movingStarsV:
            if star.moveup:
                star.y -= 1
            else:
                star.y += 1
            if star.y < 190:
                star.moveup = False
            if star.y > 400:
                star.moveup = True