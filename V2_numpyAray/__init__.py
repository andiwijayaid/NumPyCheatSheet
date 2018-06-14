import numpy as np

# membuat vector
vektor = np.array([1,2,3,4,5])
print("Vektor\n", vektor)
print("")

# membuat array
larik = np.array( [ (1,2,3,4,5),
                    (6,7,8,9,10) ])
print("Array\n", larik)
print("")

# membuat linespace (batas bawah, batas atas, banyaknya isi array)
linsSpace = np.linspace(1,10,4)
print(linsSpace)
print("")

# membuat matriks dengan range tertentu (batas bawah, batas atas, beda)
a = np.arange(1,10,2)
print(a)
print("")

#membuat matrix 0
nol = np.zeros((5,5))
print("Matrix nol\n", nol)
print("")

# membuat matrix 1
satu = np.ones((5,5))
print("Matriks satu\n", satu)
print("")

# membuat matrix identitas
i1 = np.identity(5)
i2 = np.eye(3)
print("Identitas dengan identity()\n", i1)
print("Identitas dengan eye()\n", i2)
print("")


