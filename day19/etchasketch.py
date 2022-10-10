from turtle import Turtle, Screen
from random import randint, choice


t = Turtle()
s = Screen()


def rotateCW():
    h = t.heading()
    t.setheading(h + 10)


def moveForward():
    t.forward(10)


def rotateCCW():
    h = t.heading()
    t.setheading(h - 10)


def moveBackward():
    t.bk(10)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()




s.onkey(key='Up', fun=moveForward)
s.onkey(key='Down', fun=moveBackward)
s.onkey(key='Left', fun=rotateCW)
s.onkey(key='Right', fun=rotateCCW)
s.onkey(key='space', fun=clear)
s.listen()




s.exitonclick()