from turtle import Turtle, Screen
from random import randint, choice


t = Turtle()
screen = Screen()

'''
#Draw square
for i in range(4):
    t.forward(100)
    t.rt(90)
'''

'''
#Draw dotted line
for i in range(20):
    t.pendown()
    t.forward(10)
    t.penup()
    t.forward(10)
'''

screen.colormode(255)

'''
#draw tri - 10 decagon in random color
for i in range(7):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    t.pencolor(r, g, b)
    sides = i + 3
    for s in range (sides):
        t.forward(100)
        t.rt(360 / sides)
'''


#random walk

def randColor():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    t.pencolor(r, g, b)

'''    
step = 20
steps = 200
t.speed(0)
t.pensize(10)
t.shape('circle')

directions = [0, 90, 180, 270]

for i in range(steps):
    randColor()
    t.setheading(choice(directions))
    t.forward(step)
'''

'''
#spirograph
circles = 75
t.speed(0)
t.hideturtle()
for i in range (circles):
    randColor()
    t.setheading((360 / circles) * i)
    t.circle(100)
'''

screen.exitonclick()
