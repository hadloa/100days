import turtle, random, time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
LANES = [540, ]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.cars = []

    def creator(self):
        if bool(random.choice([0,1])):
            new_car = Car()
            self.cars.append(new_car)

    def deletor(self):
        for car in self.cars:
            if car.xcor() <= -330:
                self.cars.remove(car)

    def move(self, level):
        for car in self.cars:
            car.move(level)



class Car(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.penup()
        y_pos = random.randrange(-220, 240, 20)
        self.goto(310, y_pos)

    def move(self, level):
        if self.xcor() > -330:
            self.forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT * (level - 1))




