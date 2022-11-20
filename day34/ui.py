from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WRONG = '#D16666'
RIGHT = '#29B677'
FONT = ('arial', 20, 'italic')

class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        # window
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(pady=20, bg=THEME_COLOR)

        #canvas
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125,
                                                     fill=THEME_COLOR,
                                                     font=FONT,
                                                     width=280)
        self.canvas.grid(column=0, columnspan=2, row=1, pady=20, padx=20)

        #score
        self.score = Label(text=f'Score: {0}', bg=THEME_COLOR, fg='white', font=('arial', 18))
        self.score.grid(column=1, row=0)

        #buttons
        self.right_img = PhotoImage(file='./images/true.png')
        self.wrong_img = PhotoImage(file='./images/false.png')

        self.right_button = Button(image=self.right_img, command=self.get_is_true)
        self.wrong_button = Button(image=self.wrong_img, command=self.get_is_false)

        self.right_button.grid(column=0, row=2)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f'Score: {self.quiz.score}')
            next_q = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=next_q)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.right_button.config(state='disabled')
            self.wrong_button.config(state='disabled')
    def get_is_true(self):
        is_right = self.quiz.check_answer('true')
        self.give_feedback(is_right)

    def get_is_false(self):
        is_right = self.quiz.check_answer('false')
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg=RIGHT)
            self.window.after(ms=500, func=self.get_next_question)
        else:
            self.canvas.config(bg=WRONG)
            self.window.after(ms=500, func=self.get_next_question)

