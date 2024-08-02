"""
TRANSFORMASI ANGKA, KARAKTER, DAN STRING (AKS)
"""

# FORMATTING PADA STRING
print("FORMATTING PADA STRING")
print("")

print(".zfill")
kata = "hello"
print("sebelum di zfill", kata)
tambah_number = kata.zfill(7)
print("setelah di zfill",tambah_number)
"""
PENJELASAN: jadi .zfill itu dia akan menambahkan nilai nol pada awalan string sebelum kata hello
terdapat dua angka nol karena kita telah menambahkan zfill. Intinya zfill dia akan menambahkan angka
nol diawalan string. lihat pada contoh diatas fill yang ditambahkan sebanyak 7 fill, lihat kata hello
yang sebanyak 5 karakter, jadi kelebihan dua fill itulah yang akan benilai nol dan akan ditambahkan 
pada nilai string di sebelah kiri (awalan string). zfill ini memastikan panjang karakter mestinya 7
bukan 5
"""
print("")

print(".rjust")
kata = ("hello")
print("sebelum di rjust", kata)
tambah_number = kata.rjust(10)
print("setelah di rjust",tambah_number)
"""
PENJELASN: jadi .rjust itu akan menggeser kata hello ke kanan sesuai angka yang kita masukkan di .rjust
dengan catatan angkanya harus lebih banyak dari kata yang ada di variabel kata. ketika kita memasukkan
angka 10, maka outputnya akan menggeser kata hello sebanyak 5 kali ke kanan. Sebanarnya dia menambahkan
whitespace untuk menggeser kata hello ke kanan. kita juga bisa menambah karakter lain selain whitespace
(default). Contohnya pada kodingan dibawah ini
"""
tambah_number = kata.rjust(10,'*')
print("setelah di rjust menggunakan * =",tambah_number)
print("")

print(".ljust")
kata = ("hello")
print("sebelum di ljust", kata)
tambah_number = kata.ljust(10)
print("setelah di ljust",tambah_number)
"""
PENJELASAN: jadi .ljust itu dia akan menambahkan karakter setelah nilai string dengan tujuan membuat teks
menjadi rata kiri. intinya ini kebalikan dari .rjust. kita juga bisa menambahkan karakter lain selain white
space
"""
tambah_number = kata.ljust(10,'*')
print("setelah di rjust menggunakan * =",tambah_number)
print("")

print(".center")
kata = ("hello")
nilai = 11
print("sebelum di center", kata)
tambah_number = kata.center(nilai)
print("setelah di center",tambah_number)
"""
PENJELASAN: jadi .center ini bertujuan untuk membuat teks menjadi rata tengah berbeda dengan .rjust dan .ljust.
dengan .center terdapat whitespace di kiri dan whitespace di kanan. Kita juga bisa mengganti whitespace (nilai 
default) dengan karakter lain, contohnya ada pada kodingan dibawah ini.
"""
tambah_number = kata.center(nilai,'*')
print("setelah di center menggunakan * =",tambah_number)
print("")

"""
[PENJELASAN TAMBAHAN]
Sekali lagi, Anda harus ingat bahwa zfill(), rjust(), ljust(), dan center() berfungsi sama, yakni memastikan 
panjang teks sesuai dengan yang diminta dan harus lebih dari karakter yang ada di variabel bernilai string.
"""





