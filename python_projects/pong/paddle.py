from turtle import Turtle


class Paddle:
    def __init__(self):
            self.tosbiş = Turtle()
            self.tosbiş.shape("square")
            self.tosbiş.color("white")
            self.tosbiş.penup()
            self.tosbiş.setpos(-420, 0)
            self.tosbiş.shapesize(3, 1)


    def move_up(self):
        if self.tosbiş.ycor() < 250:
            self.tosbiş.shapesize(1, 3)
            self.tosbiş.setheading(90)
            self.tosbiş.forward(21)

    def move_down(self):
        if self.tosbiş.ycor() > -250:
            self.tosbiş.shapesize(1, 3)
            self.tosbiş.setheading(270)
            self.tosbiş.forward(21)



class Paddle_bot:
    def __init__(self):
        self.tosbiş = Turtle()
        self.tosbiş.shape("square")
        self.tosbiş.color("white")
        self.tosbiş.penup()
        self.tosbiş.setpos(415, 0)
        self.tosbiş.shapesize(3, 1)

    def move_up(self):
        if self.tosbiş.ycor() < 250:
            self.tosbiş.shapesize(1, 3)
            self.tosbiş.setheading(90)
            self.tosbiş.forward(21)

    def move_down(self):
        if self.tosbiş.ycor() > -250:
            self.tosbiş.shapesize(1, 3)
            self.tosbiş.setheading(270)
            self.tosbiş.forward(21)