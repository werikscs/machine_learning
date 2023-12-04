"""More with numpy arrays."""

import pandas as pd
df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
arr = df[['Pclass', 'Fare', 'Age']].values

### Selecting elements from a numpy array.
# select a single element from a numpy array
print(arr[0, 1])
# select a row from a numpy array
print(arr[0])
# select a column from a numpy array
print(arr[:,2]) # all rows of the 3rd column

### Masking: is a way to filter the data in a numpy array
# all rows of the 3rd column where the value is less than 18
mask = arr[:, 2] < 18 # array([False, ..., False]). False mean adult and True mean child
# apply the mask to the array
print(arr[mask]) # we see that all the rows here are for passengers that are children
# we don't need to define the mask variable and can do the above in just a single line
print(arr[arr[:, 2] < 18]) # this is the same as the above

### Summing and Counting
mask = arr[:, 2] < 18 # True values are interpreted as 1 and False values are interpreted as 0

print(mask.sum())
print((arr[:, 2] < 18).sum())
