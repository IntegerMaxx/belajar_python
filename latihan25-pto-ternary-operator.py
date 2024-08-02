"""
PERCABANGAN DAN TERNARY OPERATOR
"""

# TERNARY OPERATOR
print("TERNARY OPERATOR")
lulus = True
print("Selamat\n") if lulus else print("Perbaiki\n")
"""
PENJELASAN: ternary operator itu kondisinya ditengah, jadi saat melihat kodingan ini. Kita
harus melihat di tengah dulu, untuk ,melihat kondisinya. Kode program diatas akan 
menampilkan pesan "Selamat" ketika kondisinya bernilai True dan menampilkan pesan "Perbaiki"
ketika kondisinya bernilai false. Kita juga bisa menulisnya seperti contoh kode dibawah ini.
Intinya ternari operator bentuk penyederhanaan dari if else.
"""
lulus = False
if lulus:
    print("Selamat")
else:
    print("Perbaiki")

# TERNARY OPERATOR DENGAN TUPLES
print("\nTERNARY OPERATOR DENGAN TUPLES")
lulus = True
kelulusan = ("Perbaiki, Anda belum lulus.", "Selamat, Anda lulus!") [lulus]
print(kelulusan)
"""
PENJELASAN: jadi untuk tuples ini kondisinya berada pada bagian akhir, sehingga hal yang
pertama kali kita lihat adalah akhir dari kode, untuk melihat kondisinya. Aksi pertama
benilai false dan aksi kedua bernilai true, berkebalikan dengan ternary operator 
sebelumnya atau if else statement sebelumnya. Bentuk lain dari ternary operator dengan
tuples ada pada contoh dibawah ini.
"""
lulus = True
if lulus:
    print("Selamat, Anda lulus!")
else:
    print("Perbaiki, Anda belum lulus.")
"""
[PENJELASAN TAMBAHAN]
Ternary operator dengan tuples ini sebaiknya dihindari, karena cukup membingungkan saat
meletakkan kondisi true atau false
"""
