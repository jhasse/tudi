import jngl

class Star:
    def __init__(self, x, y, color = "yellow"):
        self.size = 50
        self.x = x
        self.y = y
        self.score = 1
        self.red = 255
        self.green = 255
        self.blue = 0
        if color == "blue":
            self.score = 10
            self.red = 0
            self.green = 0
            self.blue = 255
        if color == "red":
            self.score = -10
            self.red = 255
            self.green = 0
            self.blue = 0
        self.exploding = False
        self.dead = False
        self.explodeTimeout = 0
    def explode(self):
        self.exploding = True
    def draw(self):
        flash = int(jngl.Time() * 300 % 200)
        if flash > 100:
            flash = 200 - flash
        red = self.red + flash
        green = self.green + flash
        blue = self.blue + flash
        if red > 255:
            red = 255
        if blue > 255:
            blue = 255
        if green > 255:
            green = 255

        width = self.size
        height = self.size
        jngl.PushMatrix()
        jngl.Translate(self.x, self.y)
        if self.exploding:
            jngl.SetColor(red, green, blue, 255 - self.explodeTimeout)
            width -= self.explodeTimeout / 2
            height -= self.explodeTimeout / 2
            distance = self.explodeTimeout / 3
            jngl.DrawRect(-width / 6 - distance, -height / 6 - distance, width / 3, height / 3)
            jngl.DrawRect(-width / 6 - distance, -height / 6 + distance, width / 3, height / 3)
            jngl.DrawRect(-width / 6 + distance, -height / 6 + distance, width / 3, height / 3)
            jngl.DrawRect(-width / 6 + distance, -height / 6 - distance, width / 3, height / 3)
            jngl.SetFontColor(255, 255, 255, int(255 - self.explodeTimeout * 2.55))
            jngl.Print("{0:+}".format(self.score), -20, int(-15 - self.explodeTimeout / 5))
            jngl.SetFontColor(255, 255, 255, 255)
        else:
            jngl.SetColor(255, 255, 255)
            jngl.PushMatrix()
            jngl.Rotate(jngl.Time() * 50 % 360)
            jngl.DrawRect(-width / 2, -height / 2, width, height)
            jngl.PopMatrix()

            jngl.SetColor(red, green, blue)
            jngl.PushMatrix()
            jngl.Rotate(-jngl.Time() * 50 % 360)
            jngl.DrawRect(-width / 2, -height / 2, width, height)
            jngl.PopMatrix()
        jngl.PopMatrix()
    def checkCollision(self, player):
        if self.exploding:
            self.explodeTimeout += 1
            if self.explodeTimeout >= 100:
                self.dead = True
            return False
        if (player.x - self.x) * (player.x - self.x) + (player.y - self.y) * (player.y - self.y) < (self.size + player.size) / 2 * (self.size + player.size) / 2 and not player.exploding:
            return True
        return False

if __name__ == "__main__":
    import splom