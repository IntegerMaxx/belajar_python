"""
TODO:
Sebuah variabel array diberikan dengan ketentuan berikut.
- Variabel array bernama "var_array" dengan nilai dari 0 hingga 100.
- Hitung nilai rata-rata dari elemen array tersebut.
- Simpan hasil perhitungan dalam variabel bernama "result".

Tips:
- Rumus menghitung rata-rata adalah jumlah seluruh elemen dibagi banyaknya elemen.
- Gunakan percabangan dan perulangan untuk mempermudah,
  Anda tidak diperbolehkan memberikan nilai secara langsung.
"""

# var_array = [i for i in range(6)]
# index= 0
# sum= 0
# panjang= len(var_array)
# while index< panjang:
#     sum += var_array[index]
#     index += 1
#     print(sum)
#
# result = sum/panjang
# print(result)

array = [i for i in range(101)]
jumlahkan = 0

for i in range(len(array)):
    jumlahkan += array[i]

result = jumlahkan / len(array)
print(result)









