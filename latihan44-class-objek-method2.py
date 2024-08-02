"""
CLASS, OBJECT DAN METHOD
"""

print("CLASS, OBJECT DAN METHOD")

# CLASS CONSTRUCTOR
print("\nCLASS CONSTRUCTOR")

class Mobil:
    # Atribut Instance
    def __init__(self):
        self.warna = "Merah" # ini akan dianggap sebagai nilai default sehingga saat pembuatan
                             # objek kodingan tidak akan error
mobil_1 = Mobil()
mobil_2 = Mobil()

print(mobil_1.warna)
print(mobil_2.warna)

# Mengubah atribut instance
mobil_1.warna = "Hitam"

# Menampilkan kembali atribut warna
print(mobil_1.warna)
print(mobil_2.warna)
"""
PENJELASAN: pada kodingan diatas kita telah berhasil mengubah warna yang berada pada fungsi
"__init__(self)" yang berada pada class "Mobil". keyword "self" merepresentasikan class itu
sendiri yakni "Mobil". Pada setiap pembuatan fungsi pasti akan ada parameter "self". 
"""

class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
mobil1 = Mobil("Kuning", "Ferari", 250)
print()
print(mobil1.warna)
print(mobil1.merek)
print(mobil1.kecepatan)
"""
PENJELASAN: pada kodingan diatas ita telah berhasil membuat sebuah objek dengan parameter
tambahan, yang dimana parameternya ini akan mengakses fungsi yang ada di dalam class.
Bearti saat membuat fungsi disebuah class dan menambahkan parameter selain parameter self
kita harus mengisi parameter tersebut saat melakukan instansiasi, contohnya pada baris ke-38
"mobil1 = Mobil("Kuning", "Ferari", 250)". Saat kita melakukan "print(mobil1)" Program akan
error
"""

# METHOD
print("\nMETHOD")
def my_decorator(func):
    def wrapper():
        print("Sebelum fungsi dieksekusi.")
        func()
        print("Setelah fungsi dieksekusi.")
    return wrapper

# Dekorasi fungsi dengan dekorator
@my_decorator
def say_hello():
    print("Hello, World!")

# Memanggil fungsi yang sudah didekorasi
say_hello()
"""
PENJELASAN: jadi pada kodingan diatas kita telah membuat method dekorasi intinya disini
mereka saling memanggil. Pertama kita menuliskan "def my_decorator" yang berarti sebuah
fungsi. kemudian kita menambahkan parameter "(func)". Lalu setelah fungsi dekorator dibuat
selanjutnya fungsi pembungkus yang kita buat di dalam fungsi dekorator "def wrapper():"
setelah kita kita melakukan print di dalam fungsi pembungkus. Lalu stelahnya kita 
menambahkan "func()", lalu setelahnya kita melakukan print lagi. Setelah semua prosedur
yang ada di fungsi pembungkus di tulis, kita keluar dari fungsi pembungkus kemudian 
mereturn atau mengembalikan nilai dari fungsi pembungkus tadi "return wrapper".
di baris selanjutnya kita akan mendefinisikan fungsi dekorator dengan penambahan simbol "@",
kita bisa menulisnya seperti "@my_dekorator", setelahnya kita membuat fungsi 
"def say_hello():" kemudian didalamnya kita menambahkan "print("Hello, World!")". Setelah
semua dilakukan kita melakukan pemanggilan "say_hello()" dan output mengeluarkan 
"Sebelum fungsi dieksekusi.
Hello, World!
Setelah fungsi dieksekusi."
[PENJELASAN TAMBAHAN]
sebenarnya "say_hello()" itu masuk ke dalam "func()" yang ada di dalam fungsi wrapper atau 
fungsi pembungkus kemudian di return untuk mengembalikan semua nilai yang ada di fungsi 
wrapper tadi "return wrapper"
"""








