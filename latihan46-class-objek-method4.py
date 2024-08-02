"""
CLASS, OBJECT DAN METHOD
"""

print("CLASS, OBJECT DAN METHOD")

print("\nMetode dari Kelas (Class Method)")

class Mobil:
    def __init__(self, merek):
        self.merek = merek

    @classmethod
    def intro_mobil(cls):
        print("Ini adalah metode dari kelas Mobil")


Mobil.intro_mobil()
Mobil_1 = Mobil("Ferari")
Mobil_1.intro_mobil()

"""
PENJELASAN: pada bagian fungsi/method dari "intro_mobil(cls)", kita menambahkan "cls" karena
"cls" adalah parameter wajib dalam menggunakan dekorator "classmethod"
"""
print()


class Mobil:
    def __init__(self, merek):
        self.merek = merek

    @classmethod
    def intro_mobil(*args):
        print(args)


Mobil.intro_mobil()
mobil_1 = Mobil("Ferari")
mobil_1.intro_mobil()
"""
PENJELASAN: lihat hasil output dari python "(<class '__main__.Mobil'>,)", yang menunjukan 
bahwa method ini adalah method utama dari "class Mobil". Ini membuktikan bahwa ketika Anda
menggunakan class method, Python akan secara otomatis menambahkan kelas tersebut sebagai 
argumen pertama.
"""






