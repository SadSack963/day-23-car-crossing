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
counter = 0
cars = []
while game_is_on:
    time.sleep(0.1)
    screen.update()
    counter += 1
    if counter == 6:
        # Create Car
        cars.append(CarManager())
        counter = 0
    for car in cars:
        car.move()
        # Detect collision with player
        if -20 <= car.xcor() <= 20 and -20 < player.ycor() - car.ycor() < 20:
            game_is_on = False
            messenger.display_message("You Lost!")
    if player.win:
        game_is_on = False
        messenger.display_message("You Win!")


screen.exitonclick()
