"""
Style Guide, Prinsip Penamaan pada Python
"""
class MyClass:
    def __init__(self):
        self._private_var = 42   # Variabel non publik dengan awalan satu garis bawah
        self._secret_list = [1, 2, 3]  # Variabel non publik lainnya

    def _private_method(self):
        print("Ini adalah method non publik")

    def public_method(self):
        print("Ini adalah method publik")
        self._private_method()  # Method publik dapat memanggil method non publik

"""
PENJELASAN: Pada contoh di atas, method '_private_method' merupakan jenis fungsi yang tidak 
diakses secara langsung. Anda bisa melihat pada method 'public_method', tempat kita menggunakan
method private di sana. Selain itu, variabel seperti '_private_var' atau '_secret_list' merupakan
variabel non_publik yang tidak digunakan secara langsung ketika kelas dipanggil.

Method/Variabel publik dipersiapkan untuk pihak eksternal menggunakan kelas Anda. Anda juga
otomatis berkomitmen untuk menghindari adanya incompatible backward changes atau suatu kode yang
tidak dapat berjalan kembali setelah adanya perubahan. 

Sebaliknya, method/variabel dengan atribut non-publik hanya digunakan oleh Anda sebagai developer.
Itu juga tidak memberikan garansi kepada siapa pun bahwa Anda takkan mengubah atau menghapusnya.
Di sini kita tidak menggunakan atribut private karena dalam Python tidak ada atribut yang
benar-benar private.
"""