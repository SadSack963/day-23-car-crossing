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

# Create Messengers - Used to write brief messages for the Player
status_message = Messenger(position = (0, 0), fontcolor="red", fontsize=50,
                           fonttype="bold italic")
level_message = Messenger(position = (0, 0), fontcolor="dark green", fontsize=50,
                          fonttype="italic")

# Create Level Display
level_display = Messenger(position = (-250, 276), fontcolor="black", fontsize=16,
                          fonttype="normal")

# Create Player
player = Player()
screen.onkeypress(player.move_up, "Up")

game_is_on = True
counter = 0
cars = []
level = 1
level_message.display_message(f"Level {level}", time=1)
while game_is_on:
    level_display.display_message(f"Level {level}", time=-1)
    time.sleep(0.1)
    screen.update()
    counter += 1
    if counter == 6:
        # Create Car
        cars.append(CarManager(level))
        counter = 0
    for car in cars:
        car.move()
        # Detect collision with player
        if -20 <= car.xcor() <= 20 and -20 < player.ycor() - car.ycor() < 20:
            screen.update()
            game_is_on = False
            status_message.display_message("You Lost!", time=-1)
        # Remove the car from the list if past the end of the road
        if car.xcor() < -380:
            cars.remove(car)
    if player.win:
        status_message.display_message("You Win!", time=1.5)
        level += 1
        level_message.display_message(f"Level {level}", time=1)
        player.start()

screen.exitonclick()
