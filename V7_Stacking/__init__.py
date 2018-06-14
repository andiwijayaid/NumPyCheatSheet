import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

# gabung secara horizontal
horizontal = np.hstack((a,b))
print("horizontal\n", horizontal)

# gabung secara vertical
vertical = np.vstack((a,b))
print("vertical\n", vertical)
