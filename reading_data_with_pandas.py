"""Basic use of pandas to read data from a csv file"""
import pandas as pd
pd.options.display.width = 100

df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')

print(df.head())
print('\n')
print(df.describe())
