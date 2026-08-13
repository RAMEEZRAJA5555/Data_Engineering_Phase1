import numpy as np

                                             # dtype and Memory
                                 # The same number of elements can use different amounts of memory
                                   # depending on the data type.


                                     # 1 million values stored as float64
big = np.ones(1_000_000, dtype=np.float64)       #it means creates a NumPy array containing 1,000,000 ones, where every value is stored as a 64-bit floating-point number.

                                     # 1 million values stored as float32
half = np.ones(1_000_000, dtype=np.float32)

                                # 1 million values stored as int8
tiny = np.ones(1_000_000, dtype=np.int8)


print("float64 memory:", big.nbytes / 1e6, "MB")
print("float32 memory:", half.nbytes / 1e6, "MB")
print("int8 memory:", tiny.nbytes / 1e6, "MB")


                                     # Check the data type of each array
print("\nData types:")
print("big:", big.dtype)
print("half:", half.dtype)
print("tiny:", tiny.dtype)