import numpy as np
arr = np.array( [[5, 10, 15],[20, 25, 30],[35, 40, 45]])
print("Print 10:",arr[0,1])
print("Print 30:",arr[1,2])
print("Print 35:",arr[2,0])
print("Diagonal Elements :",arr.diagonal())
print("Last Row :",arr[2])