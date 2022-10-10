from turtle import Screen, Turtle
from random import randint

screenW = 800
screenH = 400

s = Screen()
s.setup(width=screenW, height=screenH)

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

spaceV = 50
spaceH = 20
spacing = (screenH - spaceV) / len(colors)
finishLine = screenW/2 - 100

turtles = []
for i in range(6):
    turt = Turtle(shape='turtle')
    turtles.append(turt)
    turt.penup()
    turt.color(colors[i])
    x = - screenW / 2 + spaceH
    y = screenH / 2 - spaceV - spacing * i
    turt.goto(x=x, y=y)

tFinish = Turtle()
tFinish.hideturtle()
tFinish.penup()
tFinish.goto(x=finishLine, y=(screenH / 2))
tFinish.pendown()
tFinish.sety(y=(-screenH / 2))

user_bet = 0
while True:
    user_bet = s.textinput(title='Make your bet',
                           prompt='Which turtle will win the race? Enter a color: ').strip().lower()
    if user_bet in colors:
        break

racing = True
order = []
while racing:
    behind = 0
    for turt in turtles:
        if turt.xcor() >= finishLine and turt not in order:
            order.append(turt)
        elif turt.xcor() < finishLine:
            turt.forward(randint(1, 10))
            behind += 1
    if behind == 0:
        racing = False

for turt, i in zip(order, range(len(order))):
    print(f'{turt.color()[0].capitalize()} came in {i + 1} place!')

if order[0].color()[0] == user_bet:
    print("You won!")
else:
    print('You Lost')

s.exitonclick()
