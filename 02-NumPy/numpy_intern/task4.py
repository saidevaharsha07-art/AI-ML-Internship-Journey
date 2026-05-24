import numpy as np
arr = np.random.randint(1, 50, (3, 3))
print("3D Array:")
print(arr)
print("Middle Element:", arr[1, 1])
print("First Row and Last Column :", arr[0], arr[:, 2])