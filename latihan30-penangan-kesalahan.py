"""
PENANGANAN KESALAHAN (ERROR HANDLING AND EXCEPTION HANDLING)
"""

# KESALAHAN SINTAKS (SYNTAX ERRORS)
print("KESALAHAN SINTAKS (SYNTAX ERRORS)")

# CONTOH
# if 5 > 10:
# print("Hello world")
"""
PENJELASAN: jadi kode diatas akan menyebabkan error, dikarenakan tidak terdapat tab
pada fungsi print. Tab sendiri mengindikasikan bahwa statement yang di maksud masih
termasuk dari child statement dari parent statement. Parent statement pada kode diatas
adalah if
"""
# CONTOH 2
# i = 1
# while i<3
#     print("Hello world")
#     i += 1
"""
PENJELASAN: jadi pada contoh 2 diatas terdapat kesalahan penulisan. Diakhir "while i<3"
kita tidak menambahkan ":" sehingga menimbulkan SyntaxErrors. Tapi Python akan langsung
merekomendasikan bagaimana penulisan seharusnya dilakukan. Pada contoh 2 diatas Python
merekomendasikan titik dua ":" (expected ':').
"""

# PENGECUALIAN (EXCEPTIONS)
print("\nPENGECUALIAN (EXCEPTIONS)")

# CONTOH
# print(angka)
"""
PENJELASAN: pada contoh diatas kode program akan error dikarenakan "angka" tidak 
terdefinisikan sebagai apa, misalnya variabel ataupun objek. Tipe error yang terjadi
adalah "NameError" atau penamaan error.
"""

# CONTOH 2
# bukan_angka = '1'
# bukan_angka + 2

"""
PENJELASAN: jadi kode program pada contoh 2 diatas akan error dikarenakan string 
dijumlahkan dengan int, itu sama sekali tidak valid.
"""

# PENANGANAN PENGECUALIAN (HANDLING EXCEPTION)
print("\nPENANGANAN PENGECUALIAN (HANDLING EXCEPTION)")
# z = 0
# print(1/z)

# CONTOH
z = 0
try:
    print(1/z)
except ZeroDivisionError:
    print("Anda tidak bisa membagi angka dengan nol")

"""
PENJELASAN: pada kode diatas di statement "try" kode akan dicoba terlebih dahulu, jika 
tidak terjadi error kode akan tetap dieksekusi, namun jika terjadi error maka dia akan
menjalankan statement "except" yang selanjutnya mengprint "Anda tidak bisa....".
Pada kode diatas kita tidak bisa membagi 1 dengan 0 hasilnya error (ZeroDivisionError),
sehingga kita bisa mencobanya terlebih dahulu menggunakan "try", jika error dia akan 
menjalankan "except".
"""
print("")
# CONTOH 2

var_dict ={"rata-rata" : "1.0"}

try:
    print(f"Rata-rata adalah {var_dict["rata-rata"]}")
except KeyError:
    print("Key tidak ditemukan.")
except TypeError:
    print("Anda tidak bisa membagi nilai dengan tipe data string.")
else:
    print("Kode ini dieksekusi jika tidak ada exception.")
finally:
    print("Kode ini dieksekusi terlepas dari ada atau tidaknya exception.")

"""
PENJELASAN: pada kode diatas adalah penerapan exception handling secara lengkap pada
statement try kode akan dicoba jika terdapat error dia akan menjalankan statement 
except dibawah. "except KeyError" jika terdapat kesalahan penulisan key dari data 
collection dictionary. "except TypeError" akan dijalankan jika terjadi kesalahan 
operasi tipe data, misalnya integer dijumlahkan dengan string. statement "else" 
dieksekusi jika pada "try" berhasil dijalankan atau tidak terdapat error. statement
"finally" dijalankan jika semua statement diatas berhasil di jalankan
"""
print("")

# RAISE EXCEPTION
print("RAISE EXCEPTION")
var = -1
if var < 0:
    raise ValueError("Bilangan negatif tidak diperbolehkan")
else:
    for i in range(var):
        print(i+1)
"""
PENJELASAN: pada contoh kodingan diatas raise exception, Pertama ini bukan exception
handling hanya untuk mengatur logika pemrograman. Program tidak akan berjalan jika
terjadi error pada raise. Raise digunakan bersamaan dengan if statement. Raise 
statement digunakan untuk menampilkan pesan error berwarna merah yang berarti dari 
system
"""









