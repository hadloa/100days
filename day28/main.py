from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
stop = False


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps, stop
    stop = True
    reps = 0
    label_title.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text=f'00:00')
    label_check.config(text='')


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start():
    global reps, stop
    stop = False
    reps += 1
    checks = '✔' * int(reps / 2)
    label_check.config(text=checks)

    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        label_title.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        label_title.config(text="Break", fg=PINK)
    else:
        countdown(WORK_MIN * 60)
        label_title.config(text="work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = int(count / 60)
    count_sec = count % 60

    if stop:
        return

    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        window.after(1000, countdown, count - 1)
    else:
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)
        start()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

label_title = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, 'bold'))
label_title.grid(column=1, row=0)

label_check = Label(bg=YELLOW, fg=GREEN, pady=20, font=(FONT_NAME, 20))
label_check.grid(column=1, row=4)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=1, row=1)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 30, 'bold'))

button_start = Button(text="Start", font=FONT_NAME, command=start)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", command=reset, font=FONT_NAME)
button_reset.grid(column=2, row=2)

mainloop()
