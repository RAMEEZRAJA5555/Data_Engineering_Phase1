#Purpose: Learn how to access a specific element of a NumPy array.

import numpy as np

# Create a 1D array
arr = np.array([10, 20, 30, 40, 50])

# Access the first element
print(arr[0])

# Access the third element
print(arr[2])

# Access the last element
print(arr[-1])


# Create a 2D array
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

# Access the element at row 0, column 1
print(matrix[0, 1])

# Access the element at row 1, column 2
print(matrix[1, 2])

# Change an element
matrix[0, 1] = 99

print(matrix)