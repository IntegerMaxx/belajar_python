"""
FUNDAMENTAL ARRAY
"""
import array


x = [1,2,3,4,5]
print(x,type(x))
"""
PENJELASAN: pada python tidak terdapat tipe data array seperti yang ada di java atau bahasa
pemrograman lainnya. kita bisa menggunakan tipe data list atau tuple sebagai penggantinya
seperti pada contoh diatas. Tapi kita juga bisa menggunakan array dengan mengimport library
dari array 
"""

y = array.array("i",[1,2,3,4,5])
print(y)
print(type(y))

# PROSES REKAP NILAI
nama_siswa1 = 90
nama_siswa2 = 100
nama_siswa3 = 50
nama_siswa4 = 80
nama_siswa5 = 85
nama_siswa6 = 45
nama_siswa7 = 80
nama_siswa8 = 75
nama_siswa9 = 50
nama_siswa10 = 60

print(nama_siswa1)
print(nama_siswa2)
print(nama_siswa3)
print(nama_siswa4)
print(nama_siswa5)
print(nama_siswa6)
print(nama_siswa7)
print(nama_siswa8)
print(nama_siswa9)
print(nama_siswa10)
"""
PENJELASAN: pada kodingan diatas terdapat nilai siswa yang di Imputkan satu persatu.
alih-alih membuat variabel setiap kali ada siswa baru, Kita bisa membuatnya pada sebuah
list untuk mempermudah. Contoh pada kodingan dibawah ini
"""
siswa = [90, 100, 50, 80, 85, 45, 80, 75, 50, 60]

print(siswa)
print(siswa[0])