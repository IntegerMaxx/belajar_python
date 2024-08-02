"""
MEMFORMAT KODE
"""

print("MEMFORMAT KODE")
"""
PENJELASAN: jika proses linting menghasilkan pesan dengan menunjukkan baris dan kode yang
mengalami kesalahan, proses memformat kode akan memberikan pesan berupa kode yang telah
diperbaiki. Ini artinya Anda tidak perlu mengubah kode secara manual
"""


class Kalkulator:
    """kalkulator tambah kurang"""

    def __init__(self, _i):
        self.i = _i

    def tambah(self, _i):
        return self.i + _i

    def kurang(self, _i):
        return self.i - _i


"""
PENJELASAN: jadi pada sesi kali ini kita telah berhasil menginstal aplikasi "black" untuk
mengformat penulisan dari python. Untuk menginstalnya kita bisa menggunakan perintah
"pip install black" pada terminal dari Pycharm. "black" digunakan untuk mengatur penulisan
dari pada file python. Misalnya pada baris kode diatas fungsinya dibuat berhimpit, kemudian
fungsi tambah, style penulisannya dibuat seperti penulisan one-linear (satu baris). Kemudian
saat kita menjalankan perintah "black namaFile.py" dia akan langsung tertata secara otomatis,
jika terdapat kesalahan dalam penulisan dia akan langsung memberitahunya.

kita juga bisa menginstal autopep8 untuk melihat rekomendasinya di terminal, ketikan perintah
"pip install autopep8" untuk menginstal autopep8. Kemudian ketikan "autopep8 --in-place
--aggressive --aggressive namaFile.py" untuk memperbaiki baris kode (TIDAK EFEKTIF, LEBIH 
BAIK GUNAKAN BLACK)
"""
