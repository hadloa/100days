from turtle import Screen, Turtle
import time
from paddle import Paddle
from scoreboard import Score, FONT, ALIGNMENT


s = Screen()
s.setup(width=800, height=600)
LEFT = {'posP': (-375, 0), 'posS': (-150, 250), 'color': 'red3'}
RIGHT = {'posP': (375, 0), 'posS': (150, 250), 'color': 'navy'}

s.bgcolor("black")
s.title('Pong')
s.tracer(0)

paddleL = Paddle(LEFT)
#scoreL = Score('LEFT')
paddleR = Paddle(RIGHT)
#score

s.listen()
s.onkey(paddleR.up, 'Up')
s.onkey(paddleR.down, 'Down')

s.onkeypress(paddleL.up, 'w')
s.onkeypress(paddleL.down, 's')


gameIsOn = True
while gameIsOn:
    s.update()
    time.sleep(.01)







s.exitonclick()