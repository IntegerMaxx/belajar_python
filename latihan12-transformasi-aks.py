"""
TRANSFORMASI ANGKA, KARAKTER, DAN STRING (AKS)
"""

# MEMISAH DAN MENGGABUNGKAN STRING
print("MEMISAH DAN MENGGABUNGKAN STRING")
print(".join()")
print("Sebelum di join")
print("Hallo-halo Gorontalo, apa kabar?")
print("")
print("Setelah di join")
print(" ".join(['Hallo-halo', 'Gorontalo', 'apa kabar?']))
"""
PENJELASAN: jadi .join() itu dia akan menambahkan kata yang di dalam itu menjadi sebuah
String yang utuh. tanda petik dua baris 15 sebelum .join diatas bermaksud untuk membuat
spasi antara kata, kalau kita ganti spasi tadi dengan nol 0 dia akan menjadi 
"Hallo-halo0Gorontalo0apa kabar" intinya di akhiran petik satu pada baris kode 15 akan 
ditambahkan 0. Jadi petik dua diatas bari 15 sebelum .join itu namanya delimeter, dia
akan ditambahkan setelah kata di dalam join terprint satu persatu
"""
print("")

print(".split()")
print("Sebelum di .split")
print("Hallo-halo Gorontalo, apa kabar?")
print("")
print("Setelah di split")
print("Hallo-halo Gorontalo, apa kabar?".split())
"""
PENJELASAN: jadi .split() itu dia akan memisah kata-kata yang ada di di dalam petik dua
kemudian dia akan menampilkannya dalam bentuk data collection list. .split() ini kebalikan
dari .join(). Setiap ada spasi itu akan dianggap sebagai delimeter atau batas setiap kata, 
spasi inilah yang akan memisahkan indexnya. Kita juga bisa menambahkan delimeter (\n) atau
newline untuk memisahkan setiap baris pada string multiline. Contohnya ada dibawah. pada 
contoh dibawah setiap dibuat baris baru dari string itu akan terpisah index listnya, itu
dikarenakan penggunaan delimeter (\n) jadi setiap baris baru akan dianggap sebagai index baru
"""
print("")
print("""ini adalah 
kata panjang yang multiline.
ini sebelum tersplit menggunakan newline""")
print("""ini adalah 
kata panjang yang multiline.
ini setelah tersplit menggunakan 
newline""".split("\n"))
print("")

# MENGGANTI ELEMENT STRING
print(".replace()")
kata = "Halo-halo Gorontalo, Hari ini cerah yaa??"
print("sebelum di replace")
print(kata)
print("setelah di replace")
print(kata.replace("cerah", "mendung"))
"""
PENJELASAN: .replace() sesuai namanya dia akan mengganti kata yang ada di dalam string. 
Penulisannya index ke-0 itu sebagai selector atau memilih kata yang ingin di ganti pada 
variabel kata, kemudian index ke-1 itu sebagai kata penggantinya. .replace() bersifat 
case sensitif.
"""
print("")







