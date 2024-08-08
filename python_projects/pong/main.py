from turtle import Screen, Turtle
from paddle import Paddle , Paddle_bot
import time
from ball import Ball
from scoreboard import Scoreboard

devam = True
ekran = Screen()
ekran.setup(900, 600)
ekran.bgcolor("black")
ekran.tracer(0)


def bg_cizgi():
    bg.pendown()
    bg.forward(10)
    bg.penup()
    bg.forward(12)

bg = Turtle()
bg.ht()
bg.pensize(5)
bg.color("white")
bg.penup()
bg.setpos(0, 270)
bg.setheading(270)
for _ in range(26):
    bg_cizgi()

oyuncu = Paddle()
bot = Paddle_bot()
top = Ball()
tahta = Scoreboard()
ekran.update()

ekran.onkeypress(oyuncu.move_up, "w")
ekran.onkeypress(oyuncu.move_down, "s")
ekran.onkeypress(bot.move_up, "Up")
ekran.onkeypress(bot.move_down, "Down")
ekran.listen()
top.random_start()
tahta.write_score()
move_speed = 0.05

while devam:
    time.sleep(move_speed)
    ekran.update()
    top.tosbik.forward(10)
    if top.tosbik.ycor() > 280:
        top.bounce()
    if top.tosbik.ycor() < -270:
        top.bounce()
    if oyuncu.tosbiş.distance(top.tosbik) < 45 and top.tosbik.xcor() < -400:
        top.bounce_player()
        move_speed *= 0.9
    if bot.tosbiş.distance(top.tosbik) < 45 and top.tosbik.xcor() > 400:
        top.bounce_player()
        move_speed *= 0.9
    if not -500 < top.tosbik.xcor():
        top.reset_self()
        move_speed = 0.05
        tahta.right += 1
        tahta.write_score()
    elif not top.tosbik.xcor() < 500:
        top.reset_self()
        move_speed = 0.05
        tahta.left += 1
        tahta.write_score()

ekran.exitonclick()