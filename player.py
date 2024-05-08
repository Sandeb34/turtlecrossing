from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    # Allows the turtle to move forward. No need to change coordinates just let it move forward
    def go_up(self):
        self.forward(MOVE_DISTANCE)

    # Checks if turtle is at Finish lined define at top.
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            False

    def go_to_start(self):
        self.goto(STARTING_POSITION)
