"""
STYLE GUIDE STATEMENT GABUNGAN
"""

# DISARANKAN SEPERTI INI
# if foo == 'blah':
#     do_blah_thing()
# do_one()
# do_two()
# do_three()

# TIDAK DISARANKAN SEPERTI INI
# if foo == 'blah': do_blah_thing()
# do_one(); do_two(); do_three()

# SANGAT TIDAK DISARANKAN SEPERTI INI
# if foo == 'blah': do_blah_thing()
# else: do_non_blah_thing()
# try: something()
# finally: cleanup()
# do_one(); do_two(); do_three(long, argument,
#                              list, like, this)
# if foo == 'blah': one(); two(); three()

# (PENGGUNAAN TRAILING COMMAS)
# DISARANKAN SEPERTI INI
FILES = ('setup.cfg',)

# TIDAK DISARANKAN SEPERTI INI
FILES2 = 'setup.cfg',

# DISARANKAN SEPERTI INI
# FILES = [
#     'setup.cfg',
#     'tox.ini',
#     ]
# initialize(FILES,
#            error=True,
#            )

# TIDAK DISARANKAN SEPERTI INI
# FILES = ['setup.cfg', 'tox.ini',]
# initialize(FILES, error=True,)




# (ANOTASI FUNGSI)
# Perhatikan penggunaan spasi dari kedua kode berikut.

# Yes: # DISARANKAN
# def munge(input: str):  # Menambahkan informasi parameter bertipe string
#     pass
# def munge() -> str:  # Menambahkan informasi return value bertipe string
#     pass
#
# No: TIDAK DISARANKAN
# def munge(input:str):  # Menambahkan informasi parameter bertipe string
#     pass
# def munge()->str:  # Menambahkan informasi return value bertipe string
#     pass
"""
PENJELASAN: anotasi fungsi itu untuk menjelaskan bagaimana dan apa seharusnya tipe data yang
diterima dari sebuah fungsi dengan penggunaan "->" dan ":". Pada contoh kode yang diberikan 
komentar diatas pada baris kode yang ke-54 ada perintah "-> str:" yang mengindikasikan bahwa
fungsi yang ada baris tersebut harus bertipe string. kemudian pada baris kode ke-52 ada 
perintah "input: str" yang mengindikasikan bahwa variabel "input" harus bernilai "str" atau
bernilai string. PERBEDAAN PADA BARIS KODE DIATAS TERLETAK PADA BERHIMPITNYA COMMAND ANOTASI
FUNGSI. CONTOH LAIN PENGGUNAAN ANOTASI FUNGSI PADA KODE PROGRAM DIBAWAH INI.
"""
def LuasPersegiPanjang(panjang: int = 2, lebar: int = None):
    luas = panjang*lebar
    return luas

luas_satu = LuasPersegiPanjang(lebar=2)
print(luas_satu)
"""
PENJELASAN: pada kode diatas kita telah melakukan anotasi fungsi "panjang: int" artinya 
variabel panjang harus integer, "lebar: int" artinya variabel lebar harus bertipe data integer
anotasi fungsi hanya bersifat optional atau hanya memberikan petunjuk. Jika pada kode diatas
kita mengubah anotasi fungsi menjadi ": str" itu tidak akan mempengaruhi program
"""

# Yes: DISARANKAN
def LuasPersegiPanjang(panjang=2, lebar=None):
    luas = panjang * lebar
    return luas


# No: TIDAK DISARANKAN
def LuasPersegiPanjang2(panjang = 2, lebar = None):
    luas = panjang * lebar
    return luas

"""
PENJELASAN: pada kodingan diatas, jika tidak menggunakan anotasi fungsi hindari penggunaan
spasi saat memberikan nilai default. Saat menggunakan anotasi fungsi sebaiknya kita 
menggunakan spasi yang jelas seperti pada baris kode ke-71
"""




