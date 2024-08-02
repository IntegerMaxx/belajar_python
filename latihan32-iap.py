"""
IMPLEMENTASI ARRAY DENGAN PYTHON
"""

# MENDEKLARASIKAN ARRAY
print("MENDEKLARASIKAN ARRAY")
var_list = [1,2,3]
for element in var_list:
    print(id(element))
"""
PENJELASAN: jadi pada kode diatas variabel list yang memiliki nilai dari indeks ke 0 sampai
indeks ke 2 akan di simpan pada memory. "print(id(element))" akan menampilkan id dari 
alokasi memori tersebut. Statement "element" adalah variabel yang akan menyimpan nilai dari
"var_list" setelah looping dilakukan. Id yang ditampilkan memiliki awalan nomor yang sama
tapi dengan akhiran yang berbeda, yang mengidikasikan bahwa penyimpanan nilai [1,2,3],
berada pada alokasi memory yang sama namun dengan penempatan yang berbeda
"""
# MENDEFINISIKAN ISI ARRAY
print("\nMENDEFINISIKAN ISI ARRAY")
var_arr1 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(var_arr1)
"""
PENJELASAN: jadi pada kodigan diatas akan menyimpan nilai array dengan panjang 10. Indeks 
ke-0 nya dimulai dengan nilai 9. Berakhir dengan indeks-9 dengan nilai 0
"""

# MENDEFINISIKAN NILAI DEFAULT
print("\nMENDEFINISIKAN NILAI DEFAULT")
var_arr = [0 for i in range(10)]
print(var_arr)
"""
PENJELASAN: jadi pada kodingan diatas itu kita mendefinisikan nilai default menggunakan
list komprehension yang nilainya itu semua nol sebagai nilai default dengan panjang 10,
berarti indeksnya dari 0 sampai 9
"""

array = [0 for i in range(10)]
print("\nNilai default sebelum dimasukkan nilai",array)
for i in range(10):
    array[i] = i

print("Nilai default setelah dimasukkan nilai",array)
"""
PENJELASAN: jadi pada kodingan diatas nilai default yang tdinya kosong "0" pada baris 37 itu 
telah diisi dengan nilai dari 0 sampai 9 yang panjangnya adalah 10 pada baris kode 39-40.
"array[i] = i" dimaksudkan bahwa variabel i pada for (baris kode-39) setelah dilakukan 
penjumlahan sebanyak satu kali selanjutnya disimpan pada variabel "array[i]"
"""

# MENGAKSES ELEMENT ARRAY
print("\nMENGAKSES ELEMENT ARRAY")
print("Nilai array pada indeks ke-0 =",var_arr1[0])













