import numpy

"""
OPERASI MATRIKS PADA PYTON
"""
print("OPERASI MATRIKS PADA PYTON")

# MATRIKS 2X2

matriks1 = [[5, 0],
           [1, -2]]
matriks2 = [[0 for j in range(2)] for i in range(2)]
print("\nmatriks1 sebelum dikalikan =",matriks1)
print("matriks2 sebelum dikalikan =",matriks2)
for i in range(len(matriks1)):
    for j in range(len(matriks1[0])):
        matriks2[i][j] = matriks1[i][j]*2

print("matriks2 setelah matriks1 dikali dengan konstanta 2 =", matriks2)
"""
PENJELASAN: jadi pada kodingan diatas kita telah melakukan perkalian "matriks1" dengan 
konstanta "2" yang selanjutnya hasilnya akan disimpan pada "matriks2". Cara kerjanya
adalah,pertama kita menginisialisasikan variabel "matriks1" dan "matriks2", kemudian 
dilakukan looping agar dapat dikalikan dengan konstanta. Pertama adalah looping luar yang
akan mengambil nilai dari "matriks1", yang bisa kita lihat pada tulisan "matriks[i][j]".
looping luar akan diulang sebanyak 4 kali sesuai panjangn dari "matriks1". Kedua adalah
looping dalam akan diulang sebanyak 2 kali sepanjang baris pertama pada "matriks1" 
kodingannya = "len(matriks1[0])". Didalam looping kedua atau looping dalam kita akan
mengisi "matriks2" yang sebelumnya kosong dengan nilai yang ada pada "matriks1" dikali
dengan 2. Saat looping dalam pertama kali dijalankan "matriks1[i][j]" akan menjadi
"matriks1[0][0]" yang berarti dia mengakses baris ke-1 dan kolom ke 1, selanjutnya karna
looping dalam masih bernilai true dikarenakan panjang (2) dari looping dalam masih 
memenuhi perulangan, maka perulangan selanjutnya akan menjadi "matriks1[0][1]", yang
berarti dia mengakses baris ke-1 dan kolom ke-2, karena looping selanjutnya sudah melebihi
maka dia keluar dari looping dalam. Looping luar masih memenuhi untuk melakukan looping,
sehingga looping luar dilakukan sekali lagi dan masuk ke looping dalam. nilai yang akan
diakses menjadi "matriks[1][0]" hingga seterusnya sampe keluar dari looping dalam dan luar.
Semua proses tadi disimpan pada "matriks2[i][j]". ADA CARA YANG LEBIH MUDAH DENGAN 
MENGGUNAKAN LIBRARY NUMPY
"""

print("\nDENGAN NUMPY")
matriks3 = numpy.array([[5,0],
                        [1,-2]])

hasil = matriks3 * 2
print("matriks3 setelah dikali dengan 2 =\n", hasil)












