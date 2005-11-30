from star import Star
from levelbase import LevelBase
import jngl

class Level(LevelBase):
    def __init__(self):
        LevelBase.__init__(self)
        self.stars = [Star(100, 200, "green"  ), Star(200, 200, "red"  ), Star(300, 200, "green" ), Star(400, 200, "red"  ), Star(500, 200, "red"  ), Star(600, 200, "red"  ), Star(700, 200, "green"),
                      Star(100, 300, "green"  ), Star(200, 300, "green"),
                      Star(100, 400, "green"), Star(200, 400, "red"  ), Star(300, 400, "green"), Star(400, 400, "red"  ), Star(500, 400, "red" ), Star(600, 400, "red"  ), Star(700, 400, "red"  )]
        for star in self.stars:
            star.x += 30
    def drawHints(self):
        jngl.Print("Green Stars are worth 5 points.", 310, 290)