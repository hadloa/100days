import time
import turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.setheading(90)
        self.penup()
        self.reset_pos()

    def up(self):
        if self.ycor() < 280:
            self.forward(MOVE_DISTANCE)

    def reset_pos(self):
        self.goto(STARTING_POSITION)



