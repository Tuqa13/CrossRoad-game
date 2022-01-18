from turtle import Turtle
import random

COLORS = ['silver', 'gray', 'rosybrown', 'darkred', 'tomato', 'orangered', 'chocolate', 'tan', 'gold',
          'olive', 'yellowgreen', 'lawngreen', 'lightgreen', 'darkgreen', 'lime', 'aquamarine', 'teal',
          'cyan', 'lightblue', 'royalblue', 'navy', 'blueviolet', 'mediumorchid', 'orchid', 'plum',
          'purple', 'fuchsia', 'deeppink', 'hotpink', 'pink', 'crimson']

# Another solution is to create this class without inherit turtle
# and make it # cars and create all the cars in here as shown in angela solution...


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)

    def new_game(self):
        new_y = random.randint(-250, 250)
        new_x = random.randint(-250, 500)
        self.goto(new_x, new_y)

    def move_car(self):
        self.backward(10)
