#Purpose: Learn how to access a specific element of a NumPy array.

import numpy as np


# Create a 1D NumPy array
arr1d = np.array([10, 20, 30, 40, 50, 60, 70, 80])


# Access an element using its index
print(arr1d[0])


# Access an element using a negative index
# -1 means the last element
print(arr1d[-1])


# Create a 2D NumPy array
table = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])


# Access an element using row and column
# First value is the row, second value is the column
print(table[1, 2])


# Access the complete first row
print(table[0, :])


# Access the complete third column
print(table[:, 2])


# Access a specific row
print(table[1])


# Create a 3D NumPy array
# Shape: (2, 3, 4)
# 2 tables, 3 rows in each table, 4 columns in each row
cube = np.arange(24).reshape(2, 3, 4)


# Access one specific element from the 3D array
# Order: depth, row, column
print(cube[1, 2, 3])


# Access one complete row from the second table
print(cube[1, 2, :])


# Access one complete column from the second table
print(cube[1, :, 2])


# Create a Boolean condition
scores = np.array([45, 72, 88, 31, 95, 60])


# Compare every element with 70
# The result is an array of True and False values
condition = scores > 70
print(condition)


# Use the Boolean condition to select matching elements
print(scores[scores > 70])


# Create an array of indexes
indices = np.array([0, 2, 4])


# Select elements using the given indexes
# This is called fancy indexing
print(scores[indices])