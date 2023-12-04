"""Manipulating Data with Pandas"""
import pandas as pd

df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')

"""
When selecting a single column from a Pandas DataFrame, we use single square brackets.
When selecting multiple columns, we use double square brackets.
"""

# Selecting a single column
col = df['Fare'] # return a Series
print(col)

# Selecting multiple columns
selected_cols = df[['Age','Sex','Survived']] # return a DataFrame
print(selected_cols.head())

# Creating a column
df['male'] = df['Sex'] == 'male'
print(df.head())
