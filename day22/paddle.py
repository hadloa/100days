from turtle import Turtle
from scoreboard import Score

MOVE_DISTANCE = 20
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        #self.side = side
        score = Score(side)
        self.shape('square')
        self.color(side['color'])
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.setheading(90)
        self.penup()
        self.goto(side['posP'])
        self.kPress = False


    def up(self):
        if self.ycor() < 260:
            self.forward(MOVE_DISTANCE)

    def down(self):
        if self.ycor() > -260:
            self.backward(MOVE_DISTANCE)

    def stop(self):
        self.kPress = False

    def hit(self):
        pass
