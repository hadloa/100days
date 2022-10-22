import turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.color('black')
        self.goto(-280, 265)
        self.updateScore()
        self.lanes()

    def updateScore(self):
        self.write(f'Level: {self.score}', font=FONT)

    def point(self):
        self.score += 1
        self.clear()
        self.updateScore()

    def gameOver(self):
        self.goto(0, 0)
        self.write(f'Game Over', font=("Courier", 36, "bold"), align='center')

    @staticmethod
    def lanes():
        line = turtle.Turtle()
        line.hideturtle()
        line.penup()
        line.setheading(180)
        xPos = 300
        yPos = 250
        for lane in range(25):
            line.goto(xPos, yPos)
            for dash in range(20):
                line.pendown()
                line.forward(15)
                line.penup()
                line.forward(15)
            yPos -= 20
