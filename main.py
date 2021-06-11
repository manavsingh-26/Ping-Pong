import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from bgdesign import Bgdesign
import time

screen = t.Screen()
screen.setup(width =800,height = 600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)


bgdesign = Bgdesign()

    

RPOS=(350,0)
LPOS=(-350,0)

paddle_r = Paddle(RPOS)
paddle_l = Paddle(LPOS)

ball = Ball()

scoreboard = Scoreboard()


screen.listen()

screen.onkeypress(paddle_r.up,"Up")
screen.onkeypress(paddle_r.down,"Down")

screen.onkeypress(paddle_l.up,"w")
screen.onkeypress(paddle_l.down,"s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    #Detect collision with wall
    
    if ball.ycor() > 270 or ball.ycor() <-270:
        #ball bounce
        ball.bounce_y()
    
    #collision with paddle
    if ball.distance(paddle_r)<50 and ball.xcor()> 330:
        
        ball.bounce_x()
    
    if ball.distance(paddle_l)<50 and ball.xcor()< -330:
        
        ball.bounce_x()
        
    #If Right Paddle misses
    
    if ball.xcor()>380:
        ball.reset_pos()
        scoreboard.l_score_update()
    
    #If Left Paddle misses
    
    if ball.xcor()<-380:
        ball.reset_pos()
        scoreboard.r_score_update()
    
   
    
        
    
    
    





screen.exitonclick()
t.bye()