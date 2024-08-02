"""
INHERITANCE (PEWARISAN)
"""

print("INHERITANCE (PEWARISAN)")

class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan

    def tambah_kecepatan(self):
        self.kecepatan += 10

class MobilSport(Mobil): # INHERITANCE
    def turbo(self):
        self.kecepatan += 50



# Kelas Mobil Dasar
mobil_1 = Mobil("Merah", "Ferari", 220)
print("Ini mobil biasa =",mobil_1.kecepatan)

print()

# Kelas Mobil Sport
mobil_sport_1 = MobilSport("Silver", "BMW", 220)
print("Ini mobil sport =",mobil_sport_1.kecepatan)
mobil_sport_1.turbo()
print("Ini mobil sport setelah mendapat turbo =",mobil_sport_1.kecepatan)
"""
PENJELASAN: jadi pada kodingan diatas kita telah membuat CLASS INHERITANCE pada baris kode
ke-16 yang dimana class ini mewarisi atribut pada class sebelumnya atau mewarisi variabel
pada class sebelumnya. variabel pada class sebelumnya ada "warna, merek, kecepatan" yang
diwariskan pada class selanjutnya "warna, merek, kecepatan". Walaupun sebenarnya objek 
yang telah dibuat dengan class "MobilSport" sebenarnya bisa mengakses method yang ada pada
class "Mobil" karna ini masih saling berhubungan. DENGAN MEMBUAT PEWARISAN ANDA DENGAN
MUDAH BISA MENAMBAHKAN (EXTEND) KEMAMPUAN DARI SUATU KELAS DENGAN FITUR YANG DIBUAT SENDIRI 
"""








