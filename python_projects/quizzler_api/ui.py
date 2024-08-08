from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizzUI:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.text = self.canvas.create_text(150, 130, text=f"question here", font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=40, pady=40)

        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")



        self.true_button = Button(command=self.true, image=true_image, highlightthickness=0)
        self.true_button.grid(column=0, row=3)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false)
        self.false_button.grid(column=1, row=3)

        self.counter = Label(text=f"Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 15, "italic"))
        self.counter.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.counter.config(text=f"Score: {self.quiz.score}")
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=question)
        else:
            self.canvas.itemconfig(self.text, text="You have finished all the questions")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true(self):
        self.give_feedback(self.quiz.check_answer("True"))


    def false(self):
        self.give_feedback(self.quiz.check_answer("False"))



    def give_feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
            self.quiz.score += 1
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


