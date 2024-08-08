from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmarks = ""
time = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_clock():
    global checkmarks, reps
    window.after_cancel(timer)
    yazı1.config(text="Timer", fg=GREEN)
    checkmarks = ""
    tick.config(text=checkmarks)
    canvas.itemconfig(clock_text, text="00:00")
    reps = 0

# ---------------------------- TIMER MECHANISM -------------------------------  #


def count():
    global checkmarks
    if reps == 0:
        yazı1.config(text="Work", fg=GREEN)
        clock(25, 0)
    else:
        if reps % 7 == 0:
            yazı1.config(text="Break", fg=RED)
            checkmarks += "✓"
            tick.config(text=checkmarks)
            clock(20, 0)
        elif reps % 2 == 0:
            yazı1.config(text="Work", fg=GREEN)
            clock(25, 0)
        elif reps % 2 == 1:
            yazı1.config(text="Break", fg=PINK)
            checkmarks += "✓"
            tick.config(text=checkmarks)
            clock(5, 0)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def clock(count_min, seconds):
    global reps
    global timer
    if seconds < 10:
        canvas.itemconfig(clock_text, text=f"{count_min}:0{seconds}")
    elif seconds >= 10:
        canvas.itemconfig(clock_text, text=f"{count_min}:{seconds}")
    if count_min == 0 and seconds == 0:
        reps += 1
        count()
    if count_min >= 0 and seconds >= 0:
        if seconds == 0:
            seconds += 60
            count_min -= 1
        timer = window.after(1000, clock, count_min, seconds - 1)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title = "pomodoro"
window.config(padx=150, pady=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
resim = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=resim)
clock_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)
yazı1 = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
yazı1.grid(column=1, row=0)
start_button = Button(text="Start", command=count)
start_button.grid(column=0, row=2)
stop_button = Button(text="Stop", command=reset_clock)
stop_button.grid(column=2, row=2)
tick = Label(text=checkmarks, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
tick.grid(column=1, row=3)
window.mainloop()
