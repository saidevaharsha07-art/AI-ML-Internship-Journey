import numpy as np
arr = np.array([5, 12, 18, 21, 30, 42])
print("Number divisible by 3:",
      arr[np.where(arr % 3 == 0)])
print("Number greater than 20:",
      arr[np.where(arr > 20)])