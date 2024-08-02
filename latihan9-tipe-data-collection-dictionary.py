"""
TIPE DATA COLLECTION DICTIONARY
"""
# PENGENALAN KEY-VALUE
"""
PENJELASAN, tipe data ini memilik key atau bisa kita anggap variabel, kemudian value atau nilai dari
sebuah variabel, sama seperti data collection yang lain. Untuk tanda petik key disini, kita bisa 
menggunakan petik satu atau petik dua dan jika anda ingin mengambil nilai / value, kita tidak 
menggunakan index untuk mengakses nilainya, melainkan dengan menggunakan key. Anda bisa melihat
pada contoh dibawah ini
"""
x ={'nama' : "Sunarto Utina", 'umur' : 20, "jalur" : True }
print(type(x))
# print(x[0]) >> hasilnya akan error
print(x['jalur'])


# MENAMBAH DATA PADA DICTIONARY
"""
PENJELASAN, saat kita menambahkan data pada DICTIONARY kita harus menuliskan nama variabelnya 
terlebih dahulu, nama variabelnya harus sama dengan yang kita inisialisasikan di awal, kemudian
nama value yang dibuat di dalam kurung siku dan menggunakan tanda petik satu, kemudian nilainya. 
nilai secara otomatis ditambahkan pada urutan terakhir, dan akan bertambah satu key dan nilai baru.
Untuk menghapus data pada dictionary mengetik kata "del" kemudian nama variabel "x" dan nama key
yang ingin dihapus. Mengubah data caranya mengetik nama variabel kemudian nama key yang ingin diubah
kemudian nilainya apa yang ingin dimasukkan/diubah
"""
x ['jenisPekerjaan'] = "Engginering"
print(x)

# MENGHAPUS DATA PADA DICTIONARY
del x["jalur"]
print(x)

# MENGUBAH DATA PADA DICTIONARY
x ['nama'] = 'Sunarti'
print(x)
