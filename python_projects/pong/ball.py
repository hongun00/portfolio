from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.tosbik = Turtle()
        self.tosbik.penup()
        self.tosbik.color("white")
        self.tosbik.shape("circle")
        self.tosbik.shapesize(0.8)

    def random_start(self):
        self.ball_degree = random.randint(0, 360)
        while 45 < self.ball_degree and self.ball_degree < 135 or 225 < self.ball_degree and self.ball_degree < 315:
            self.ball_degree = random.randint(0, 360)
        self.tosbik.setheading(self.ball_degree)


    def bounce(self):
        bounce_degree = 360 - self.ball_degree
        self.ball_degree = bounce_degree
        self.tosbik.setheading(self.ball_degree)

    def bounce_player(self):
        bounce_degree = 180 - self.ball_degree
        self.ball_degree = bounce_degree
        self.tosbik.setheading(self.ball_degree)

    def reset_self(self):
        self.tosbik.ht()
        self.tosbik.setpos(0, 0)
        self.tosbik.st()
        self.random_start()
        