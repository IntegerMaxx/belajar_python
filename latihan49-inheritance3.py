"""
INHERITANCE (PEWARISAN)
"""

print("INHERITANCE (PEWARISAN)")

print("Super\n")

class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10

class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50

    def tambah_kecepatan(self):
        super().tambah_kecepatan()
        print("kecepatan Anda meningkat! Hati-Hati!!")

mobil_sport_1 = MobilSport("Navy", "Honda Brio", 180)
mobil_sport_1.tambah_kecepatan()
print(mobil_sport_1.kecepatan)
"""
PENJELASAN: pada kodingan diatas kita telah berhasil memanggil fungsi, fungsi di dalam sebuah 
fungsi. Lihat pada baris kode ke-23 disitu kita memanggil fungsi "tambah_kecepatan()" pada
class induk hal ini bisa dilakukan dengan menggunakan fungsi "super()". Saat mengprint
yang akan terprint dluan adalah "print("kecepatan Anda meningkat! Hati-Hati!!")" itu 
dikarenakan saat masuk pada fungsi "tambah_kecepatan(self)" Python akan masuk pada 
"super().tambah_kecepatan()" yang setelahnya dia akan mencari fungsi "tambah_kecepatan()"
hal ini membutuhkan waktu sehingga sehingga fungsi "print("kecepatan Anda meningkat! Hati-Hati!!")"
ditampilkan lebih dahulu lalu setelah itu baru kecepatannya
"""












