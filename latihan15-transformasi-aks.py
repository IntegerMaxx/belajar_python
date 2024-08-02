"""
TRANSFORMASI ANGKA, KARAKTER, DAN STRING (AKS)
"""

# STRING LITERALS
print("STRING LITERALS")
print("")

# kata = 'jum'at' # ini akan invalid
kata = "jum'at" # ini yang benar
print(kata)
"""
PENJELASAN: jadi pada nilai kata diatas penulisan 'jum'at' akan dianggap invalid
oleh python. Penulisan kata "jum'at", tanda petik satu itu akan dianggap menjadi 
bagian nari nilai string. Misalnya kita tetap menginginkan petik satu sebagai
penulisan nilai string, python menyediakan Escape Character. Contohnya Escape 
Character (\) backslash penerapannya pada kodingan dibawah ini
"""
kata2 = 'jum\'at'
print(kata2)
"""
[ESCAPE CHARACTER]
\' Single quote
\" Double quote
\t Tab
\n Newline (line break)
\\ Backslash
Contoh lain penggunaan NewLine pada kodingan dibawah ini
"""
print("Hallo apa kabar dunia,\nsaya berharap semua jum\'at akan lebih baik,\nsemoga semua manusia bisa mencapai kebahagiaan.\n")
print("")

# RAW STRING
print("RAW STRING")
print(r"Hallo apa kabar dunia,\nsaya berharap semua jum\'at akan lebih baik,\nsemoga semua manusia bisa mencapai kebahagiaan.\n")
"""
PENJELASAN: lihat pada hasil print kodingan raw string di atas, semua escape character di print tanpa pandang bulu . Itu kerena penggunaan 
raw string untuk lebih meyakinkan lihat kodingan dibawah ini. Dengan penggunaan 
raw string dia akan mengabaikan fungsi dari escape character
"""
kata = "[H\'e\"l\tlo\n \\World]"
print("sebelum di raw string =", kata)
kata2 = r"H\'e\"l\tlo\n \\World"
print("setelah di raw string =",kata2)




