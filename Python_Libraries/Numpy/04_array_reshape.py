import numpy as np

                                          # Reshape
                        # This file demonstrates how reshape changes the structure
                          # of an array without changing the number of elements.

                        # Create a 1D array containing 12 elements
flat = np.arange(12)

print("Original array:")
print(flat)

print("Original shape:", flat.shape)
print("Original dimensions:", flat.ndim)
print("Original size:", flat.size)


                              # Reshape the 1D array into 3 rows and 4 columns
                              # 3 × 4 = 12, so the reshape is valid
grid = flat.reshape(3, 4)

print("\nReshaped to 3x4:")
print(grid)
print("New shape:", grid.shape)


                                 # Reshape the same 12 elements into 2 layers,
                                   # 2 rows, and 3 columns
                                    # 2 × 2 × 3 = 12
cube = flat.reshape(2, 2, 3)

print("\nReshaped to 2x2x3:")
print(cube)
print("New shape:", cube.shape)


                             # The number of elements must remain the same
print("\nOriginal size:", flat.size)
print("Grid size:", grid.size)
print("Cube size:", cube.size)