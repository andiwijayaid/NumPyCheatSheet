import numpy as np

# hasil jumlah list Python
a = [1,2,3,4,5]
b = [6,7,8,9,10]
print("List python\n", a + b, "\n") #akan menambahkan isi array, bukan menjumlahkan isi a dan b

# list NumPy

#mengalikan isi matriks sesuai index
numA = np.array([1,2,3,4,5])
numB = np.array([6,7,8,9,10])
print(numA*numB)

# namun jika kita menggalikan array multi dimensional, maka numpy tidak mengembalikan nilai perkalian dengan metode matriks
# melainkan hanya mengalikan antar index
mulA = np.array( [ (1,2,3,),
                   (5,6,7),
                   (4,8,1)])
mulB = np.array( [ (2,6,4),
                   (1,5,6),
                   (8,4,1)])
print("\n", mulA*mulB)