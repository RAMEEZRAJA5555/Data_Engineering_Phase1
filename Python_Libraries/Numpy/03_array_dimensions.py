import numpy as np


                                      #Array Dimensions
                            # This file demonstrates 1D, 2D, and 3D NumPy arrays.


                                          # 1D array
arr_1d = np.array([1, 2, 3, 4, 5])

print("1D Array:")
print(arr_1d)
print("Shape:", arr_1d.shape)
print("Dimensions:", arr_1d.ndim)


                                       # 2D array
arr_2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\n2D Array:")
print(arr_2d)
print("Shape:", arr_2d.shape)
print("Dimensions:", arr_2d.ndim)


                                              # 3D array
                                   # 2 layers × 2 rows × 2 columns
arr_3d = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

print("\n3D Array:")
print(arr_3d)
print("Shape:", arr_3d.shape)
print("Dimensions:", arr_3d.ndim)
print("Total elements:", arr_3d.size)