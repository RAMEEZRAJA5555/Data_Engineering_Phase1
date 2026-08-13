#Purpose: Learn how NumPy allows arrays of compatible shapes to work together, even when they are not exactly the same shape.

import numpy as np

# Broadcasting
# Broadcasting allows NumPy to perform operations between
# arrays with compatible shapes.


# Create a 2D array with 2 rows and 3 columns
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Create a 1D array with 3 elements
# Its shape is (3,)
b = np.array([10, 20, 30])


# NumPy broadcasts b across each row of a
# b is conceptually applied to both rows
result_add = a + b
print("Addition:")
print(result_add)


# Broadcasting also works with subtraction
result_sub = a - b
print("Subtraction:")
print(result_sub)


# Broadcasting also works with multiplication
result_mul = a * b
print("Multiplication:")
print(result_mul)


# Broadcasting also works with division
result_div = a / b
print("Division:")
print(result_div)