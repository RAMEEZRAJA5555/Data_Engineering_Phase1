#It teaches how NumPy calculates summary values from an array, such as the total, average, minimum, and maximum.

import numpy as np


# Create a NumPy array of marks
marks = np.array([60, 70, 80, 90, 100])


# Calculate the total of all elements
total = np.sum(marks)
print("Sum:", total)


# Calculate the average of all elements
average = np.mean(marks)
print("Mean:", average)


# Find the smallest value
minimum = np.min(marks)
print("Minimum:", minimum)


# Find the largest value
maximum = np.max(marks)
print("Maximum:", maximum)


# Find the position of the smallest value
minimum_index = np.argmin(marks)
print("Index of minimum:", minimum_index)


# Find the position of the largest value
maximum_index = np.argmax(marks)
print("Index of maximum:", maximum_index)