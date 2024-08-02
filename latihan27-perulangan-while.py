"""
PERULANGAN
"""

print("PERULANGAN")
print("WHILE")

test = 1
while test <= 10:
    print(test)
    test += 1
"""
PENJELASAN: jadi while ini akan melakukan pengecekkan terlebih dahulu, jika sudah 
dilakukan pengecekkan dan bernilai true lalu dia akan melakukan aksi yakni "print(test)".
Karna dia masih bernilai true kode yang ada dibawahnya juga akan dieksekusi yakni 
"test += 1" (iterasi). Setelah dijumlahkan sebanyak satu kali, nilainya akan akan 
disimpan pada variabel test yang selanjutnya menjadi 2 dan dikembalikan pada varibel test
yang ada pada baris ke sembilan karna 2 kurang dari sepuluh berarti bernilai true, maka
proses print dan penjumlahan tadi akan terus dilakukan sampai nilainya keluar dari <=10
"""

# INFINITE LOOP
# counter = 1
# while counter <= 5:
#     print(counter)

# FOR BERSARANG
print("\nFOR BERSARANG")
for i in range(1,3):
    for j in range(1,3):
        print(i,j)
"""
PENJELASAN: jadi saat for pertama bernilai true, dia akan mengeksekusi for kedua yang ada
di dalam for pertama lalu menampilkan nilai dari for pertama dan for kedua (dengan syarat
for kedua harus selesai dulu loopingannya). 
"""


