"""
IMPLEMENTASI MATRIKS PADA PYTHON
"""
import numpy

print("IMPLEMENTASI MATRIKS PADA PYTHON")

# DEKLARASI MATRIX
print("\nDEKLARASI MATRIX")
# MATRIX SATUAN
print("\nMATRIX SATUAN")
matriks = [[1,0,1,0,1],
           [0,1,0,1,0],
           [1,0,1,0,1]]
print(matriks)

# MATRIX DEFAULT
print("DEKLARASI MATRIX dengan NILAI DEFAULT")
matriks2 = [[0 for j in range(4)] for i in range(3)]

print(matriks2)
"""
PENJELASKAN: Oke, jadi "matriks2" diatas akan menghasilkan matriks dengan nilai default nol "0".
Matriks nilai default dibuat dengan list comprehension yang dimana perulangan dalam "j" adalah
sebagai kolom dan perulangan luar "i" sebagai baris
"""

# AKSES ELEMEN MATRIX
print("\n\nAKSES ELEMEN MATRIX")
matriks3 = [[1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15],
            [16,17,18,19,20],
            [21,22,23,24,24,25]]
print(matriks3[2][1])
"""
PENJELASAN: jadi pada kodingan diatas kita mencoba untuk mengakses nilai di dalam array dengan
melakukan indexing. "matriks3[2][1]" = "matriks3" sebagai nama variabel yang menampung nilai
array, "[2]" sebagai baris (INGAT DISINI INDEXING DARI 0), lalu "1" sebagai kolom, dengan kata
lain kita mengakses nilai pada matriks3 dengan baris 2 dan kolom 1, sehingga menghasilkan output
nilai 12 
[PENJELASAN TAMBAHAN]
INGAT UNTUK MENDEKLARASIKAN MATRIX NUMPY. PENULISANNNYA HARIS BERURUTAN DARI NAMA VARIABEL 
KEMUDIAN ASSIGNMENT, LALU numpy.array(), KEMUDIAN KURUNG SIKU [[],[],[]], SETELAHNYA BARU
MENGISIKAN NILAI PADA MATRIX. KALAU KITA MENGIKUTI PROSEDUR INI PROGRAM AKAN ERROR
"""
print("\nDENGAN NUMPY")
matriks4 = numpy.array([[1,2,3,4,5],
                        [6,7,8,9,10],
                        [11,12,13,14,15],
                        [16,17,18,19,20],
                        [21,22,23,24,25]])

print(matriks4[2][3])








