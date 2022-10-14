from turtle import Turtle
import random
import time

MOVE = 20
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color('white')
        self.speed('fastest')


    def bounceR(self):

        pass
    def start(self):
        self.goto(0,0)
        self.setheading(random.randint(0,359))
        time.sleep(2)

    def move(self):
        self.forward(MOVE)