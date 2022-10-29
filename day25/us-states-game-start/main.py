import turtle
import pandas as pd

FONT = ("Courier", 12, "normal")

data_states = pd.read_csv('./50_states.csv')
states = data_states.state.to_list()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

guessed = []

while len(guessed) < 50:

    answer_state = screen.textinput(title=f"Guess the State {len(guessed)}/50", prompt="What's another state's name?").title()

    if len(data_states.loc[data_states['state'] == answer_state]) > 0:
        guessed.append(answer_state)

        # stateDF = data_states.loc[data_states['state'] == answer_state]
        # state = stateDF.iloc[0]['state']
        # x = stateDF.iloc[0]['x']
        # y = stateDF.iloc[0]['y']

        state_data = data_states[data_states.state == answer_state]
        state = answer_state
        x = int(state_data.x)
        y = int(state_data.y)
        print(state, x, y)

        t_state = turtle.Turtle()
        t_state.hideturtle()
        t_state.penup()
        t_state.speed('fastest')
        t_state.goto(x, y)
        t_state.write(state, font=FONT, align='center')
    elif answer_state == 'Exit':
        break


for state in guessed:
    if state in states:
        states.remove(state)

missed_states = pd.DataFrame(states)
missed_states.to_csv('missed_states.txt')

screen.exitonclick()
