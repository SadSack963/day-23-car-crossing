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
        """Move the player up and check for the finish line"""
        if self.ycor() < FINISH_LINE_Y:
            self.fd(MOVE_DISTANCE)
        else:
            self.win = True

    def start(self):
        """Reset the player to the starting position"""
        self.setposition(STARTING_POSITION)
        self.win = False
