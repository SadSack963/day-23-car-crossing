from turtle import Turtle


class Messenger(Turtle):
    def __init__(self):
        super(Messenger, self).__init__()
        self.pu()
        self.hideturtle()
        self.pencolor("red")

    def display_message(self, message):
        self.write(arg=message, move=False, align="center", font=("Comic Sans", 48, "italic"))

