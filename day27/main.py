from tkinter import *

FONT = ('Arial', '24', 'bold')


count: int = 0
def button_click():
    global count
    count += 1
    my_label['text'] = f'{count}: {input.get()}'


window = Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#label

my_label = Label(text="Label", font=FONT)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


#button 1
butt = Button(text='Click Me', command=button_click)
butt.grid(column=1, row=1)

#button 2
butt = Button(text='Click Me', command=button_click)
butt.grid(column=2, row=0)

#entry

input = Entry(width=10)
input.grid(column=3, row=3)



mainloop()


