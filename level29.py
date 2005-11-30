from star import Star
from levelbase import LevelBase
import jngl

class Level(LevelBase):
    def __init__(self):
        LevelBase.__init__(self)
        self.stars = [Star(100, 200, "red"  ), Star(200, 200, "red"  ), Star(300, 200, "blue" ), Star(400, 200, "red"  ), Star(500, 200, "red"  ), Star(600, 200, "red"  ), Star(700, 200, ),
                      Star(100, 300, "red"  ), Star(200, 300, "green"), Star(300, 300, "red"  ), Star(400, 300, "green"), Star(500, 300, "red"  ), Star(600, 300, "red"  ), Star(700, 300, "red"  ),
                      Star(100, 400, "green"), Star(200, 400, "red"  ), Star(300, 400, "green"), Star(400, 400, "red"  ), Star(500, 400, "blue" ), Star(600, 400, "red"  ), Star(700, 400, "red"  )]
        for star in self.stars:
            star.x += 30