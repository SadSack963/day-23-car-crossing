import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from messenger import Messenger

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# Create Messenger - Used to write messages for the Player
messenger = Messenger()

# Create Player
player = Player()
screen.onkeypress(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.win:
        game_is_on = False
        messenger.display_message("You Win!")


screen.exitonclick()
