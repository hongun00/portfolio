from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.75, 0.75)
        self.color("blue")
        self.ht()
        self.penup()
        self.speed("fastest")

    def randomize(self):
        self.ht()
        x = random.randint(-10, 10)
        y = random.randint(-10, 10)
        self.setpos(x*21, y*21)
        self.showturtle()
