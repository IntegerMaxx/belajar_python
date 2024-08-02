"""
TIPE DATA
"""

# NUMBERS
x = 6
print(type(x)) # >> INTEGER

x = 1.5
print(type(x)) # >> FLOAT

x = 1+2j
print(type(x)) # >> COMPLEX
print("")

# IMMUTABLE
var = 10
print(var)
print(id(var))
var = 11
print(var)
print(id(var))

"""
# IMMUTABLE
Penjelasan, nilainya berubah. dan lokasi memorinya juga ikut berubah, 
jadi yang sebenarnya terjadi adalah pembuatan objek baru. Tidak merubah data pada
variabel sebelumnya, hanya membuat objek baru dengan nilai baru (IMMUTABLE)
"""
print("")

# BOOLEAN (TRUE/FALSE)

x = True
print(type(x))

y = False
print(type(y))
print("")

# STRING (STR)

x = 'Hello World'
print(type(x))

# STRING (MULTI-LINE)

multi_line = """Halo semuanya. Ini adalah bahasa pemrograman
 python yang sangat keren, kamu bisa mengenter 
 stringnya tanpa perlu menambah nilai string (+).
 Skrang aku mengerti kenapa bahasa pemrograman ini 
 sangat keren. Tidak hanya itu outputnya juga akan 
 otomatis ter-enter sesuai yang kita tulis disini
 WOWWWWW AWSOME****"""

print(multi_line)

# STRING (INDEX)
j = "Halo Gorontalo"
print(j)
print(j[0])
"""
BERUSAHA MERUBAH STRING PADA INDEX KE 0
"""
# j[0] = 'G'
# print(j)

# STRING (MENGAKSES SUBSTRING)
s = "Halo Sunarto"
print(s[5:]) # 5 itu index yang ada pada string
print("")

"""
{ KESADARAN }
"""
s = "manusia1"
s = "hello world"
s = "manusia1"
print(s)
print("")

# STRING (FORMATED STRING)
#   1. Formatted String
name = "Sunarto Utina"
print(f"Hallo nama saya {name}")
#   2. %-Formatting
name = "Surjana Utina"
print("nama saya %s" % (name))
# 3. str-format()
name = "Sunarti Utina"
print("Halo semua, nama saya {}".format(name))
















