from star import Star
from levelbase import LevelBase
import jngl

class Level(LevelBase):
    def __init__(self):
        LevelBase.__init__(self)
        for y in range(200, 450, 80):
            self.stars.append(Star(500, y, "red"))
    def drawHints(self):
        jngl.Print("Congratulation! You've made it through all levels!\nWhat's your Total Score? Compare it to the table below.\nPress R to restart.\nTip: Press J in Level 1!", 10, 100)
        jngl.Print("Scores Table\n1000 - Maximum\n>900 - Very good\n>800 - Good\n>700 - Okay\n>600 - Average\n<600 - Noob\n<200 - Nice one!", 580, 200)
        jngl.Print("Thank you for playing Tudi!", 90, 430)