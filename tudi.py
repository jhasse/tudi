import jngl
try:
    import jnal
except:
    import os
    os.system("oalinst.exe")
    import jnal
import os

class Player:
    def __init__(self, game):
        self.windowWidth = game.windowWidth
        self.windowHeight = game.windowHeight
        self.yspeed = 0
        self.xspeed = 2.5
        self.size = 50
        self.x = -self.size / 2
        self.y = self.windowHeight - self.size * 5
        self.exploding = False
        self.explodeTimeout = 50 # Fade in level
        self.dead = False
        self.canJump = False
        self.nonstopJump = True
    def move(self, game):
        if self.exploding:
            self.explodeTimeout += 1
            if self.explodeTimeout > 100:
                self.dead = True
        else:
            if self.explodeTimeout > 0:
                self.explodeTimeout -= 1 # Fade in
            if jngl.KeyDown(jngl.key.Right):
                self.xspeed += 0.2
            if jngl.KeyDown(jngl.key.Left):
                self.xspeed -= 0.2
            self.yspeed += 0.2
            self.xspeed *= 0.97

            self.x += self.xspeed
            if game.level.checkCollision(self):
                self.x -= self.xspeed
                self.xspeed = -self.xspeed

            self.y += self.yspeed
            if game.level.checkCollision(self):
                self.y -= self.yspeed
                if self.yspeed > 0:
                    self.jump(game)
                else:
                    self.yspeed = -self.yspeed
            else:
                self.canJump = False

            if self.y + self.size / 2 > self.windowHeight:
                self.y = self.windowHeight - self.size / 2
                self.jump(game)
            if self.x - self.size / 2 < 0 and self.xspeed < 0:
                self.xspeed = -self.xspeed
                self.x = self.size / 2
    def jump(self, game):
        if self.nonstopJump or (jngl.KeyDown(jngl.key.Up)):
            self.yspeed = -10
            game.moveCamera = self.windowHeight - self.y - 100
        else:
            self.canJump = True
            self.yspeed = 0
    def explode(self):
        jnal.Play("dead.ogg")
        self.exploding = True
    def draw(self):
        if self.exploding:
            if self.explodeTimeout > 50:
                # Fade out level
                jngl.SetColor(0, 0, 0, int((self.explodeTimeout - 50) * 5.1))
                jngl.PushMatrix()
                jngl.Reset()
                jngl.DrawRect(0, 0, jngl.GetWindowWidth(), jngl.GetWindowHeight())
                jngl.PopMatrix()
            jngl.SetColor(255, 255, 255)
            jngl.PushMatrix()
            jngl.Translate(self.x, self.y)
            width = self.size / 2 - self.explodeTimeout / 4
            height = self.size / 2 - self.explodeTimeout / 4
            distance = self.explodeTimeout / 2 + self.size / 4
            jngl.DrawRect(-width / 2 - distance, -height / 2 - distance, width, height)
            jngl.DrawRect(-width / 2 - distance, -height / 2 + distance, width, height)
            jngl.DrawRect(-width / 2 + distance, -height / 2 + distance, width, height)
            jngl.DrawRect(-width / 2 + distance, -height / 2 - distance, width, height)
            jngl.PopMatrix()
        else:
            if self.explodeTimeout != 0:
                # Fade in level
                jngl.SetColor(0, 0, 0, int(self.explodeTimeout * 5.1))
                jngl.DrawRect(0, 0, self.windowWidth, self.windowHeight)
            jngl.SetColor(255, 255, 255)
            width = self.size
            height = self.size
            height -= self.yspeed * 3
            width += self.yspeed * 0.8
            jngl.DrawRect(self.x - width / 2, self.y - height / 2,
                          width, height)

class Music:
    def __init__(self):
        self.playing = True
        self.songs = [ ("javagore", "Thornar"), ("deathstar", "jamendrock"), ("pornophonique", "sad robot") ]
        for song in self.songs:
            jnal.Load("music/{0}/{1}.ogg".format(song[0], song[1]))
        self.currentSong = -1
        self.drawTimeout = 0
    def step(self):
        song = self.songs[self.currentSong]
        if not jnal.IsPlaying("music/{0}/{1}.ogg".format(song[0], song[1])):
            self.next()
    def next(self):
        if self.playing:
            if self.currentSong >= 0:
                jnal.Stop("music/{0[0]}/{0[1]}.ogg".format(self.songs[self.currentSong]))
            self.currentSong += 1
            if self.currentSong >= len(self.songs):
                self.currentSong = 0
            song = self.songs[self.currentSong]
            jnal.Play("music/{0}/{1}.ogg".format(song[0], song[1]))
            self.drawTimeout = 555
    def draw(self):
        if self.drawTimeout > 0:
            self.drawTimeout -= 1
            jngl.SetFontColor(255, 255, 255)
            if self.drawTimeout > 300:
                jngl.SetFontColor(255, 255, 255, 555 - self.drawTimeout)
            if self.drawTimeout < 255:
                jngl.SetFontColor(255, 255, 255, self.drawTimeout)
            text = "Now playing: {0[1]} by {0[0]}".format(self.songs[self.currentSong])
            jngl.Print(text, 10, 455)
            jngl.SetFontColor(255, 255, 255)
    def togglePlaying(self):
        self.playing = not self.playing
        if self.playing:
            self.next()
        else:
            jnal.Stop("music/{0[0]}/{0[1]}.ogg".format(self.songs[self.currentSong]))

class Game:
    def __init__(self):
        self.version = "1.03"
        self.levelNr = 1
        self.totalScore = 0
        self.level = None
        self.scaleFactor = 1
        self.windowWidth = 800
        self.windowHeight = 480
        self.player = Player(self)
        jngl.ShowWindow("Tudi {0} - Copyright 2009 Jan Niklas Hasse - http://watteimdocht.de/tudi".format(self.version),
                        int(self.windowWidth * self.scaleFactor), int(self.windowHeight * self.scaleFactor))
        jngl.SetBackgroundColor(0, 0, 0)
        jngl.SetFont('victor-pixel.ttf')
        jngl.SetFontSize(16)
        jngl.SetFontColor(255, 255, 255)
        jngl.SetAntiAliasing(True)

        self.music = None

        while not jngl.KeyPressed(jngl.key.Any) and jngl.Running():
            jngl.Scale(self.scaleFactor)
            jngl.Draw("crap.png", 240, 100)
            if self.music == None:
                text = "Loading ..."
            else:
                text = "Press any key"
            jngl.Print(text, int(self.windowWidth / 2 - jngl.GetTextWidth(text) / 2), 400)
            jngl.SwapBuffers()
            if self.music == None:
                self.music = Music()
                jnal.Load("dead.ogg")
                jnal.Load("collect.ogg")

        self.highscore = 0
        if os.path.exists("highscore"):
            file = open("highscore")
            self.highscore = int(file.read(4))
            file.close()

        self.loadNextLevel() # load level 1

    def getLevel(self):
        return self.level

    def loadNextLevel(self):
        if self.level != None and self.level.getScore() >= 0:
            self.totalScore += self.level.getScore()
            self.levelNr += 1
        self.level = __import__('level{0}'.format(self.levelNr)).Level()
        temp = self.player.nonstopJump
        self.player = Player(self)
        self.player.nonstopJump = temp
        self.moveCamera = 0
        self.camera = 0

    def run(self):
        self.camera = 0
        lastTime = jngl.Time()
        needDraw = True
        timePerStep = 0.01
        counter = 0
        fps = 0
        while jngl.Running():
            if jngl.Time() - lastTime > timePerStep:
                lastTime += timePerStep
                needDraw = True
                self.music.step()
                self.player.move(self)
                self.level.checkStars(self.player)
                if self.player.x - self.player.size / 2 > self.windowWidth or self.player.dead:
                    self.loadNextLevel()
                self.level.step()
                if (self.player.y - self.windowHeight) + self.camera > 0:
                    newMoveCamera = self.windowHeight - self.player.y - 100
                    if newMoveCamera < self.moveCamera:
                        self.moveCamera = newMoveCamera
                if self.moveCamera < 0:
                    self.moveCamera = 0
                self.camera += (self.moveCamera - self.camera) / 30

                if jngl.KeyPressed('m'):
                    self.music.togglePlaying()
                if jngl.KeyPressed('j') and self.levelNr == 1:
                    self.player.nonstopJump = not self.player.nonstopJump
                if jngl.KeyPressed('r') and self.levelNr == 37:
                    self.levelNr = 0
                    self.loadNextLevel()

            elif needDraw:
                needDraw = False

                jngl.Scale(self.scaleFactor)
                jngl.PushMatrix()
                jngl.Translate(0, int(self.camera))
                self.level.draw()
                self.level.drawHints()
                self.player.draw()
                jngl.PopMatrix()

                jngl.Print("#{1}  Score: {0}".format(self.level.getScore(), self.levelNr), 10, 10)

                text = "Total Score: {0}".format(self.totalScore)
                jngl.Print(text, int(self.windowWidth - 10 - jngl.GetTextWidth(text)), 10)

                self.music.draw()

                if self.levelNr == 37:
                    if self.totalScore > self.highscore:
                        self.highscore = self.totalScore
                        file = open("highscore", "w")
                        file.write(str(self.highscore))
                        file.close()

                    jngl.Print("Your Highscore:\n{0: >4}".format(self.highscore), 580, 405)

                fps += jngl.FPS() / 50
                counter -= 1
                if counter < 0:
                    counter = 50
                    jngl.SetTitle("Tudi {0} - Highscore: {1} - FPS: {2}".format(self.version, self.highscore, int(fps)))
                    fps = 0

                jngl.SwapBuffers()
            else:
                jngl.Sleep(1)

game = Game()
game.run()
