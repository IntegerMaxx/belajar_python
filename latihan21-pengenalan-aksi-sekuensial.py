"""
PENGENALAN AKSI SEKUENSIAL
"""

# print("PENGENALAN AKSI SEKUENSIAL")
# print("Selamat datang di Program Python\n")
# print("Silahkan masukkan data diri anda.")
# nama = input("Masukkan nama anda: ")
# tahunlahir = input("masukkan tahun lahir anda: ")
# umur = 2024 - int(tahunlahir)
#
# print(f"Selamat datang {nama} di program Python,per 2024 umur anda adalah {umur} tahun.\n")
# print("Terima kasih, telah menggunakan program ini")
"""
PENJELASAN: jadi input() untuk menerima input dari pengguna, dan menyimpannya dalam 
sebuah variabel. Contohnya pada variabel nama yang ada pada baris 8.
[PENJELASAN TAMBAHAN]
jadi program diatas menggambarkan, bahwa program akan dieksekusi secara berurutan dimulai
dari baris yang paling atas dan berakhir pada baris yang paling bawah
"""
print("")

# URUTAN INISIALISAI
a = 6
b = 9
result = a + b
print("Sebelum diubah",result)
result2 = b + a
print("Setelah diubah",result2)
print("Hasil Tidak ada yang berubah")
print("")

a1 = 6
b1 = 9
print("Sebelum diubah",a1**2) # artinya 6 dikali sebanyak 2 kali bisa ditulis 6*6
print("Sebelum diubah",b1//3) # artinya 9 dibahagi dengan 3, hasilnya 3

print("\nSetelah diubah",b1//3) # artinya 9 dibahagi dengan 3, hasilnya 3
print("Setelah diubah",a1**2) # artinya 6 dikali sebanyak 2 kali bisa ditulis 6*6
"""
PENJELASAN: jadi ada kode yang kalau di print hasilnya tidak akan berubah, seperti
pada contoh kode dari baris 24 sampai 29, walaupun kita menukarkan print tersebut,
hasilnya akan tetap sama dan jika operannya juga kita tukar hasilnya tetap sama.
Berbeda pada baris kode 33 sampai 39, saat printnya dibalik maka hasil yang di 
tampilkan juga ikut berubah.

"""
