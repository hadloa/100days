from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = 'arial'




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

right_button = Button(image=right_img)
wrong_button = Button(image=wrong_img)


# canvas layout---------------------------
canvas.grid(column=0, columnspan=2, row=0, rowspan=2)
label_language.place(x=320, y=150)
label_word.place(x=320, y=263)
right_button.grid(column=0, row=2)
wrong_button.grid(column=1, row=2)


'''
button_start = Button(text="Start", font=FONT_NAME, command=start)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", command=reset, font=FONT_NAME)
button_reset.grid(column=2, row=2)
'''
mainloop()
