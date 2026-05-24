import numpy as np
arr = np.array([[78, 85, 90, 88],[67, 72, 80, 76],[90, 91, 89, 95]])
print("Marks of Student 1 :", arr[0])
print("Marks of Subject 3 :", arr[:,2])
print("The highest mark from the array:", np.max(arr))