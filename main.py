import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = t.Screen()
screen.bgcolor('black')
screen.setup(width = 800, height = 800)
screen.title('Pong Arcade Game')
#t.tracer() - this function is used to turn turtle animation on or off and set a delay for update drawings
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((350,0))
ball = Ball()
scoreboard = Scoreboard()

#t.listen() - set focus on TurtleScreen (in order to collect key-events)
screen.listen()
#player 1 controls
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(l_paddle.go_up, 'Down')
#player 2 controls
screen.onkey(r_paddle.go_up, 'w')
screen.onkey(l_paddle.go_up, 's')

paddle_game_is_on = True

while paddle_game_is_on:
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()