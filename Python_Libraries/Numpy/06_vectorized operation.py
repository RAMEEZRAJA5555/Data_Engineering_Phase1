#Purpose: Learn how NumPy performs an operation on all elements of an array without writing a Python for loop.

import numpy as np

# Create two NumPy arrays
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

# NumPy performs addition element-by-element
result_add = a + b
print("Addition:", result_add)

# NumPy performs subtraction element-by-element
result_sub = a - b
print("Subtraction:", result_sub)

# NumPy performs multiplication element-by-element
result_mul = a * b
print("Multiplication:", result_mul)

# NumPy performs division element-by-element
result_div = b / a
print("Division:", result_div)

# Multiply every element of the array by 2
result = a * 2
print("Array multiplied by 2:", result)