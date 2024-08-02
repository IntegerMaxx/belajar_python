"""
TRANSFORMASI ANGKA, KARAKTER, DAN STRING (AKS)
"""

# PENGECEKAN STRING
print("PENGECEKAN STRING")
print(".isupper")
kata = "HELLO WORLD"
print("sebelum di isupper = ", kata)
print("setelah di isupper = ", kata.isupper())
"""
PENJELASAN: .isupper(), jika string yang ada di variabel kata semuanya berhuruf besar,
maka hasil dari .isupper() akan bernilai true. Intinya isupper akan mengecek nilainya
menggunakan huruf besar atau tidak, jika menggunakan huruf besar maka hasilnya true,
jika menggunakan huruf kecil maka maka hasilnya menjadi false
"""
print("")

print(".islower")
kata = "hello world"
print("sebelum di islower = ", kata)
print("setelah di islower = ", kata.islower())
"""
PENJELASAN: jadi .islower ini dia kebalikan dari .isupper(). jika string yang di cek 
semuanya berhuruf kecil maka hasilnya akan true, jika salah satu saja ada yang berhuruf 
besar maka hasilnya akan menjadi false 
"""
print("")

print(".isalpha")
kata = "hello world"
print("sebelum di isalpha = ", kata)
print("setelah di isalpha = ", kata.isalpha())
"""
PENJELASAN: .isalpha itu dia akan melihat nilai yang ada di dalam string jika terdapat
satu karakter saja yang bukan alpabet, misalnya; spasi, angka, dan simbol-simbol, maka dia
akan mengeluarkan hasil false. lihat di baris 32, terdapat spasi maka hasil dari .isalpha 
adalah false
"""
print("")

print(".isalnum")
kata = "hello123"
print("sebelum di isalnum = ", kata)
print("setelah di isalnum = ", kata.isalnum())
"""
PENJELASAN: .isalnum itu dia akan mengecek apa di variabel kata terdapat angka atau tidak.
jadi pengecekakkannya berurutan jika terdapat spasi atau simbol sebelum number maka dia akan
berhenti dan menghasilkan nilai false. Jika hanya terdapat huruf dan angka (tidak ada spasi 
atau simbol) maka hasilnya akan menjadi true
"""
print("")

print(".isdecimal")
kata = "55555"
print("sebelum di isdecimal = ", kata)
print("setelah di isdecimal = ", kata.isdecimal())
"""
PENJELASAN: .isdecimal itu dia akan mengecek apa di variabel kata terdapat nilai decimal atau 
tidak, jika terdapat salah satu saja nilainya bukan decimal (alpabet, spasi, dan simbol) maka
hasilnya akan false. Jika semua nilainya decimal maka hasilnya akan menjadi true
"""
print("")

print(".isspace")
kata = "      "
print("sebelum di isspace = ", kata)
print("setelah di isspace = ", kata.isspace())
"""
PENJELASAN: .isspace itu dia akan mengecek apa di variabel kata terdapat spasi,enter,newline atau tab.
intinya semua karakter yang mempunyai whitespace, hasilnya akan true. Jika terdapat simbol,huruf atau
karakter yang bukan whitespace maka hasilnya akan false
"""
print("")

print(".istitle")
kata = "Hello World 123"
print("sebelum di istitle = ", kata)
print("setelah di istitle = ", kata.istitle())
"""
PENJELASAN: .istitle itu dia akan mengecek apa di variabel kata diawalan katanya terdapat huruf besar.
Jika diawalan kata terdapat huruf besar maka hasil yang akan dikeluarkan akan bernilai true, jika ada
salah satu kata saja ada yang tidak mempunyai awalan kata berhuruf besar maka dia akan bernilai false.
simbol,angka dan whitespace akan diabaikan.
"""
print("")