from turtle import Turtle


class Snake:
    def __init__(self):
        self.tosbişler = []
        start = [(0, 0), (-21, 0), (-42, 0)]
        for position in start:
            yılan = Turtle()
            yılan.speed(1)
            yılan.color("green")
            yılan.shape("square")
            yılan.penup()
            yılan.setpos(position)
            self.tosbişler.append(yılan)
        self.baş = self.tosbişler[0]

    def move(self):
        for _ in range(len(self.tosbişler) - 1, 0, -1):
            cord = self.tosbişler[_ - 1].pos()
            self.tosbişler[_].goto(cord)
        self.baş.forward(21)

    def k(self):
        if not self.baş.heading() == 270:
            self.baş.seth(90)

    def g(self):
        if not self.baş.heading() == 90:
            self.baş.seth(270)

    def b(self):
        if not self.baş.heading() == 0:
            self.baş.seth(180)

    def d(self):
        if not self.baş.heading() == 180:
            self.baş.seth(0)

    def add_snake(self):
        last = self.tosbişler[-1].pos()
        yılan = Turtle()
        yılan.speed(1)
        yılan.color("green")
        yılan.shape("square")
        yılan.penup()
        yılan.setpos(last)
        self.tosbişler.append(yılan)



