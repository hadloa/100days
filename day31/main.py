from tkinter import *
import time
import pandas as pd

french_words = pd.read_csv("./data/french_words.csv")

current_word = None
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = 'arial'

# Functions---------------------------------------------------------


def knew_it():
    new_card(True)


def didnt_know():
    new_card(False)


def new_card(did_you_know):
    global current_word
    current_word = french_words.sample()
    flip_front()


def flip_back():
    canvas.create_image(402, 265, image=back_img)
    label_language.config(text='English')
    label_word.config(text=current_word.iat[0, 1])


def flip_front():
    canvas.create_image(402, 265, image=front_img)
    label_language.config(text='French')
    label_word.config(text=current_word.iat[0, 0])
    #time.sleep(5)
    #flip_back()


# window------------------------------------------------------------
window = Tk()
window.title('Flashcards')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#label_title = Label(text="Timer", bg=BACKGROUND_COLOR, font=(FONT_NAME, 40, 'bold'))
#label_title.grid(column=1, row=0)

#label_check = Label(bg=BACKGROUND_COLOR, pady=20, font=(FONT_NAME, 20))
#label_check.grid(column=1, row=4)


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

new_card(False)
mainloop()

