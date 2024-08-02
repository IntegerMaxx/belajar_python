"""
LIBRARY WEB SCRAPING
"""
from urllib.request import urlopen

# Pengambilan konten
url = "http://python.org/"
page = urlopen(url)
html = page.read().decode("utf-8")

# Mencari indeks awal dan akhir
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")

# Mengekstrak dan mencetak judul halaman
title = html[start_index:end_index]
print(title)
"""
PENJELASAN: pada kodingan diatas kita telah berhasil mengimport library "urlopen". yang 
dimana library ini berfungsi untuk mengakses website dan mengambil data yang ada di 
website tersebut data ini terdapat pada element html. Pada kodingan diatas kita mengakses
element "title" untuk bisa mengambil informasi yang ada pada element "title" tersebut.
Pada kodingan diatas kita mengakses "http://python.org/" yang memiliki title 
"Welcome to Python.org" akan keluar dari output program. Kita harus memasukkan "start_index",
sebagai tag awal, kemudian "end_index" sebagai tag akhir. "utf-8" itu adalah meta-chart
untuk file "html" yang dimana dia berfungsi sebagai pengenal kepada bahasa pemrograman
kalau di "html" ini ada karakter apa saja
"""






