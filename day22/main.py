from turtle import Screen, Turtle
import time, math
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
s.update()
s.tracer(n=1)

time_start = time.time()
gameIsOn = True
while gameIsOn:

    ball.move(math.trunc((time.time() - time_start)/30)/2 + 1)
    ball.bounce_wall()
    ball.bounce_paddle(paddleL, paddleR)
    time.sleep(.1)

    if ball.xcor() > 420 or ball.xcor() < -420:
        if ball.xcor() >420:
            paddleL.score.point()
        else:
            paddleR.score.point()
        ball.start()
        paddleR.reset(RIGHT['posP'])
        paddleL.reset(LEFT['posP'])
        time.sleep(1)





s.exitonclick()