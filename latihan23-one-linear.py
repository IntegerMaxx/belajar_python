"""
ONE LINEAR
"""

x = 10
y = 2

temp = x
x = y
y = temp
print("Setelah pertukaran: ")
print("x =",x)
print("y =",y)
"""
PENJELASAN: jadi kode diatas mengindikasikan one linear. Bada awal inisialisasi "x" 
bernilai 10 dan "y" bernilai 2. Dibuat satu variabel penampung "temp" yang menampung 
nilai dari "x", lalu variabel "x" menampung nilai dari variabel "y", lalu variabel "y" 
menampung nilai dari variabel "temp" yang terdapat nilai dari variabel "x". Intinya
pada kode program ini terjadi pertukaran. Hal ini terjadi karena aksi sekuensial, dimana
program dieksekusi baris perbaris
"""
print("")

# CONTOH LEBIH SEDERHANA
a = 1
b = 2
a, b = b, a # One-linear

print("Setelah pertukaran: ")
print("a =",a)
print("b =",b)