"""
PERULANGAN
"""
print("PERULANGAN")
print("CONTROL PERULANGAN\n")


print("ELSE SETELAH WHILE")
count = 0

while count < 3:
    print("Hello world")
    count += 1
else:
    print("Blok else dieksekusi karena kondisi pada while salah (3<3 == False).")

"""
PENJELASAN: jadi saat masuk ke kedalam perulangan, karna count kurang dari 3 maka dia 
benilai true dan print hello world pun dieksekusi kemudian dilakukan penjumlahan satu
sehingga hasil count menjadi 1 kemudian hasil count dikembalikan lagi pada count yang ada 
dibaris 11, karna 1 kurang dari 3 maka perulangan diulang lagi sampai hasilnya keluar dari
3. Jika hasilnya sudah keluar dari 3 maka statement else akan dieksekusi dan mengprint
blok else dieksekusi.
"""

print("\nELSE SETELAH WHILE DENGAN BREAK")
n = 10
while n > 0:
    n = n - 1
    if n == 7:
        break
    print(n)
else:
    print("Loop selesai")
"""
PENJELASAN: jadi, karna nilai n itu lebih besar dari 0 maka dia bernilai true sehingga 
looping didalam while akan dieksekusi lalu variabel n akan dikurangi satu dan disimpan 
kembali pada variabel n. Looping terus dilakukan dan menampilkan nilai dari n, kemudian saat
masuk n ke 7 maka dia break sehingga tidak menampilkan nilai 7, karna dia break maka dia
keluar dari while dan tidak masuk di else. print yang ada pada baris kode ke 32 itu termasuk
bagian dari while BUKAN IF
[PENJELASAN TAMBAHAN]
Jadi while tersebut masih bernilai benar walaupun program keluar karena "break".
"""

print("\nPASS STATEMENT")
x = 10
while x > 5:
    pass
    break
else:
    print("Nilai x tidak memenuhi kondisi")
"""
PENJELASAN: jadi statement pass digunakan saat anda ingin sebuah blok pernyataan atau 
statement, tetapi tidak ada tindakan atau program tidak melakukan apapun. karna while tanpa
pass maka program akan error jika kita menginginkan while tanpa melakukan operasi apapun.
loopingannya juga tidak akan bernilai false.
[PENJELASAN TAMBAHAN]
jadi saat kita mengrunning program kemudian dia sampai pada statement pass, maka program itu
akan terus berjalan, jadi kita harus menambahkan break untuk membuatnya berhenti.
"""

print("\nLIST COMPREHENSION")
angka = [1,2,3,4]
pangkat = []
for n in angka:
    pangkat.append(n**2)
print(pangkat)
"""
PENJELASAN: jadi saat dilakukan looping. Looping akan masuk kedalam angka kemudian melakukan
looping di dalam variabel angka. Pangkat itu kan masih tidak ada isi. Kita akan mengisinya 
dengan menggunakan fungsi dari append(dengan catatan nilai yang sudah kita ambil pada 
variabel angka itu harus dipangkatkan) kemudian disimpan pada variabel pangkat. Ketika kita 
mengprint pangkat maka hasilnya adalah hasil perpangkatan dari variabel angka. Adapun cara
yang lebih mudah, pada contoh dibawah ini.
"""
angka = [1,2,3,4]
pangkat = [n**2 for n in angka] # inilah yang disebut list comprehension
print(pangkat)
"""
PENJELASAN: jadi "n**2" itu disebut sebagai expresion, kemudian "for n in angka" itu disebut
sebagai for loop one or more expression, intinya pada bagian ini kita menaruh looping yang
kita butuhkan.
hal ini memudahkan kita karna tidak perlu menggunakan fungsi tambahan seperti
append() untuk menambah nilai baru
"""
# INI ADALAH TUGAS
evenNumber = [0]
for i in evenNumber:
    i += 2
    if i > 500:
        break
    evenNumber.append(i)
print(evenNumber)
print(type(evenNumber))













