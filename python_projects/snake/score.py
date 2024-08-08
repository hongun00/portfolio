from turtle import Turtle


class Score:
    def __init__(self):
        self.board = Turtle()
        self.board.ht()
        self.board.penup()
        self.current = 0
        with open("highscore.txt", "r") as highscore:
            self.highscore = highscore.read()
        self.board.setpos(0, 250)
        self.board.pendown()

    def skor_yaz(self):
        self.board.clear()
        self.board.write(f"score: {self.current}  Highscore: {self.highscore} ", False, "center", ("Ariel", 20, "normal"))