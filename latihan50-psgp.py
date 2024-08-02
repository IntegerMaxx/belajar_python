"""
PENGECEKAN STYLE GUIDE PEP8
"""

"""
PENJELASAN: PEP = Python Enhancement Proposal merupakan panduan yang telah menjadi acuan untuk
perkembangan python.
"""

# class Kalkulator:
#     """kalkulator tambah kurang"""
#     def __init__(self, _i):
#         self.i = _i
#     def tambah(self, _i): return self.i + _i
#     def kurang(self, _i):
#     return self.i - _i

"""
PENJELASAN: instal flake8 sebagai pengecekan style guide pada python, maksudnya adalah
aplikasi flake8 adalah aplikasi yang akan mengecek bentuk penulisan dari bahasa
pemrograman python. Bagaimana penulisan yang benar dan baik, aplikasi ini yang akan
mengeceknya. Sebelumnya kita install dulu dengan menggunakan perintah "pip install flake8"
pada terminal yang ada disini, di aplikasi ini (pycharm) BUKAN TERMINAL YANG ADA DI WINDOWS.
Setelah terinstal kita bisa melakukan mengecekan sintax yang salah atau kurang benar dengan
mengetikan perintah "flake8 latihan50-psgp.py".

setelah di cek aplikasi itu akan memberikan pesan kesalahan. Pesannya seperti dibawah ini:
".\latihan50-psgp.py:16:6: E999 IndentationError: expected an indented block after function
definition on line 15". ":16:6:" angka menunjukan letak kesalahannya 16 mewakili baris
kemudian 6 mewakili kolom, kalau kita lihat pada kode diatas dia berada pada baris 16
kemudian kolom 6 yang berarti perintah "return self.i - _i" terjadi kesalahan penulisan.
PESAN YANG DITAMPILKAN ADALAH "IndentationError" yang artinya terjadi kesalahan indentasi
atau terjadi kesalahan dalam penataan penulisan perintah
"""

class Kalkulator:
    """kalkulator tambah kurang"""

    def __init__(self, _i):
        self.i = _i

    def tambah(self, _i): return self.i + _i

    def kurang(self, _i):
        return self.i - _i
"""
PENJELASAN: saat kita menjalankan kode ini dengan perintah "lake8 .\latihan50-psgp.py". Akan
menampilkan banyak pesan error dikarenaka terdapat banyak komentar yang ada pada modul ini.
Tapi tidak apa-apa hal ini menunjukan bahwa "flake8" bekerja
"""



