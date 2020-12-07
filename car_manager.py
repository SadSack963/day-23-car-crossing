from turtle import Turtle
from random import randint, choice


COLORS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, level):
        super(CarManager, self).__init__()
        self.pu()
        self.shape("square")
        self.resizemode("user")
        self.shapesize(stretch_len=2)
        self.setheading(180)
        self.setundobuffer(None)
        self.color(choice(COLORS))
        self.setx(320)
        self.sety(randint(-250, 250))
        self.move_distance = STARTING_MOVE_DISTANCE + int(MOVE_INCREMENT * (level - 1) / 2)

    def move(self):
        self.fd(self.move_distance)
