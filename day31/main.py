from tkinter import *
import pandas as pd

#french_words = pd.read_csv("./data/french_words.csv")
words_to_learn = None
current_word = None
BACKGROUND_COLOR = "#B1DDC6"
BACK_COLOR = "#91C2AF"
FONT_NAME = 'arial'
FILE_PATH = './data/words_to_learn.csv'


# Functions---------------------------------------------------------
def startup():
    global words_to_learn
    try:
        words_to_learn = pd.read_csv("./data/words_to_learn.csv", index_col=0)
    except FileNotFoundError:
        words_to_learn = pd.read_csv("./data/french_words.csv")


def knew_it():
    new_card(True)


def didnt_know():
    new_card(False)


def new_card(did_you_know):
    global current_word, words_to_learn
    if did_you_know:
        words_to_learn = words_to_learn.drop(current_word.index[0])
        words_to_learn.to_csv(path_or_buf=FILE_PATH)
    current_word = words_to_learn.sample()
    flip_front()
    window.after(3000, flip_back)


def flip_back():
    canvas.create_image(402, 265, image=back_img)
    label_language.config(text='English', bg=BACK_COLOR)
    label_word.config(text=current_word.iat[0, 1], bg=BACK_COLOR)


def flip_front():
    canvas.create_image(402, 265, image=front_img)
    label_language.config(text='French', bg='white')
    label_word.config(text=current_word.iat[0, 0], bg='white')


# window------------------------------------------------------------
window = Tk()
window.title('Flashcards')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# canvas------------
canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)

front_img = PhotoImage(file='./images/card_front.png')
back_img = PhotoImage(file='./images/card_back.png')

canvas.create_image(402, 265, image=front_img)

# Labels----------
label_language = Label(text='French', bg='white', font=(FONT_NAME, 40, 'italic'))
label_word = Label(text='trouve', bg='white', font=(FONT_NAME, 40, 'bold'))

# Buttons--------
right_img = PhotoImage(file='./images/right.png')
wrong_img = PhotoImage(file='./images/wrong.png')

right_button = Button(image=right_img, command=knew_it)
wrong_button = Button(image=wrong_img, command=didnt_know)

# canvas layout---------------------------
canvas.grid(column=0, columnspan=2, row=0, rowspan=2)
label_language.place(x=320, y=150)
label_word.place(x=320, y=263)
right_button.grid(column=0, row=2)
wrong_button.grid(column=1, row=2)


startup()
new_card(False)
mainloop()
