"""
TRANSFORMASI ANGKA, KARAKTER, DAN STRING (AKS)
"""

# TRANSFORMASI HURUF BESAR/KECIL
print("TRANSFORMASI HURUF BESAR/KECIL")
kataKecil1 = "hello world"
kataBesar2 = "HELLO WORLD"
kataKecil3 = kataKecil1.upper()
kataBesar4 = kataBesar2.lower()
print("kata kecil sebelum diubah = ", kataKecil1)
print("kata kecil setelah diubah = ", kataKecil3)
print("\nkata besar sebelum diubah = ", kataBesar2)
print("kata besar setelah diubah = ", kataBesar4)

# AWALAN DAN AKHIRAN
print("\nAWALAN DAN AKHIRAN")
print(".rstrip()")
kata = "helo       "
print("sebelum di strip", kata)
kata1 = kata.rstrip()
print("setelah di strip", kata1)
print("")
"""
PENJELASAN: jadi rstrip() itu akan menghapus white space (spasi) yang ada di sebelah kanan
atau di ujung dari string lihat baris kode yang ke 19, kemudian lihat hasil printnya setelah 
kata hello sudah tidak ada character lagi
"""


print(".lstrip()")
kata = "            helo"
print("sebelum di lstrip", kata)
kata1 = kata.lstrip()
print("setelah di lstrip", kata1)
print("")
"""
PENJELASAN: jadi .lstrip() itu akan menghapus white space (spasi) yang ada di sebelah kiri,
kebalikan dari .rstrip()
"""


print(".strip()")
kata = "      helo       "
print("sebelum di strip", kata)
kata1 = kata.strip()
print("setelah di strip", kata1)
"""
PENJELASAN: jadi .strip() itu akan menghapus white space (spasi) yang ada di sebelah kanan
dan kiri, penggabungan dari .rstrip() dan .lstrip(). kita juga bisa menggunakan strip untuk
menghilangkan kata yang berulang, contohnya pada kodingan dibawah ini.
"""
kata = "Helo Helo Helo World Helo Helo Helo"
print("sebelum di strip", kata)
kata1 = kata.strip(" Helo ") # menggunakan spasi agar akurat
print("setelah di strip", kata1)
print("")

print(".startswith()")
kata = "Hello World"
print("sebelum di startwith", kata)
kata1 = kata.startswith("Hello")
print("setelah di startwith", kata1)
"""
PENJELASAN: .startswith() ini akan memeriksa apa kata kata "Helo" sesuai dengan nilai pertama
pada variabel kata, karena pada variabel kata, nilai pertamanya adalah "Helo", maka hasil dari
.startwith() akan menjadi True. Jika kata pertama pada variabel kata kita ubah menjadi halo, maka
dia akan menjadi false
"""
print("")

print(".endswith()")
kata = "Hello World"
print("sebelum di endswith", kata)
kata1 = kata.endswith("Hello")
print("setelah di endswith", kata1)
"""
PENJELASAN: .endswith() dia akan memeriksa nilai akhir dari sebuah string. Jika nilainya sama
maka hasil yang akan di keluarkan  adalah True, jika tidak sama maka hasilnya akan False. Sama
seperti dengan .startwith(), berbedaannya hanya terletak pada akhiran kata
"""

