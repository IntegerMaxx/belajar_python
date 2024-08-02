"""
FUNGSI
"""

print("===FUNGSI===")

print("\n====5 JENIS PARAMETER FUNGSI====")

print("POSITIONAL-OR-KEYWORD")
def sapa(nama, pesan):
    return "Halo " + nama + " ! " + pesan
sapa_dia = sapa("Sunarto", "selamat pagi")
print(sapa_dia)
"""
PENJELASAN: pada kode diatas kita membuat fungsi yang mengembalikan nilai yang kita inputkan 
dan juga nilai yang ada di dalam fungsi.
"""

print("\nPOSITIONAL-ONLY")
def penjumlahan(a,b,/):
    return a + b
ini_penjumlahan = penjumlahan(3 ,6)
print(ini_penjumlahan)
"""
PENJELASAN: pada kode diatas kita menambahkan parameter  "/" yang berarti fungsi ini hanya
bisa dilakukan dengan POSTIONAL-ONLY yang artinya ketika kita mengisikan nilai fungsinya
di baris 22 sebagai "penjumlahan( a=3 ,b=6)" maka program akan error penulisannya harus
seperti "penjumlahan(3 ,6)"
"""



print("\nKEYWORD-ONLY")
def sapa2(*,nama, pesan):
    return "Halo " + nama + " ! " + pesan
sapa_dia = sapa2(nama="Sunarto",pesan="selamat pagi")
print(sapa_dia)
"""
PENJELASAN: pada kode diatas kita menambahkan sintaks "*" yang berarti fungsi ini KEYWORD-ONLY.
saat pemanggilan nama fungsi kita harus menggunakan keyword seperti yang ada pada fungsi,
contoh penulisannya seperti ini " sapa2(nama="Sunarto",pesan="selamat pagi") ". Program akan
error ketika penulisannya seperti ini "sapa2("Sunarto","selamat pagi") ".
"""


print("\nVAR-POSITIONAL") # VARIADIC POSITIONAL PARAMETER
def hitung_total(*args):
    print(type(args))
    total = sum(args)
    return total
print(hitung_total(3,3))
"""
PENJELASAN: jadi pada kodingan diatas kita telah membuat sebuah fungsi yang menerima nilai
integer ataupun float, karena di dalam fungsi itu terdapat fungsi sum() jadi dia hanya 
akan menerima tipe data numerik. Walaupun sebenarnya dia bisa menerima tipe data apa pun itu.
Saat masuk kedalam fungsi argumen >> "args" langsung diubah menjadi tuple, walaupun hanya
satu inputan yang kita masukkan. "args" itu sebenarnya variabel yang menampung nilai dari 
masukkan tadi. Variabel dengan tipe data tuple. Yang membuat fungsi ini berbeda dengan 
fungsi lainnya adalah sintaks "*"
"""


print("\nVAR-KEYWORD") # VARIADIC KEYWORD PARAMETER
def cetak_info(**test):
    info = ""
    for key, value in test.items():
        info += key + ': ' + value + ", "
    return info
test5 = cetak_info(nama="Sunarto", umur="20", menikah="False")
print(test5)
"""
PENJELASAN: jadi pada fungsi diatas, itu adalah fungsi VARIADIC KEYWORD PARAMETER yang 
fungsinya seperti tipe data dictionary yang mengharuskan ada key dan value. Jadi dia akan 
mengambil nilai dari keyword yang kita masukkan dan di looping. Kemudian dikembalikan 
hasil atau nilai dari loopingannya.
"""



















