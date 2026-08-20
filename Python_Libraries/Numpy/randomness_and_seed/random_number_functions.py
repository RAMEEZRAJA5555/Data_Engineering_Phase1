#rand() only gives decimal numbers between 0 and 1
#we use seed to get the same random result we got before with the same seed 
#seed is used for reproducibility of random result


import numpy as np

np.random.seed(42)   #42 seed 

a=np.random.rand(6)

np.random.seed(42)   #same 42 seed again to get the same random result

b=np.random.rand(6)
print(a)
print(b)