"""
FUNGSI
"""

print("===FUNGSI===")

print("FUNGSI ANONIM (LAMBDA EXPRESION)") # LAMDA EXPRESION

mencari_luas_persegi_panjang = lambda panjang, lebar: panjang*lebar
print(mencari_luas_persegi_panjang(5,3))

"""
PENJELASAN: fungsi lambda ini adalah fungsi one-liner nya Python. "mencari_luas_persegi_panjang"
ini dianggap sebagai nama fungsi walaupun setara dengan variabel, "lambda" merupakan statement
yang menunjukan kalau ini itu fungsi one-liner, "panjang, lebar" adalah argumen atau parameter
yang menerima masukan, "panjang*lebar" ini adalah operasi yang dilakukan sekaligus nilai yang
akan dikembalikan.
"""

print("\nVARIABEL GLOBAL DAN LOKAL")

print("VARIABEL GLOBAL")

a = 10 # VARIABEL GLOBAL
def tambahkan(b):
    hasil = a+b
    return hasil

bilanganPertama = tambahkan(20)
print(bilanganPertama)
"""
PENJELASAN: pada kodingan diatas kita telah melakukan pembuatan variabel global yang berada 
diluar dari fungsi, jadi kita bisa memanggil variabel global ini kedalam fungsi tambahkan
"""

print("\nVARIABEL LOKAL")

def tambahkan(a,b):
    variabel_lokal = 5 # VARIABEL LOKAL
    hasil = a+b-variabel_lokal
    return hasil

bilanganKedua = tambahkan(10,20)
print(bilanganKedua)
"""
PENJELASAN: jadi variabel lokal ini berada dalam fungsi dan kita hanya bisa menggunakannya 
selama masih berada dalam fungsi. Kita pun tidak bisa menggunakannya diluar dari fungsi utama
"""








