"""
CLASS, OBJECT DAN METHOD
"""

print("CLASS, OBJECT DAN METHOD")

# CLASS
print("CLASS")

class Mobil:
    pass

# CLASS DENGAN ATRIBUT
class Mobil2:
    # Atribut
    warna = "Merah"

# OBJECT
print("OBJECT")

class Mobil3:
    # Atribut
    warna = "Merah"

mobil_1 = Mobil3() # Instansiasi
print("\n",mobil_1.warna)
"""
PENJELASAN: pada kodingan diatas kita telah membuah sebuah objek. Di dalam Python untuk membuat
Object kita perlu memanggil nama kelasnya terlebih dahulu, kemudian disimpan pada sebuah objek
"Mobil3()" adalah pemanggilan nama classnya. "mobil_1" adalah pembuatan objek dari class. 
Untuk memanggil atribut dari objek. Yang pertama kali kita tuliskan adalah nama objek yang 
sudah dibuat kemudia atribut yang ingin dipanggil, contoh penulisannya seperti "mobil_1.warna"
"""

class Mobil4:
    # Atribut
    warna = "Merah"

mobil_1 = Mobil4() # Instansiasi
mobil_1.warna = "Biru"
print("\n",mobil_1.warna)
"""
PENJELASAN: pada baris kode diatas, kita berhasil mengubah nilai dari attribut "warna" yang 
ada pada objek "mobil_1" menjadi "Biru". Untuk objek sendiri, kita bisa menggunakan nama yang
sama dengan objek yang kita instansiasi sebelumnya.
"""

# ATRIBUT
print("\nATRIBUT")

class Mobil5:
    # Atribut kelas
    warna = "Merah"

mobil_1 = Mobil5()
print(mobil_1.warna)

mobil_2 = Mobil5()
print(mobil_2.warna)

# MENGUBAH ATRIBUT KELAS
Mobil5.warna = "Hitam"
print(mobil_1.warna)
print(mobil_2.warna)
"""
PENJELASAN: pada kodingan diatas kita telah berhasil mengubah nilai dari attribut "warna" yang
ada pada kelas "Mobil5" menjadi "Hitam". Untuk mengubahnya kita perlu memanggil nama kelas 
kemudian nama atribut lalu nilai yang inginkan, contoh penulisannya "Mobil5.warna = "Hitam"".
untuk mengeceknya kita menggunakan objek yang sudah kita instansiasi sebelumnya yaitu "mobil_1"
dan "mobil_2". Kita mengeceknya menggunakan print "print(mobil_1.warna)" lalu 
"print(mobil_2.warna)".
"""
























