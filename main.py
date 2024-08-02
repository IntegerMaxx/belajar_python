# import hello
from hello import mencari_luas_persegi_panjang, nama
"""
MENULIS MODUL PADA PYTHON
"""

# persegi_panjang_pertama = hello.mencari_luas_persegi_panjang(5,10)
# print(persegi_panjang_pertama)
# print(hello.nama)

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)
print(nama)
"""
PENJELASAN: jadi pada kodingan diatas kita telah berhasil melakukan import dari sebuah modul
yakni "hello" yang telah kita buat sebelumnya. Pada baris kode yang ke-2 "from hello import 
mencari_luas_persegi_panjang, nama" kita mengimport fungsi dan variabel secara spesifika
atau kita menyebutkan nama fungsi dan variabelnya. Saat pemanggilan kita langgung memanggil
nama fungsi dan variabelnya bisa dilihat pada baris kode ke-11 dan ke-12. Berbeda dengan 
"import hello" kita harus memanggil nama modulnya contoh penulisannya pada baris kode ke-7 dan
ke-9, nama modul kemudian variabel atau fungsi yang ingin dipanggil
"""















