import numpy as np
a = np.array([45, 12, 78, 23, 56])
a.sort()
print("\nThe array in ascending order is:", a)
print("\nThe array in descending order is:", a[::-1])
print("\nThe original array and the sorted array:", a, "\n", a[::-1])