#it choose the random values from the array

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

np.random.seed(42)


#size=3 means choose only 3 values from arr.
result = np.random.choice(arr, size=3)


print(result)

