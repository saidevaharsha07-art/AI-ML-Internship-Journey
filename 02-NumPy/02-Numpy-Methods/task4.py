import numpy as np
arr = np.array([10, 25, 30, 45, 50, 65])
print("Index positions of element greater than 40:",
      np.where(arr > 40))
print("Index positions of even number:",
      np.where(arr % 2 == 0))