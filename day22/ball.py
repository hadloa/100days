from turtle import Turtle
import random
import time

SPEED_INIT = 20
START_POS = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 160, 165, 170, 175, 180, 185, 190, 195, 200]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.speed('fastest')

    @staticmethod
    def bounce_coef():
        return random.uniform(.9, 1.1)

    def bounce_wall(self):
        if self.ycor() > 280:
            self.setheading(-self.heading() * self.bounce_coef())
        elif self.ycor() < -270:
            self.setheading((360 - self.heading()) * self.bounce_coef())

    def bounce_paddle(self, paddleL, paddleR):
        paddles = [paddleL, paddleR]

        for paddle in paddles:
            x_marker = abs(self.xcor() - paddle.xcor()) < 20
            y_marker = abs(self.ycor() - paddle.ycor()) < 50
            if x_marker and y_marker:
                self.setheading((180 - self.heading()) * self.bounce_coef())

    def start(self):
        self.goto(0, 0)
        self.setheading(random.choice(START_POS))

    def move(self, modifier):
        self.forward(SPEED_INIT * modifier)
