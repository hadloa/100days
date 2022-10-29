import pandas as pd

nato_df = pd.read_csv('./nato_phonetic_alphabet.csv')

nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

exit = False
while not exit:
    word_input = input("Enter word for nato alphabet: ").strip().upper()
    if word_input == 'EXIT':
        exit = True
    elif word_input.isalpha():
        output = [nato_dict[letter] for letter in word_input]
        print(output)
    else:
        print('sorry that is not a valid word')
    print('\n')
