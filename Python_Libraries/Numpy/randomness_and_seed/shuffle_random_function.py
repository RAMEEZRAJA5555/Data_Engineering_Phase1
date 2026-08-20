#it shuffles the original array values

import numpy as np


arr = np.array([10, 20, 30, 40, 50])

np.random.seed(42)

np.random.shuffle(arr)

print(arr)