"""
TIPE DATA COLLECTION LIST
"""

# LIST
"""
Jadi di dalam tipe data list ini kita tidak perlu looping untuk
melihat data yang ada di dalamnya. List itu mutable, artinya nilai
di dalamnya dapat berubah
"""
x = [1,True,3.0,"Hello World"]
print(x)
print(type(x))
print(x[3]) # Melihat index
print("=======MUTABLE=======")
x[1] = "Test" # >> MUTABLE ARTINYA DAPAT BERUBAH
x[3] = False # >> MUTABLE ARTINYA DAPAT BERUBAH
print(x[1],x[3])
print(x)
print("=======INDEXING=======")
"""
Jadi pada konsep indexing ini. Kita bisa mengambil nilai yang ada 
di dalam list berdasarkan index. Ingat indexnya dari nol 0. Contohnya
pada baris ke-31 sampai baris ke-32. Kemudian
jika kita menambahkan -1 maka dia akan mengambil nilai index 
yang paling terakhir, kalau -2 dia akan mengambil nilai index setelah 
nilai terakhir contohnya pada baris ke-33 sampai ke-34 
"""
x = ["Laptop","Mouse","Monitor","Mouse Pad", "Casing PC", "Keyboard", "Buku",]
print(x)
print(x[0])
print(x[1])
print(x[-1])
print(x[-2])
print("=======INDEXING SLICING=======")
print(x[0:7:3])
"""
print(x[0:7:3]), PENJELASAN: jadi 0 itu dia akan mengambil nilai index ke 0
kemudian 7 itu panjang dari index yakni sepanjang 7 index. 3 itu dia akan
mengambil nilai index yang ke 3 setelah 0 (0,1,2,3) index 3 yang akan diambil
kemudian dilanjutkan dengan mengambil nilai index ketiga selanjutnya (3,5,6)
index 6 yang akan diambil, jika masih ada index lagi, maka yang diambil adalah
index yang ke 9. Artinya perkalian 3
"""
print(x[1:])
"""
print(x[1:]), PENJELASAN: jadi 1: itu nilai yang diambil dari index ke 1 sampai
seterusnya (terakhir)
"""
print(x[:3])
"""
print(x[:3]), PENJELASAN: jadi :3 itu nilai yang diambil sebanyak 3 dimulai dari
index ke 0 sampai index ke 2
"""


# PENJELASAN EKSKLUSIF/INKLUSIF
"""
eksklusif itu dalam python, berarti rentang nilainya tidak ada misalnya a = 5; 
a > 5; hal ini akan error atau perogram tidak akan berjalan, karena a sama dengan 5
bukan lebih besar. inklusif dalam python, rentang nilainya termasuk misalnya a = 5;
a >= 5; hal ini akan membuat program berjalan, karena nilai a termasuk yakni lima
lebih besar sama dengan lima, masih masuk di sama dengan
"""


