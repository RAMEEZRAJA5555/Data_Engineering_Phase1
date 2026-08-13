#Purpose: Learn how to extract a portion of a NumPy array instead of accessing only one element.


import numpy as np


# Create a 1D NumPy array
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])


# Basic slicing
# Start at index 2 and stop before index 5
print(arr[2:5])


# Get the first three elements
print(arr[:3])


# Get elements from index 3 to the end
print(arr[3:])


# Get every second element
print(arr[::2])


# Get every second element starting from index 1
print(arr[1::2])


# Reverse the array
print(arr[::-1])


# Create a 2D NumPy array
table = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])


# Select the first two rows
print(table[:2, :])


# Select the first two columns
print(table[:, :2])


# Select rows 1 and 2
print(table[1:3, :])


# Select columns 1 and 2
print(table[:, 1:3])


# Select a smaller section of the table
# Rows 1 and 2, columns 1 and 2
print(table[1:3, 1:3])


# Create a 3D NumPy array
cube = np.arange(24).reshape(2, 3, 4)


# Select the first table
print(cube[0, :, :])


# Select the second table
print(cube[1, :, :])


# Select the first two rows from the second table
print(cube[1, :2, :])


# Select the first two columns from every row
print(cube[:, :, :2])


# Select a smaller section from the 3D array
print(cube[:, 1:3, 1:3])