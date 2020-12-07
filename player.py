from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.pu()
        self.shape("turtle")
        self.setposition(STARTING_POSITION)
        self.setheading(90)
        self.win = False

    def move_up(self):
        if self.ycor() < FINISH_LINE_Y:
            self.fd(MOVE_DISTANCE)
        else:
            self.win = True



