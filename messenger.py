from turtle import Turtle
from time import sleep


class Messenger(Turtle):
    def __init__(self, position, fontcolor, fontsize, fonttype):
        super(Messenger, self).__init__()
        self.pu()
        self.hideturtle()
        self.setposition(position)
        self.pencolor(fontcolor)
        self.font = ("Comic Sans", fontsize, fonttype)

    def display_message(self, message, time):
        """Displays message for a time.
        If time <= 0 then the message is not cleared."""
        self.clear()  # Clear any previous message
        self.write(arg=message, move=False, align="center", font=self.font)
        if time > 0:
            sleep(time)
            self.clear()

