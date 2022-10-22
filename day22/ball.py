from turtle import Turtle
import random
import time

MOVE = 40

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color('white')
        self.speed('fastest')


    def bounce_coef(self):
       return random.uniform(.8, 1.2)
    def bounce_wall(self):
        if self.ycor() > 280:
            self.setheading(-self.heading() * self.bounce_coef())
        elif self.ycor() < -270:
            self.setheading((360 - self.heading()) * self.bounce_coef())
    def bounce_paddle(self, paddleL, paddleR):
        paddles = [paddleL, paddleR]

        quadUR = self.heading() > 90 and self.heading() < 180
        quadUL = self.heading() > 0 and self.heading() < 90

        for paddle in paddles:
            x_marker = abs(self.xcor() - paddle.xcor()) < 10
            y_marker = abs(self.ycor() - paddle.ycor()) < 40
            if x_marker and y_marker:
                if quadUL or quadUL:
                    paddle.setheading(180 - paddle.heading() * self.bounce_coef())
                else:
                    pass

    def start(self):
        self.goto(0,0)
        self.setheading(random.randint(0,359))



    def move(self):
        self.forward(MOVE)