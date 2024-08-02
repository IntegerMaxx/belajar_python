"""
FUNGSI
"""

print("===FUNGSI===")

def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)

persegi_panjang_kedua = mencari_luas_persegi_panjang(4,15)
print(persegi_panjang_kedua)

def mencari_luas_persegi_panjang1(panjang,lebar):
    """
    Fungsi ini digunakan untuk menghitung luas persegi panjang.

    Args:
        panjang (int): Panjang persegi panjang.
        lebar (int): Lebar persegi panjang.

    Returns:
        int: Luas persegi panjang hasil perhitungan.
    """
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang1(5,10)
print("\n",persegi_panjang_pertama)
"""
PENJELASAN: kode diatas menjelaskan tentang kode yang telah kita buat atau docstring,
atau dokumentasi. Komponen docsting diatas terdiri dari: Deskripsi, Arguments dan Returns.
Deskripsi menjelaskan tentang tujuan fungsi dibuat, Arguments menjelaskan tentang fungsi 
ini menerima inputan apa atau argumen yang diterima oleh fungsi, Returns menjelaskan 
tentang nilai apa yang akan dikembalikan setelah semua proses di dalam fungsi dilakukan
"""


print("\nKEYWORD ARGUMENT")
def mencari_luas_persegi_panjang2(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang2(lebar=10, panjang=5)

print(persegi_panjang_pertama)
"""
PENJELASAN: kode diatas merupakan penerapan dari keyword argumen dimana kita 
menginisialisasikan nilai setelah fungsi di deklarasikan. Penerapan pada baris kode 46:
"mencari_luas_persegi_panjang2(panjang=5, lebar=10)". Keuntungannya adalah kita tidak
perlu menuliskannya secara berurutan, python akan langsung mengetahui argumen yang 
dimaksud akan masuk kemana
"""































