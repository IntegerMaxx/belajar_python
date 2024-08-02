"""
LIBRARY TEXT PROCESSING
"""


testString = "world"
print("Default =", testString)
# upper()
print("upper =",testString.upper())
# lower()
print("lower =",testString.lower())
# title()
print("title =",testString.title())
# split()
print("split =",testString.split("l"))
# zfill()
print(testString.zfill(20))


"""
REGEX
"""
import re

pola = "^H.........d$"
string_tes = "Hello World"
hasil = re.match(pola, string_tes)

if hasil:
    print("Pencarian berhasil.")
else:
    print("Pencarian gagal")

"""
PENJELASAN: pada kodingan diatas kita telah berhasil mengimport dan menggunakan library
RE atau REGEX atau Regular Expression. Library ini digunakan untuk mecari pola tertentu
pada sebuah teks. Misalnya pada contoh diatas kita mencari kata dengan awalan "H" dan
akhiran "d". Untuk fungsi "re.match()" jika kita ingin mencari diawalan kata, kita
harus menggunakan "^" untuk diakhiran kata kita menggunakan "$". *UNTUK MENGGUNAKAN
FUNGSI "re.match()" JUMLAH KARAKTER (POLA) HARUS SAMA DENGAN JUMLAH KARAKTER YANG
INGIN DICARI. Pada contoh diatas jumlah karakternya ada 11 kemudian untuk karakter
untuk mengecek polanya juga harus 11
"""


























