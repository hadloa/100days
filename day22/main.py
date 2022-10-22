from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Score, FONT, ALIGNMENT


s = Screen()
s.setup(width=800, height=600)
LEFT = {'posP': (-375, 0), 'posS': (-150, 250), 'color': 'red3'}
RIGHT = {'posP': (375, 0), 'posS': (150, 250), 'color': 'navy'}

s.bgcolor("black")
s.title('Pong')
s.tracer(0)

paddleL = Paddle(LEFT)
paddleR = Paddle(RIGHT)
ball = Ball()

s.listen()
s.onkey(paddleR.up, 'Up')
s.onkey(paddleR.down, 'Down')

s.onkeypress(paddleL.up, 'w')
s.onkeypress(paddleL.down, 's')


ball.start()

gameIsOn = True
while gameIsOn:
    s.update()
    ball.move()
    ball.bounce_wall()
    ball.bounce_paddle(paddleL, paddleR)
    time.sleep(.1)

    if ball.xcor() > 420 or ball.xcor() < -420:
        ball.start()
        time.sleep(3)





s.exitonclick()