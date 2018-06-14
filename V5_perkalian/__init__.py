import numpy as np

a = np.array(( [1,2],
               [3,4]))

b = np.ones([2,2])

print("matriks a\n", a)
print("matriks b\n", b)

dot1 = a.dot(b)    # cara 1
dot2 = np.dot(a,b) # cara 2
print("perkalian dot 1\n", dot1)
print("perkalian dot 2\n", dot2)

