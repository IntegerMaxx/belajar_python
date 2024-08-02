"""
CLASS, OBJECT DAN METHOD
"""

print("CLASS, OBJECT DAN METHOD")

print("\nMetode dari Objek (Object Method)")

class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10

mobil_1 = Mobil("Hitam", "Ferari", 220)
print("Sebelum ditambahkan")
print(mobil_1.kecepatan)

mobil_1.tambah_kecepatan()          # Memanggil metode tambah_kecepatan

print("Setelah ditambahkan")
print(mobil_1.kecepatan)
"""
PENJELASAN: jadi pada kodingan diatas kita telah membuat class, objek, method yang dimana objek
yang telah kita buat telah dilakukan operasi penjumlahan Tepat dibaris 22. Sehingga hasil dari
print baris kode yang ke-25 sudah berbeda daripada print baris kode yang ke-20 
"""

print("\nMetode secara Statis (Static Method)")

class Mobill:
    def __init__(self, merek):
        self.merek = merek

    @staticmethod
    def intro_mobil():
        print("Ini adalah metode dari kelas Mobil")

Mobill.intro_mobil()
mobil1 = Mobill("Ferari")
mobil1.intro_mobil()
"""
PENJELASAN: jadi pada kodingan diatas kita bisa langsung memanggil method di dalam class
dengan menyebutkan nama method tersebut "Mobill.intro_mobil()". lalu kita juga bisa
memanggil method yaang ada di dalam dengan melalui objek yang telah kita buat 
"mobil1.intro_mobil()". SEMUA INI BISA KITA LAKUKAN KARENA METHOD YANG KITA PANGGIL ADALAH
METHOD STATIC, DENGAN PENAMBAHAN "@staticmethod" DI ATAS METHOD YANG INGIN KITA PANGGIL
AKAN MENJADIKAN METHOD TERSEBUT SEBAGAI METHOD STATIC yang artinya dia tidak akan memanggil
dirinya sendiri. "@" adalah keyword, "staticmethod" adalah fungsi tambahan dari python,
kita juga bisa membuatnya sendiri dari nama fungsi misalnya "@my_decorator" (lihat pada
modul latihan44)
"""


















