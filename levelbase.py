class LevelBase:
    def __init__(self):
        self.score = 0
        self.stars = []
        self.boxes = []
    def getScore(self):
        return self.score
    def draw(self):
        for star in self.stars:
            star.draw()
        for box in self.boxes:
            box.draw()
    def drawHints(self):
        pass
    def checkStars(self, player):
        for star in self.stars:
            if star.checkCollision(player):
                self.score += star.score
                if self.score < 0:
                    player.explode()
                else:
                    star.explode()
        for star in self.stars:
            if star.dead:
                self.stars.remove(star)
    def checkCollision(self, player):
        for box in self.boxes:
            if box.checkCollision(player):
                return True
        return False
    def step(self):
        pass