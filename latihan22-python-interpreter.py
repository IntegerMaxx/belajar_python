"""
PYTHON INTERPRETER
"""

# BLOCK CODE
"""
PENJELASAN: block code merupakan potongan baris-baris kode yang dijalankan
sebagai satu unit. Block kode dapat berupa modul, fungsi, control flow,
kelas, dan lain sebagainya. Contohnya kode dibawah ini, merupakan 
implementasi dari block kode. Kode yang ada dibawah merupakan perulangan,
bagian dari control flow
"""
# for i in range(10):
# print(i)
"""
[PENJELASAN TAMBAHAN]
jadi di python itu pemberian spasi atau tab akan sangat berpengaruh pada program
contohnya kode perulangan yang ada diatas. Saat baris kode ke-14 kita tab satu kali
program berjalan dengan normal, tapi saat kita hapus tabnya, program menjadi error.
Hal ini disebabkan karena "print(i)" akan dianggap sebagai bagian dari 
"for i in range(10):"
"""

# CASE-SENSITIVE
"""
PENJELASAN: python memperlakukan huruf besar atau huruf kecil sebagai karakter yang
berbeda dalam penulisan nama fungsi, variabel, atau seluruhan penulisan baris kode
secara umum. Contohnya pada kodingan dibawah ini. kedua variabel teks dianggap
berbeda karena terdapat perbedaan ukuran teks, baris kode-34 menggunakan variabel
"teks" yang semua hurufnya berkarakter sebagai huruf kecil, kemudian pada baris kode-35 variabel
"Teks" ditulis dengan awalan karakter sebagai huruf besar. Jadi karena perbedaan
itulah python menganggap kedua variabel ini berbeda
"""
teks = "Hello"
Teks = "World"
print(teks)
print(Teks)
