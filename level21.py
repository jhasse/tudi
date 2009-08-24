from star import Star
from levelbase import LevelBase
from box import Box
import jngl

class Level(LevelBase):
    def __init__(self):
        LevelBase.__init__(self)
        self.stars = [ Star(720, 190), Star(60, -180), Star(300, -1000, "blue"), Star(380, -1000, "blue"), Star(460, -1000, "blue"),
                       Star(750, -510, "red")]
        self.boxes = [ Box(770, -400, 20, 860), Box(700, 240, 70, 20), Box(400, 5, 70, 20), Box(0, -120, 250, 20), Box(0, -320, 140, 20),
                       Box(100, -520, 600, 20), Box(100, -720, 600, 20), Box(770, -1500, 20, 920) ]