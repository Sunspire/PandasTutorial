from termcolor import colored
import pandas as pd


print(colored('Empty data frame', 'cyan'))
df = pd.DataFrame()
print(df)
print()

print(colored('From list', 'cyan'))
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)
print()

data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print(df)
print()

print(colored('From Dict of ndarrays / Lists', 'cyan'))
print(colored('Arrays must be of the same length', 'cyan'))
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print(df)
print()

print(colored('Indexed DataFrame using array', 'cyan'))
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print(df)