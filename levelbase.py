class LevelBase:
    def __init__(self):
        self.score = 0
        self.stars = []
    def getScore(self):
        return self.score
    def drawStars(self):
        for star in self.stars:
            star.draw()
    def drawHints(self):
        pass
    def checkStars(self, player):
        for star in self.stars:
            if star.checkCollision(player):
                self.score += star.score
                star.explode()
        for star in self.stars:
            if star.dead:
                self.stars.remove(star)
    def step(self):
        pass