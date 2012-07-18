import jngl

class Box:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.xspeed = 0
        self.yspeed = 0
        self.width = width
        self.height = height
    def draw(self):
        jngl.setColor(200, 200, 200)
        jngl.drawRect(self.x, self.y, self.width, self.height)
    def checkCollision(self, player):
        self.x += self.xspeed
        self.y += self.yspeed
        left1 = self.x
        left2 = player.x - player.size / 2
        right1 = self.x + self.width
        right2 = player.x + player.size / 2
        top1 = self.y
        top2 = player.y - player.size / 2
        bottom1 = self.y + self.height
        bottom2 = player.y + player.size / 2

        if left1 > right2:
            return False
        if left2 > right1:
            return False
        if top1 > bottom2:
            return False
        if top2 > bottom1:
            return False
        return True