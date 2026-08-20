
import numpy as np

# Seed makes random results reproducible.
# Same seed → same random results.

np.random.seed(42)
a = np.random.rand(5)

np.random.seed(42)
b = np.random.rand(5)

print("a:", a)
print("b:", b)

# Both are the same because we used the same seed.
print("Same results:", np.array_equal(a, b))

