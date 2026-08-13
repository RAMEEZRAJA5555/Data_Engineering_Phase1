#Purpose: Learn how to extract a portion of a NumPy array instead of accessing only one element.


import numpy as np

# Create a 1D array
arr = np.array([10, 20, 30, 40, 50])

# Get elements from index 1 up to index 4
print(arr[1:4])

# Get the first three elements
print(arr[:3])

# Get elements from index 2 to the end
print(arr[2:])

# Get every second element
print(arr[::2])


# Create a 2D array
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Get the first two rows
print(matrix[:2])

# Get the first two columns
print(matrix[:, :2])

# Get rows 1 and 2, and columns 1 and 2
print(matrix[1:3, 1:3])