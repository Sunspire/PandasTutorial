from termcolor import colored
import pandas as pd
import numpy as np

print(colored('Empty series', 'cyan'))
s = pd.Series()
print(s)
print()

print(colored('Series from ndarray', 'cyan'))
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s)
print()

print(colored('Same as above but using customized index', 'cyan'))
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print(s)
print()

print(colored('Series from dict. Dictionary keys create the index', 'cyan'))
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
print(s)
print()

print(colored('Series from Scalar', 'cyan'))
s = pd.Series(5, index=[0, 1, 2, 3])
print(s)
print()

print(colored('Get first 3 elements', 'cyan'))
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s[:3])
print()

print(colored('Get last 3 elements', 'cyan'))
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s[-3:])
print()

print(colored('Get data with label', 'cyan'))
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s['b'])
print()

print(colored('Get multiple elements with label', 'cyan'))
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(s[['b', 'e']])
print()