from tkinter import *

FONT = ('Arial', '16', 'normal')

def mile_to_km_convert():
    try:
        l_conversion['text'] = round(float(input.get()) * 1.609344, 2)
    except ValueError:
        l_conversion['text'] = 'Error'



window = Tk()
window.title('My First GUI Program')
window.config(padx=20, pady=20)

#button 1
butt = Button(text='Click Me', command=mile_to_km_convert)
butt.grid(column=1, row=3)

#entry
input = Entry(width=10)
input.grid(column=1, row=0)

#converted label
l_conversion = Label(text=0, font=FONT)
l_conversion.grid(column=1, row=1)

#label is euqual to
l_equals = Label(text="is equal to", font=FONT)
l_equals.grid(column=0, row=1)

#label miles
l_m = Label(text="Miles", font=FONT)
l_m.grid(column=2, row=0)

#label km
l_km = Label(text="Km", font=FONT)
l_km .grid(column=2, row=1)


mainloop()


