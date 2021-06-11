import turtle as t

class Paddle(t.Turtle):
    
    
    def __init__(self,pos):
        super().__init__()
        self.color("red")
        self.shape("square")
        self.setheading(90)
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.penup()
        self.goto(pos)
        
        
        
    
    def up(self):
        if self.ycor()<245 :
            self.forward(30)
        
    def down(self):
        if self.ycor()>-230 :
            self.backward(30)
   