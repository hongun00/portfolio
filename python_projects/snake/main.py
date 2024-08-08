from turtle import Turtle, Screen
from snake import Snake
from score import Score
import time
from food import Food

tosbik = Turtle()
tosbik.penup()
tosbik.ht()
tosbik.color("black")

ekran = Screen()
ekran.setup(700, 700)
ekran.screensize(700, 700)
ekran.bgcolor("khaki")
devam = True
yemek = Food()
skor = Score()

def arkaplan():
    Y = -220.5
    X = -220.5
    for _ in range(22):
        arkaplan = Turtle()
        arkaplan.ht()
        arkaplan.speed(0)
        arkaplan.penup()
        arkaplan.setpos(X, Y)
        arkaplan.pendown()
        Y += 21
        arkaplan.forward(441)
    for _ in range(22):
        arkaplan = Turtle()
        arkaplan.ht()
        arkaplan.speed(0)
        arkaplan.left(90)
        arkaplan.penup()
        arkaplan.setpos(X, -220.5)
        arkaplan.pendown()
        X += 21
        arkaplan.forward(441)


yemek.randomize()
ekran.tracer(0)
yılan = Snake()
arkaplan()
skor.skor_yaz()
ekran.onkey(yılan.k, "Up")
ekran.onkey(yılan.g, "Down")
ekran.onkey(yılan.d, "Right")
ekran.onkey(yılan.b, "Left")
ekran.listen()

sleep_time = 0.35


while devam:
    ekran.update()
    time.sleep(sleep_time)
    yılan.move()
    if yılan.baş.distance(yemek) < 2:
        extra_check = True
        yılan.add_snake()
        yemek.randomize()
        while extra_check:
            for oppa in yılan.tosbişler:
                if oppa.distance(yemek) > 10:
                    extra_check = False
                else:
                    yemek.randomize()

        skor.current += 1
        skor.skor_yaz()
        sleep_time -= 0.0045
    if yılan.baş.xcor() < -215 or yılan.baş.xcor() > 215:
        devam = False
        tosbik.write(f"Game over", False, "center", ("Ariel", 40, "normal"))
        if skor.current > int(skor.highscore):
            with open("highscore.txt", "w") as highscore:
                highscore.write(str(skor.current))
    elif yılan.baş.ycor() < -215 or yılan.baş.ycor() > 215:
        devam = False
        tosbik.write(f"Game over", False, "center", ("Ariel", 40, "normal"))
        if skor.current > int(skor.highscore):
            with open("highscore.txt", "w") as highscore:
                highscore.write(str(skor.current))
    for tıss in yılan.tosbişler[1:]:
        if yılan.baş.distance(tıss) < 2:
            devam = False
            tosbik.write(f"Game over", False, "center", ("Ariel", 40, "normal"))
            if skor.current > int(skor.highscore):
                with open("highscore.txt", "w") as highscore:
                    highscore.write(str(skor.current))



ekran.exitonclick()

