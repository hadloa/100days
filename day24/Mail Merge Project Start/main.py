with open('Input/Names/invited_names.txt') as n_file:
    names = n_file.read().split('\n')

with open('Input/Letters/starting_letter.txt') as l_file:
    letter = l_file.read()

for name in names:
    readyToSend = f'./Output/ReadyToSend/invite_letter_{name.lower()}.txt'
    letter_copy = letter.replace('[name]', name)
    with open(readyToSend, 'w') as f_file:
        f_file.write(letter_copy)
