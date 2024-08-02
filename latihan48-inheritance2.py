"""
INHERITANCE (PEWARISAN)
"""

print("INHERITANCE (PEWARISAN)")

print("Override")
class Mobil: # CLASS INDUK
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):        # tambah_kecepatan
        self.kecepatan += 10

class MobilSport(Mobil):

    def turbo(self):
        self.kecepatan += 50

    def tambah_kecepatan(self):        # tambah_kecepatan
        self.kecepatan += 20

# Kelas Mobil Sport
mobil_sport_1 = MobilSport("Merah", "Ferari", 220)
print("Sebelum ditambah kecepatan =",mobil_sport_1.kecepatan)
mobil_sport_1.tambah_kecepatan()       # Memanggil metode baru tambah_kecepatan()
print("Setelah ditambah kecepatan =",mobil_sport_1.kecepatan)
"""
PENJELASAN: pada kodingan diatas kita telah berhasil membuat kelas pewarisan inheritance 
class dengan override. Yang artinya berhasil menimpa fungsi yang sudah kita buat pada 
class sebelumnya yakni "def tambah_kecepatan(self):". fungsi yang ada pada class sebelumnya
tidak berubah dia tetap ada selama kita ingin memanggilnya. Perlu dipahami MENIMPA BUKAN
BERARTI MENGUBAH METODE DARI CLASS INDUK
"""

print()

# Kelas Mobil Dasar
mobil_1 = Mobil("Putih", "Avanza", 120)
print(mobil_1.kecepatan)
mobil_1.tambah_kecepatan()
print(mobil_1.kecepatan)
"""
PENJELASAN: lihat kita kita berhasil membuat objek "mobil_1", walaupun kita sudah memanggil
fungsi "tambah_kecepatan()" kecepatannya tidak bertambah 20 padahal kita mempunyai fungsi 
pewarisan pada class MobilSport. ITU DIKARENAKAN KITA MENGAMBIL METHOD DARI KELAS YANG 
BERBEDA
"""














