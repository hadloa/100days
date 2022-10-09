from turtle import Turtle, Screen
from random import randint, choice
import colorgram
from math import ceil

colors = colorgram.extract('painting2.jpg', 30)

t = Turtle()
t.speed(0)
t.penup()
t.hideturtle()

screen = Screen()
screen.colormode(255)


def paletteColorRGB(palette):
    rgb = choice(colors).rgb
    return int(rgb[0]), int(rgb[1]), int(rgb[2])


space = 60
dotD = 60
screenW = 1010
screenH = 850
dotsC = (screenH - space) / (space + dotD)
dotsR = (screenW - space) / (space + dotD)


for row in range(int(ceil(dotsR))):
    t.setx(-screenW/2 + space + (space + dotD) * row)
    for column in range(int(ceil(dotsC))):
        t.color(paletteColorRGB(colors))
        t.sety(screenH/2 - space - (space + dotD) * column)
        t.dot(dotD)


screen.exitonclick()
