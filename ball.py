import turtle as t
import random

choice = [10,-10]

class Ball(t.Turtle):
    
    
    def __init__(self):
        
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.penup()
        self.xmove = random.choice(choice)
        self.ymove = random.choice(choice)
        self.move_speed = 0.08
    
    def move(self):
        
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x,new_y)
        
        
    def bounce_y(self):
        
        self.ymove *= -1
        
        
    
    
    def bounce_x(self):
        
        self.xmove *= -1
        if self.xcor()>0:
            self.goto(self.xcor()-20,self.ycor())
        else:
            self.goto(self.xcor()+20,self.ycor())
        self.move_speed*=0.9
    
    
    def reset_pos(self):
        
        self.goto(0,0)
        self.xmove *=-1
        self.move_speed = 0.08
        
        
        
        





    
    