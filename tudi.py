import jngl

class Player:
    def __init__(self, game):
        self.windowWidth = game.windowWidth
        self.windowHeight = game.windowHeight
        self.yspeed = 0
        self.xspeed = 2.5
        self.size = 50
        self.x = -self.size / 2
        self.y = self.windowHeight - self.size * 5
    def move(self):
        if jngl.KeyDown(jngl.key.Right):
            self.xspeed += 0.2
        if jngl.KeyDown(jngl.key.Left):
            self.xspeed -= 0.2
        self.yspeed += 0.2
        self.xspeed *= 0.97
        self.x += self.xspeed
        self.y += self.yspeed
        if self.y + self.size / 2 > self.windowHeight:
            self.y = self.windowHeight - self.size / 2
            self.yspeed = -10
        if self.x - self.size / 2 < 0 and self.xspeed < 0:
            self.xspeed = -self.xspeed
            self.x = self.size / 2
    def draw(self):
        jngl.SetColor(255, 255, 255)
        width = self.size
        height = self.size
        height -= self.yspeed * 3
        width += self.yspeed * 0.8
        jngl.DrawRect(self.x - width / 2, self.y - height / 2,
                      width, height)

class Game:
    def __init__(self):
        self.levelNr = 14
        self.totalScore = 0
        self.level = None
        self.scaleFactor = 1
        self.windowWidth = 800
        self.windowHeight = 480
        jngl.ShowWindow("tudi", int(self.windowWidth * self.scaleFactor), int(self.windowHeight * self.scaleFactor))
        jngl.SetBackgroundColor(0, 0, 0)
        jngl.SetFont('victor-pixel.ttf')
        jngl.SetFontSize(16)
        jngl.SetFontColor(255, 255, 255)

        while not jngl.KeyPressed(jngl.key.Any) and jngl.Running():
            jngl.Scale(self.scaleFactor)
            #jngl.Draw("crap.png", 240, 100)
            text = "Press any key"
            jngl.Print(text, int(self.windowWidth / 2 - jngl.GetTextWidth(text) / 2), 400)
            jngl.SwapBuffers()

        self.loadNextLevel() # load level 1

    def getLevel(self):
        return self.level

    def loadNextLevel(self):
        if self.level != None:
            self.totalScore += self.level.getScore()
            if self.level.getScore() >= 0:
                self.levelNr += 1
        self.level = __import__('level{0}'.format(self.levelNr)).Level()
        self.player = Player(self)

    def run(self):
        lastTime = jngl.Time()
        needDraw = True
        timePerStep = 0.01
        while jngl.Running():
            if jngl.Time() - lastTime > timePerStep:
                lastTime += timePerStep
                needDraw = True
                self.player.move()
                self.level.checkStars(self.player)
                if self.player.x - self.player.size / 2 > self.windowWidth:
                    self.loadNextLevel()
                self.level.step()

            elif needDraw:
                needDraw = False

                jngl.Scale(self.scaleFactor)
                self.player.draw()
                self.level.drawStars()
                self.level.drawHints()

                jngl.Print("#{1}  Score: {0}".format(self.level.getScore(), self.levelNr), 10, 10)

                text = "Total Score: {0}".format(self.totalScore)
                jngl.Print(text, int(self.windowWidth - 10 - jngl.GetTextWidth(text)), 10)

                jngl.SwapBuffers()
            else:
                jngl.Sleep(1)

game = Game()
game.run()

jngl.HideWindow()
