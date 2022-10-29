import pandas as pd

data_sq = pd.read_csv('./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

color_count = data_sq['Primary Fur Color'].value_counts()

color_count.to_csv('color_count.txt')
