#it creates only integer random values

import numpy as np

np.random.seed(42)

#It generates random integers from 10 to 50.
#(10,51) meand 10 included and 51 excluded
#size=5 meand only 5 values 
result = np.random.randint(10, 51, size=5)

print(result)