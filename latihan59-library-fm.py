"""
LIBRARY FILE MANAGEMENT
"""
import os
print(os.getcwd())
"""
PENJELASAN: pada kodingan diatas kita telah berhasil mngimport library os, yang dimana kita
bisa menggunakannya untuk fungsi-fungsi yang berkaitan dengan sistem operasi, salah satu 
fungsinya sudah kita panggil diatas. Fungsinya untuk menglihat lokasi folder saat kita 
mengeksekusi file python ini "latihan59-library-fm".
"""


import json
data = '{ "nama":"Sunarto", "umur":22 , "Kota":"New York"}'
# parse data:
dataJSON = json.loads(data)
print(dataJSON['nama'])
"""
PENJELASAN: pada kodingan diatas kita telah berhasil mngimport library "json". "json" 
digunakan untuk mengtransmisikan berbagai sumber data tanpa khawatir bentuknya kacau
"""

import pickle
# contoh_dictionary = {1:"6", 2:"2", 3:"f"}
# pickle_keluar = open("dict.pickle","wb")
# pickle.dump(contoh_dictionary, pickle_keluar)
# pickle_keluar.close()

pickle_masuk = open("dict.pickle", "rb")
contohDictionary = pickle.load(pickle_masuk)
pickle_masuk.close()

print(contohDictionary)

"""
PENJELASAN: pada kodingan diatas kita telah berhasil mngimport library "pickle" dimana library
ini digunakan dengan tujuan untuk membuat file keluaran dan file masukkan. File yang dihasilkan
dari libray ini ber-Extention "pickle". 
"""


































