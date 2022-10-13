from turtle import Screen, Turtle
import time
from paddle import Paddle, LEFT, RIGHT
from scoreboard import Score, FONT, ALIGNMENT


s = Screen()
s.setup(width=800, height=600)
s.bgcolor("black")
s.title('Pong')
s.tracer(0)

paddleL = Paddle(LEFT)
#scoreL = Score('LEFT')
paddleR = Paddle(RIGHT)
#score

s.listen()
s.onkeypress(paddleR.up, 'Up')
s.onkeypress(paddleR.down, 'Down')

s.onkeypress(paddleL.up, 'w')
s.onkeypress(paddleL.down, 's')


gameIsOn = True
while gameIsOn:
    s.update()
    time.sleep(.01)







s.exitonclick()