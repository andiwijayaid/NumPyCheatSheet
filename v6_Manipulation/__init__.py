import numpy as np

a = np.array( ([1,2,3],
               [4,5,6]) )
print('matrix a dengan ukuran', a.shape)
print(a)

#transpose
matriksT = a.transpose()
print("Transpose\n", matriksT)

#menjadikan matriks menjadi vektor
print("jadi vektor\n", a.ravel())

#reshape matrix
print("reshape\n", a.reshape(3,2))

#resize matrix, sama dgn reshape tp nilai a diubah
print("resize\n", a.resize(3,2))
print("matriks a\n", a)