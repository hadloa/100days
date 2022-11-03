from tkinter import *
from tkinter import messagebox
import secrets
import string
import pyperclip

N = 16
FILE_PATH = 'passlist.txt'
CHAR_CHOICE = string.ascii_letters + string.digits + string.punctuation.replace(',', '')


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen():
    entry_pass.delete(0, END)
    password = ''.join(secrets.choice(CHAR_CHOICE) for _ in range(N))
    entry_pass.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():

    website = entry_website.get()
    user = entry_user.get()
    password = entry_pass.get()
    account = {'Website': website,'Username': user, 'Password': password}

    for key in account:
        if len(account[key]) == 0:
            messagebox.showerror(title=f'Blank {key}', message=f'{key} is blank, please try again.')
            return

    is_ok = messagebox.askokcancel(title=website,message=f'Details entered: \nUsername: {user} \n'
                                                         f'Password: {password} \n OK to save?')
    if is_ok:
        with open(FILE_PATH, 'a') as f_file:
            f_file.write(f'{website},{user},{password}\n')
        entry_website.delete(0, END)
        entry_pass.delete(0, END)
        entry_user.insert(0, "AndrewDHadlock@gmail.com")


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
