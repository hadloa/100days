import datetime as dt
import random, os
import pandas as pd


TEMPLATE_PATH = './letter_templates'
BDAY_DF = pd.read_csv('./birthdays.csv', index_col=False)


def bday_check():
    date = dt.datetime.now()
    month = date.month
    day = date.day
    bdays = BDAY_DF.loc[(BDAY_DF['month'] == month) & (BDAY_DF['day'] == day)]
    bday_list = []
    for i, bday in bdays.iterrows():
        if i <= len(bdays):
            bday_list.append(letter_maker(bday))
    return bday_list


def letter_maker(bdays):
    birthday = [bdays[0], bdays[1]]
    birthday.append(choose_template().replace('[NAME]', birthday[0]))
    return birthday

def choose_template():
    template_path = TEMPLATE_PATH + '/' + random.choice(os.listdir(TEMPLATE_PATH))
    with open(template_path) as file:
        template_str = file.read()
    return template_str
