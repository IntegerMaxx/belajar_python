import numpy
import sys
# di laptop ini belum terinstal numpy
"""
FUNDAMENTAL MATRIKS
"""

# FUNDAMENTAL MATRIKS
print("FUNDAMENTAL MATRIKS")
matriks = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

print(matriks)
"""
PENJELASAN: pada kode diatas adalah bagaimana mendeklarasikan array di dalam Python. Menggunakan
nested list sangat memakan memori. Oleh karena itu kita bisa menggunakan library NumPy. Library 
merupakan sekumpulan kode yang telah dibuat oleh developer atau programmer dan disediakan kepada
pengguna lain agar dapat digunakan ulang dalam pengembangan program atau perangkat lunak. 
Library merupakan sekumpulan kode yang telah dibuat oleh developer atau programmer dan 
disediakan kepada pengguna lain agar dapat digunakan ulang dalam pengembangan program atau 
perangkat lunak. 
"""


# import numpy
# import sys

var_list= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
var_array= numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("Ukuran keseluruhan elemen list dalam bytes = ", sys.getsizeof(var_list)*len(var_list))
print("Ukuran keseluruhan elemen NumPy dalam bytes = ", var_array.size*var_array.itemsize)
"""
PENJELASAN: NumPy tidak bisa menjalankan karena belum terinstal. kode diatas akan menampilkan
ukuran byte dari matriks yang telah kita buat sebelumnya. Ukuran "var_list" lebih besar 
karena tidak menggunakan numpy, ukuran "var_array" lebih kecil karena menggunakan numpy
"""





