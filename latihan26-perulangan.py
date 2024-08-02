"""
PERULANGAN
"""

print("PERULANGAN")
"""
PENJELASAN: misalnya, kita ingin mencetak angka dari satu sampai sepuluh,
kita bisa melakukannya seperti dibawah ini. Tapi ini terlalu lama, dan
banyak memakan ruang
"""
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

# FOR
print("\nFOR")
var_list = [1,2,3,4,5,6,7,8,9,10]
for i in var_list:
    print(i)
"""
PENJELASAN: jadi didalam python itu terdapat objek yang iterable seperti tipe data
list, tuple hingga string. Pada kode program diatas, variabel i akan mengambil nilai
yang ada pada variabel var_list yang selanjutnya akan ditampilkan pada output program
"""

# FOR DENGAN RANGE
print("\nFOR DENGAN RANGE")
for i in range(10):
    print(i)
"""
PENJELASAN: jadi output yang dihasilkan adalah angka dari 0 sampai 9, yang 
mengindikasikan variabel i itu dari 0. Sementara range(10) itu artinya adalah panjang
dari sebuah iterasi yakni 10 yang dimulai dari 0 hingga 9. "range()" adalah fungsi 
bawaan dalam Python yang akan menghasilkan urutan bilangan dimulai dari indeks ke-0.
"""
print("")
for i in range(1,11,2):
    print(i)
"""
PENJELASAN: jadi range itu mempunyai start, stop, dan step. Dimana start itu artinya
iterasi akan dimulai dari angka ke-n. pada contoh diatas iterasi akan dimulai dari
angka ke-1. Stop itu artinya, iterasi akan berhenti jika bertemu dengan angka ke-n.
pada contoh diatas iterasi berhenti pada angka ke-11, artinya angka 11 tidak akan 
ditampilkan lagi, yang akan ditampilkan adalah angka dibawahnya (sebelum angka ke-11).
Step itu artinya penjumlahan, jadi saat saat masuk iterasi pertama angka pertama pada
iterasi akan dijumlahkan dengan Step. Pada contoh diatas kita menggunakan angka 2, 
artinya saat masuk iterasi ke-1 akan dijumlahkan dengan 2 dan menghasilkan 3, saat
masuk iterasi ke-2 yakni 3 akan dijumlahkan dengan 2 hasilnya 5, begitu seterusnya
sampai berhenti pada nilai yang telah kita berikan pada stop.
"""