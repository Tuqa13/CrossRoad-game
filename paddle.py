from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.goto(0, -280)

    def move_paddle(self):
        if self.ycor() != 280:
            self.fd(10)
