"""
DEFINISI SUBPROGRAM
"""

print("DEFINISI SUBPROGRAM")

print("\nMENCARI LUAS PERSEGI PANJANG")
# Luas pertama
panjang = 5
lebar = 10

luas_persegi_panjang = panjang * lebar
print(luas_persegi_panjang)

# Luas kedua
panjang = 4
lebar = 15

luas_persegi_panjang = panjang * lebar
print(luas_persegi_panjang)

"""
PENJELASAN: kode diatas dituliskan berulang kali, selain memakan waktu dan berulang ini 
juga bisa menyebabkan masalah. Bagaimana jika kita ingin mencari tahu luas persegi panjang
sebanyak 100x, tentu akan sangat merepotkan. Solusinya adalah dengan menyimpannya kedalam
sebuah fungsi, jadi kita tinggal memanggil nama sebuah fungsi dan mengisikan nilainya,
hal ini jauh lebih praktis daripada menulisnya berulang-ulang kali. Contohnya pada
kodingan dibawah ini
"""

print("\nDENGAN FUNGSI")
def mencari_luas_persegi_panjang(panjang,lebar):
    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)

persegi_panjang_kedua = mencari_luas_persegi_panjang(4,15)
print(persegi_panjang_kedua)



























































