#!/usr/bin/env python
# coding: utf-8

# In[4]:


import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = t.Screen()
#t.screen() - set or return background color of the TurtleScreen
screen.bgcolor('black')
#t.setup() - set the size and position of the main window
screen.setup(width = 800, height = 800)
#t.title() - set title of turtle window to titlestring
screen.title('Pong Arcade Game')
#t.tracer() - this function is used to turn turtle animation on or off and set a delay for update drawings
screen.tracer(0)

#user 1
r_paddle = Paddle((350,0))
#user 2
l_paddle = Paddle((350,0))
ball = Ball()
scoreboard = Scoreboard()

#t.listen() - set focus on TurtleScreen (in order to collect key-events)
screen.listen()
#user 1 - controls
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(l_paddle.go_up, 'Down')
#user 2 - controls 
screen.onkey(r_paddle.go_up, 'w')
screen.onkey(l_paddle.go_up, 's')

paddle_game_is_on = True

while paddle_game_is_on:
    screen.update()
    ball.move()
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.y_bounce()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 300 or ball.distance(l_paddle) < 50 and ball.xcor() < -300:
        ball.x_bounce()
    #r paddle
    if ball.xcor() > 375:
        ball.reset_position()
        scoreboard.l_point()
    #l paddle
    if ball.xcor() < -370:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()


# In[ ]:




