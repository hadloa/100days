import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing')
screen.tracer(0)

player = Player()
board = Scoreboard()
carManager = CarManager()


screen.listen()
screen.onkey(player.up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carManager.creator()
    carManager.move(board.score)
    carManager.deletor()
    print(len(carManager.cars))

    if player.ycor() > 260:
        board.point()
        player.reset_pos()

    for car in carManager.cars:
        if player.distance(car) < 15:
            board.gameOver()
            player.color('red')
            size = 1
            while size < 30:
                screen.update()
                player.setheading(player.heading() + 10)
                player.shapesize(stretch_wid=size, stretch_len=size)
                size *= ((1 / 36) + 1)
                time.sleep(.05)

            game_is_on = False


screen.exitonclick()