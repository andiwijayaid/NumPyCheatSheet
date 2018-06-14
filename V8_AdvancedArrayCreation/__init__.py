import numpy as np

#membuat matriks dengan tipe data tertentu
a = np.array(([1,2,3],[3,4,5]), dtype=float)
print(a)

#membuat array dengan menggunakan function
def kuadrat(baris, kolom):
    return kolom**2

def tambah(baris, kolom):
    return baris+kolom

b = np.fromfunction(kuadrat, (1,10), dtype = int)
c = np.fromfunction(tambah, (4,4), dtype = float)
print(b)
print(c)

# membuat array dengan menggunakan iterable
iterable = (x*2 for x in range(5))
d = np.fromiter(iterable, dtype = int)
print("iterable\n",d)