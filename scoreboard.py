from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.hideturtle()
        self.penup()
        self.lscore = 0
        self.rscore = 0
        self.score_update()
    
    
    def score_update(self):
        
        self.clear()
        self.goto(-150,180)
        self.write(self.lscore,align="center",font=("Courier",75,"normal"))
        self.goto(150,180)
        self.write(self.rscore,align="center",font=("Courier",75,"normal"))
    
    
    def l_score_update(self):
        
        self.lscore +=1
        self.score_update()
        
    
    def r_score_update(self):
        
        self.rscore +=1
        self.score_update()
        
        
        