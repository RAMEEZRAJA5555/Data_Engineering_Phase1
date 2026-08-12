import numpy as np

                                        #Array Inspection
                              #This file checks the structure and properties of a NumPy array.

arr = np.array([
    [80, 70, 90],
    [60, 75, 85]
])

print("Array:")
print(arr)

                                      #shape → number of rows and columns
print("\nShape:", arr.shape)

                                        # ndim → number of dimensions
print("Dimensions:", arr.ndim)

                                        # size → total number of elements
print("Total elements:", arr.size)

                                        # dtype → data type stored in the array
print("Data type:", arr.dtype)

                                       # nbytes → memory used by the array data
print("Memory used (bytes):", arr.nbytes)