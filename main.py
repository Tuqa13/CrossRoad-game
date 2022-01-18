from turtle import Screen
from paddle import Paddle
from cars import Car
from scoreboard import Level
import time

# Setup the screen:
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# create objects:
my_turtle = Paddle()
cars = []
new_cars = []
level = Level()

for n in range(25):
    cars.append(Car())
    cars[n].new_game()

# control the turtle:
screen.listen()
screen.onkeypress(my_turtle.move_paddle, 'Up')

# starting the game:
Speed = 0.1
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(Speed)
    for x in cars:
        x.move_car()
        if x.xcor() < -300:
            x.goto(500, x.ycor())
        if x.distance(my_turtle) < 25:
            game_is_on = False
            level.game_over()

    if my_turtle.ycor() >= 280:
        level.level += 1
        level.update_score()
        my_turtle.goto(0, -280)
        Speed -= 0.01

screen.exitonclick()
