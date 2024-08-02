"""
LATIHAN ARRAY
"""

# MENCARI NILAI TERBESAR
print("MENCARI NILAI TERBESAR")
array = [1,7,2,89,3]
pointer_kiri = array[0]

for i in range(len(array)-1):
    pointer_kanan = array[i + 1]
    if pointer_kanan > pointer_kiri:
        pointer_kiri = pointer_kanan
    print(pointer_kiri)
"""
PENJELASAN: jadi pada odingan diatas kita melakukan pencarian nilai terbesar pada sebuah
array menggunakan konsep two pointers. Jadi pertama kita menginisialisasikan sebuah array
lalu membuat sebuah variabel "pointer_kiri" yang nilainya itu adalah indeks ke-0 dari array
yakni 1. Lalu kita membuat sebuah perulangan. Di dalam perulangan itu kita membuat variabel
"pointer_kanan" yang dimana dia akan menyimpan nilai dari index ke-2 dari sebuah array 
"array[i + 1]", Intinya index disebelah kanan. Lalu kita akan membandingkannya jika 
"pointer_kanan" lebih besar daripada "pointer_kiri" lakukan pembaruan nilai pada 
"pointer_kiri"
"""
var_arr = [1, 7, 2, 89, 3]
left_pointer = var_arr[0]

for i in range(1, len(var_arr)):
    right_pointer = var_arr[i]
    if right_pointer > left_pointer:
        left_pointer = right_pointer

print(left_pointer)
