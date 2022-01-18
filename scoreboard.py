from turtle import Turtle
import time

FONT = ('Courier', 20, 'bold')


class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 0)
        self.color('red')
        self.write(f'Level {self.level}', False, 'center', FONT)
        time.sleep(2)
        self.clear()
        self.color('black')
        self.goto(-220, 260)
        self.write(f'Level: {self.level}', False, 'center', FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color('red')
        self.write('Game Over', False, 'center', FONT)
