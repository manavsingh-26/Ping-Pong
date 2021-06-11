from turtle import Turtle

class Bgdesign(Turtle):
    
    def __init__(self):
        super().__init__()
        self.incircle()
        self.outline()
        self.center_line()
        
    
    def incircle(self):
        
        self.hideturtle()
        self.shape("circle")
        self.pensize(10)
        self.penup()
        self.goto(0,-100)
        self.pendown()
        self.pencolor("saddle brown")
        self.circle(100)
        self.speed("fastest")
        
        
    def outline(self):
        
        self.hideturtle()
        self.speed("fastest")
        self.pensize(10)
        self.color("saddle brown")
        self.penup()
        self.goto(-400,296)
        self.pendown()
        self.forward(790)
        self.setheading(270)
        self.forward(585)
        self.setheading(180)
        self.forward(788)
        self.setheading(90)
        self.forward(590)
        
        
    def center_line(self):
        
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,-400)
        self.pensize(width=5)
        self.setheading(90)
        self.speed("fastest")
        while self.ycor()<400:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
            
                
                
                
                