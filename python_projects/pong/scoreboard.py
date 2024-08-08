from turtle import Turtle

class Scoreboard:
    def __init__(self):
        self.left = 0
        self.right = 0
        self.keeper = Turtle()
        self.keeper.penup()
        self.keeper.ht()
        self.keeper.setpos(0, 230)
        self.keeper.color("white")
        self.keeper.pendown()

    def write_score(self):
        self.keeper.clear()
        self.keeper.write(f"{self.left}        {self.right}", False, "center", ("Ariel", 40, "normal"))
