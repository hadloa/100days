from turtle import Turtle
FONT = ('Courier', 20, 'normal')
ALIGNMENT = 'center'
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 270)
        self.updateScore()


    def updateScore(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.score += 1
        self.clear()
        self.updateScore()


    def gameOver(self):
        self.goto(0, 0)
        self.write(f'Game Over', align=ALIGNMENT, font=FONT)


