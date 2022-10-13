from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Score, FONT, ALIGNMENT

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title('Snake')
s.tracer(0)

snake = Snake()
food = Food()
score = Score()

s.listen()
s.onkey(snake.up, 'Up')
s.onkey(snake.down, 'Down')
s.onkey(snake.left, 'Left')
s.onkey(snake.right, 'Right')


gameIsOn = True
while gameIsOn:
    s.update()
    time.sleep(.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.refresh()
        snake.extend()

    x_bool = snake.head.xcor() > 295 or snake.head.xcor() < -295
    y_bool = snake.head.ycor() > 295 or snake.head.ycor() < -295
    if x_bool or y_bool:
        score.gameOver()
        gameIsOn = False

    if snake.hit():
        score.gameOver()
        gameIsOn = False


s.exitonclick()