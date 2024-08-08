import turtle
import pandas
data = pandas.read_csv("50_states.csv")


screen = turtle.Screen()
screen.title("U.S States Game")
screen.addshape("blank_states_img.gif")
tosbik = turtle.Turtle()
tosbik.ht()
tosbik.penup()
tosbik.color("black")
tosbik.speed("fastest")
devam = True
eyaletler = list(data["state"])
tahmin_edilmiş = []

turtle.shape("blank_states_img.gif")
answer = screen.textinput("Guess the state", "What's another state's name?").lower().title()
score = 0

while devam:
    if answer == "Exit":
        unknown = [tah for tah in eyaletler if tah not in tahmin_edilmiş]
        son = pandas.DataFrame(unknown)
        son.to_csv("bilinmeyenler.csv")
        break
    if answer in eyaletler and answer not in tahmin_edilmiş:
        score += 1
        xcor = data[data["state"] == answer]["x"]
        ycor = data[data["state"] == answer]["y"]
        tosbik.setpos(int(xcor), int(ycor))
        tosbik.write(answer, False, "center", ("Arial", 10, "normal"))
        tahmin_edilmiş.append(answer)
    answer = screen.textinput(f"{score}/50 States Correct", "What's another state's name?").lower().title()

turtle.mainloop()