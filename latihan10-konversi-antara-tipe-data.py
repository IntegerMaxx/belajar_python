"""
KONVERSI ANTARA TIPE DATA
"""

"""
PENJELASAN, untuk melakukan konversi kita bisa melakukannya seperti dibawah ini
atau langsung mengprintnya. saya akan menambahkan contoh print pada baris ke-13
"""
# KONVERSI INTEGER KE FLOAT
a = 5; c = 102
b = float(a)
print(b)
print(float(c))
print("")

# KONVERSI FLOAT KE INTEGER
a = -10.8888888; c = 3.2
b = int(a), int(c)
print(b)
print("")

# KONVERSI DARI TIPE DATA PRIMITIF YANG LAIN KE STRING
data1 = True; data2 = 20; data3 = 1.4; data4 = "Hello World"
simpanData = data1,data2,data3,data4
konversi = str(simpanData)
print(konversi) # >> Ini tipe datanya menjadi string
print(type(simpanData)) # >> Tipe datanya akan berubah menjadi tuple
print("")

    # CARA LAIN
print(int("25")) # Tadinya String sekarang menjadi int
print(str(25)) # Tadinya int sekarang menjadi string
print(float("25")) # Tadinya String sekarang menjadi float
print(str(25.6)) # Tadinya float sekarang menjadi string
print("")
"""
Maksud dari tanda petik dua yang ada di # CARA LAIN adalah itu mengubah tipe datanya
menjadi string
"""

# KONVERSI KUMPULAN DATA
print(set([1,2,3])) # tadinya list sekarang menjadi set
print(tuple({5,6,7})) # tadinya set sekarang menjadi tuple
print(list('hello')) # tadinya tuple sekarang menjadi list
print("")

# KONVERSI KUMPULAN DATA KE DICTIONARY
print(dict([[1,2],[3,4]])) # tadinya list sekarang menjadi dictionary
print(dict([(3,26),(4,44)])) # tadinya tuple sekarang menjadi dictionary
"""
pada baris ke-48, 1 dan 3 akan menjadi key, kemudian 2 dan 4 akan menjadi value
pada baris ke-49, 3 dan 4 akan menjadi key, kemudian 26 dan 44 akan menjadi value
"""
print("")
test1 = ('nama',"sunarto"), ('umur',30)
print(type(test1)) # Baris ini untuk melihat jenis data sebelum diubah
test2 = dict(test1)
print(type(test2)) # Baris ini untuk melihat jenis data setelah diubah
print(test2['nama']) # Baris ini untuk mengakses mengakses nilai pada key 'nama'

firstName = "Sunarto"
lastName = "Utina"
age = 20
isMaried = True
print(firstName,lastName,age,isMaried)