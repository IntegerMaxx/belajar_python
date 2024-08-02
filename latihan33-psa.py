"""
PEMROSESAN SEKUENSIAL PADA ARRAY
"""
print("PEMROSESAN SEKUENSIAL PADA ARRAY")
array = [20,30,10,50,40]

for i in range(len(array)):
    nilai_saat_ini = array[i]
    index_selanjutnya = i+1

    if index_selanjutnya < len(array):
        elemen_selanjutnya = array[index_selanjutnya]
    else:
        elemen_selanjutnya = None

    print(f"nilai saat ini: {nilai_saat_ini}, elemen selajutnya {elemen_selanjutnya},")
"""
PENJELASAN: jadi pada kodingan diatas kita telah melakukan perosesan sekuensial pada array,
atau pemrosesan secara berurutan dari indeks yang ke-0 sampai indeks yang terakhir.
for akan dilakukan sampai 5 kali karna panjang dari array adalah 5. variabel "nilai_saat_ini"
menampung nilai dari array yang sudah di iterasi oleh variabel i, artinya saat iterasi 
dilakukan pertama kali berarti nilai 20 atau elemen pertama pada array sudah masuk. Lalu
pada variabel "index_selanjutnya" akan menyimpan nilai iterasi tadi kemudian dijumlahkan dengan
satu, iterasi disini berupa angka dari 0 sampai 5 (angak 5 sesuai panjang dari array), jadi yang
disimpan adalah angka 1 karna 0 + 1 = 1. Lalu pada stetment if terdapat parameter yang diisi variabel 
"index_selanjutnya" kurang dari panjang array maka simpan variabel "array" yang sudah dimasuki
"index_selanjutnya" pada "elemen_selanjutnya" jika sudah tidak relevan dengan if panjangnya
lakukan else, yang berarti "elemen_selanjutnya" menjadi none.
Setelah semua proses dilakukan jalankan print. ini adalah print f dimana kita bisa memasukkan variabel
di dalamnya dan bisa juga melakukan operator
"""