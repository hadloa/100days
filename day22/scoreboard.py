from turtle import Turtle
FONT = ('Courier', 30, 'bold')
ALIGNMENT = 'center'

class Score(Turtle):
    def __init__(self, side):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color(side['color'])
        self.goto(side['posS'])
        self.updateScore()
        self.centerLine()


    def updateScore(self):
        self.write(f'{self.score}', align=ALIGNMENT, font=FONT)

    def point(self):
        self.score += 1
        self.clear()
        self.updateScore()


    def gameOver(self):
        self.goto(0, 0)
        self.write(f'Game Over', align=ALIGNMENT, font=FONT)


    def centerLine(self):
        line = Turtle()
        line.color('white')
        line.hideturtle()
        line.penup()
        line.speed('fastest')
        line.goto(0, 300)
        line.setheading(270)
        for dash in range(20):
            line.pendown()
            line.forward(15)
            line.penup()
            line.forward(15)

