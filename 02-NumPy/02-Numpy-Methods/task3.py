import numpy as np
a = np.array([
    [9, 3, 1],
    [8, 5, 2]
])
sorted_a = np.sort(a, axis=1)
print("Sorted 2D Array:")
print(sorted_a)