from termcolor import colored
import pandas as pd
import numpy as np


data = pd.read_csv('Datasets/MusicGenreClassification/train.csv')
'''
#View the data
print(colored('data.shape: ', 'cyan') + f'{data.shape}')
print()

print(colored('data.head(): ', 'cyan') + f'\n{data.head()}')
print()
'''
'''
Gives a nice summary of the data. Such as the count of all the columns, 
the highest occurring value in each column (if applicable) and its frequency.
'''
'''
print(colored('data.describe(include="all"): ', 'cyan') + f'\n{data.describe(include="all")}')
print()

#Look for missing values
print(colored('data.isna().sum()', 'cyan') + f'\n{data.isna().sum()}')
print()
'''
artist_by_popularity = data.groupby('Artist Name')
print(artist_by_popularity.describe(include="all"))