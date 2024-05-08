from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        # creates list of all randomly created cars in create_cars method
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        # This part let allows for fewer card every time the number 1 is produced a car is made.
        # You can increase the number to make the changes of the int == 1 decrease.
        # Therefor there will be less cars created.
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            # Choses randomly out of a list with items
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            # Instead of trying to rotate the turtle just let it move backward.
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


