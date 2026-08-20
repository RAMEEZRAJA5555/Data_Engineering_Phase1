#it creates a shuffled copy

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

np.random.seed(42)

new_arr = np.random.permutation(arr)

print("Original:", arr)
print("New:", new_arr)