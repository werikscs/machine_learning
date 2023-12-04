"""
Numpy basics.
We often will take the data from our pandas DataFrame and put it in numpy arrays.
Pandas DataFrames are great because we have the column names
and other text data that makes it human readable.
A DataFrame, while easy for a human to read, is not the ideal format for doing calculations.
The numpy arrays are generally less human readable,
but are in a format that enables the necessary computation.
"""

import pandas as pd

# convert the Fare column to a numpy array.
df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')

# The values attribute of a Pandas Series give the data as a numpy array.
fare_values = df['Fare'].values # return a 1-dimensional array
print(fare_values)

# The values attribute of a Pandas DataFrame give the data as a 2d numpy array.
multi_values = df[['Pclass', 'Fare', 'Age']].values # return a 2-dimensional array
print(multi_values)

# The shape attribute of a numpy array gives the dimensions of the array.
arr = df[['Pclass', 'Fare', 'Age']].values
# You can also use the shape attribute on a pandas DataFrame (df.shape).
print(arr.shape) # (887, 3)
