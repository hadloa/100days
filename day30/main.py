from tkinter import *
from tkinter import messagebox
import secrets
import string
import pyperclip
import json

N = 16
FILE_PATH = 'passlist.json'
CHAR_CHOICE = string.ascii_letters + string.digits + string.punctuation.replace(',', '')


# ---------------------------- SEARCH ------------------------------- #
def search():
    website = entry_website.get().lower()
    try:
        with open(FILE_PATH, 'r') as f_file:
            data = json.load(f_file)
    except FileNotFoundError:
        messagebox.showerror(title=f'No entries', message=f'No entries found')
        return

    try:
        data[website]
    except KeyError:
        messagebox.showerror(title=f'Missing entry', message=f'Entry not found')
    else:
        pyperclip.copy(data[website]["Password"])
        messagebox.showinfo(title=website.capitalize(), message=f'Username: {data[website]["Username"]}\n'
                                                                f'Password: {data[website]["Password"]}')


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen():
    entry_pass.delete(0, END)
    password = ''.join(secrets.choice(CHAR_CHOICE) for _ in range(N))
    entry_pass.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def error_blank(key):
    messagebox.showerror(title=f'Blank {key}', message=f'{key} is blank, please try again.')


def add():
    website = entry_website.get().lower()
    user = entry_user.get()
    password = entry_pass.get()
    account = {
        website: {
            'Username': user,
            'Password': password
        }
    }

    site = list(account.keys())[0]
    if len(site) == 0:
        error_blank("Website")
        return
    for info in account[site]:
        if len(account[site][info]) == 0:
            error_blank(info)
            return


    #is_ok = messagebox.askokcancel(title=website,message=f'Details entered: \nUsername: {user} \n'
                                                         #f'Password: {password} \n OK to save?')
    if 'is_ok':
        try:
            with open(FILE_PATH, 'r') as f_file:
                data = json.load(f_file)
        except FileNotFoundError:
            data = account
        else:
            data.update(account)

        with open(FILE_PATH, 'w') as f_file:
            json.dump(data, f_file, indent=4)

        entry_website.delete(0, END)
        entry_pass.delete(0, END)
        entry_user.insert(0, "AndrewDHadlock@gmail.com")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=25, pady=25)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(130, 110, image=logo_img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1, sticky='W')

entry_website = Entry()
entry_website.grid(column=1, row=1, sticky='EW')
entry_website.focus()

label_user = Label(text="Username:")
label_user.grid(column=0, row=2, sticky='W')

entry_user = Entry()
entry_user.grid(column=1, columnspan=2, row=2, padx=3, pady=3, sticky='EW')
entry_user.insert(0, "AndrewDHadlock@gmail.com")

label_pass = Label(text="Password:")
label_pass.grid(column=0, row=3, sticky='W')

entry_pass = Entry()
entry_pass.grid(column=1, row=3, sticky='EW')

button_gen = Button(text="Generate Password", command=gen)
button_gen.grid(column=2, row=3, sticky='EW', padx=3)

button_add = Button(text="Add", command=add)
button_add.grid(column=1, columnspan=2, row=4, pady=3, sticky='EW')

button_search = Button(text="Search Accounts", command=search)
button_search.grid(column=2, row=1, sticky='EW', padx=3)

mainloop()
