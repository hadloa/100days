from tkinter import *

FILE_PATH = 'passlist.txt'
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    account_info = f'{entry_website.get()},{entry_user.get()},{entry_pass.get()}\n'
    with open(FILE_PATH, 'a') as f_file:
        f_file.write(account_info)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

entry_website = Entry(width=35)
entry_website.grid(column=1, columnspan=2, row=1)
entry_website.focus()

label_user = Label(text="Email/Username:")
label_user.grid(column=0, row=2)

entry_user = Entry(width=35)
entry_user.grid(column=1, columnspan=2, row=2)
entry_user.insert(0, "AndrewDHadlock@gmail.com")

label_pass = Label(text="Password:")
label_pass.grid(column=0, row=3)

entry_pass = Entry(width=21)
entry_pass.grid(column=1, columnspan=2, row=3)

button_gen = Button(text="Generate Password", command=gen)
button_gen.grid(column=2, row=3)

button_add = Button(text="Add", command=add, width=36)
button_add.grid(column=1, columnspan=2, row=4)

mainloop()