"""
JENIS-JENIS OPERATOR
operator aritmatika,operator relasional,
operator logika, operator asiggnment
"""

# OPERATOR ARITMATIKA
print("OPERATOR ARITMATIKA")
x = 11
y = 5

print(x + y)    # PENJUMLAHAN
print(x - y)    # PENGURANGAN
print(x * y)    # PERKALIAN
print(x // y)   # PEMBAGIAN BILANGAN BULAT
print(x / y)    # PEMBAGIAN BILANGAN RIIL
print(x % y)    # MODULUS/SISA DARI PEMBAGIAN
print(x ** y)   # PANGKAT DARI KEDUA BILANGAN
"""
PENJELASAN: jadi untuk pembagian itu ada dua sintax, yang pertama adalah sintax untuk
pembagian bilangan bulat, misalnya integer penulisannya menggunakan slash sebanyak dua kali
(//). Kedua pembagian bilangan riil, misalnya float maka penulisan sintaxnya menggunakan
slash sebanyak satu kali. lihat contoh diatas dari halaman 16-17.
PENTING: Untuk pangkat, dia akan mengambil bilangan pertama untuk dipangkatkan dengan
bilangan kedua, contoh diatas, berarti 11 pangkat 5. 11 pangkat 5 itu artinya;
11x11x11x11x11
"""
print("")

# OPERATOR RELASIONAL
print("OPERATOR RELASIONAL")

# integer
print("====INTEGER====")
x = 5
y = 10
print(x == y)  # SAMA DENGAN
print(x != y)   # TIDAK SAMA DENGAN
print(x > y)    # LEBIH BESAR DARI
print(x < y)    # KURANG DARI
print(x >= y)   # LEBIH BESAR SAMA DENGAN
print(x <= y)   # KURANG DARI SAMA DENGAN

# string
print("\n====STRING====")
a = "a"
b = "a"
print(a == b)   # SAMA DENGAN
print(a != b)   # TIDAK SAMA DENGAN
print(a > b)    # LEBIH BESAR DARI
print(a < b)    # KURANG DARI
print(a >= b)   # LEBIH BESAR SAMA DENGAN
print(a <= b)   # KURANG DARI SAMA DENGAN

"""
PENJELASAN: untuk string yang dilihat adalah ascii code. jadi setiap karakter huruf itu
mempunyai angka decimalnya masing-masing dan itulah yang menjadi perbandingan. Perbandingan
dilihat dari huruf pertama, jika tidak sama maka dia akan langsung membandingkan, jika
dia sama dia akan menglihat urutan karakter selanjutnya kalau urutan selanjutnya beda
maka dia akan langsung dibandingkan

[PENJELASAN TAMBAHAN]: jadi untuk operator relasional ini, hasilnya adalah bertipe 
boolean true/false
"""

