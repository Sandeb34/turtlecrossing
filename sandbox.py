# My trail on tackling the code
# not part of final code use main.py
# ****Sandbox_only****

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

# car_list = []
# for i in range(10):
#     car = CarManager()
#     car_list.append(i)


# def generator(self):
#     objs = list()
#     for i in range(20):
#         objs.append(CarManager())
#
#
# generator()


screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()
    scoreboard = Scoreboard()

#     detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()

# car_manager.py

# My 80% solution
# class CarManager(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.setheading(270)
#         self.shape("square")
#         self.penup()
#         self.color(COLORS[random.randrange(len(COLORS))])
#         self.shapesize(stretch_wid= 2, stretch_len= 1)
#         self.goto(x=280, y=random.randrange(-260,260))
#         self.x_move = MOVE_INCREMENT
#         self.move_speed = 0.5
#
#     def move(self):
#         new_x = self.xcor() - self.x_move
#         ycor = self.ycor()
#         self.goto(new_x, ycor)


# player.py


# My interpretation:
# def go_up(self):
#     new_y = self.ycor() + 10
#     self.goto(self.xcor(), new_y)
