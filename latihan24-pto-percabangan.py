"""
PERCABANGAN DAN TERNARY OPERATOR
"""

# PERCABANGAN
print("PERCABANGAN")
ketersediaan = "Daging Ayam"

if ketersediaan == "Daging Ayam":
    print("Ibu membeli dan memasak ayam")
else:
    print("Ibu membeli dan memasak tempe")

"""
PENJELASAN: jadi di python juga terdapat pecabangan (if-else) penulisannya berbeda dengan
di java. Di python tidak perlu menulis kurung kurawa dan parameter, hanya perlu mengetikkan
titik dua untuk melihat aksinya. Contohnya seperti diatas
"""
print("")

print("IF")
score = 1
if score == 100:
    print("Nilai Anda sempurna!")

"""
PENJELASAN: if merupakan blok kode, begitupun dengan else, sehingga keduanya juga merupakan
blok kode ketika digabungkan.
"""
print("")

x = 0
if x:
    print("Ini True")
else:
    print("Ini False")

"""
PENJELASAN: kode diatas menjelaskan tentang, jika variabel x tidak memiliki nilai
ketika di kondisikan maka dia akan menghasilkan false. Jika dia memiliki satu saja karakter
dia akan menghasilkan true. Angka nol pun akan dianggap false yang menandakan tidak memiliki
nilai
"""
print("")

score2 = 100
if score2 == 100: print("Nilai anda sempurna!")
"""
PENJELASAN: if statement juga memiliki versi one-linear-nya. Contohnya pada baris kode 
diatas
"""
print("")

# ELSE
print("ELSE")

tinggi_badan = 120
print("Tinggi badan Anda =",tinggi_badan)
if tinggi_badan >= 160:
    print("Anda boleh menaiki roller coaster")
else:
    print("Anda tidak diperbolehkan menaiki roller coaster")

"""
PENJELASAN: else statement umumnya bersifat opsional, Umumnya, else statement digunakan 
ketika memiliki kondisi terakhir saat semua kondisi tidak terpenuhi
"""
print("")


# ELIF
print("ELIF")

nilai = 65
if nilai >= 80:
    print("Selamat! Anda mendapat nilai A")
    print("Pertahankan!")
elif nilai >= 70:
    print("Hore! Anda mendapat nilai B")
    print("Tingkatkan!")
elif nilai >= 60:
    print("Hmmm.. Anda mendapat nilai C")
    print("Ayo Semangat!")
else:
    print("Waduh, Anda mendapat nilai D")
    print("Yuk belajar lebih giat lagi")
"""
PENJELASAN: intinya elif itu seperti if tambahan untuk mengukur parameter nilai.
Program tetap akan dieksekusi secara sekuensial atau secara berurutan, dari if statement
pertama hingga terakhir
"""

# ELIF DENGAN OERATOR LOGIKA
print("\nELIF DENGAN OERATOR LOGIKA")
nilai = 81
perilaku = "Tidak baik"

if nilai >= 80 and perilaku == "Baik":
    print("Selamat! Anda mendapat nilai A dan telah berkelakuan baik")
    print("Pertahankan!")
elif nilai >= 80 and perilaku != "Baik":
    print("Kamu mendapat nilai A, tetapi perilaku Anda kurang baik")
else:
    print("Yuk belajar lebih giat lagi")
"""
PENJELASAN: jadi kita bisa menambahkan operator logika pada if statement, kemudian
menambahkan banyak elif
"""









