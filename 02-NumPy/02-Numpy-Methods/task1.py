import numpy as np
a = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
print("First row of the array:", a[0])
print("Second column of the array:", a[:, 1])
print(a[1:3, 1:3])
print("Last two columns of the array:", a[:, 2:4])