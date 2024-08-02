"""
OPERASI PADA LIST, SET, DAN STRING
"""

print("len()")
contohListInt = [1,1,8,5,4,4,4,10,7,7]
contohString = "Hallo nama saya Grok"
contohSet = {1,1,8,5,4,4,4,10,7,7}
print("Contoh list integer =",contohListInt)
print("Contoh string =",contohString)
print("Contoh set =",contohSet)
print("Panjang list integer =",len(contohListInt))
print("Panjang string =",len(contohString))
print("Panjang set = ",len(contohSet))
"""
PENJELASAN: jadi len() ini bertujuan untuk menghitung panjang pada list,string, 
dan set. Khusus pada String dia akan menghitung setiap karakternya. Pada tipe data
set dia akan menghitung data yang tidak di duplikat, karna sifat dari set yaitu unik
yang berarti, setiap ada data yang double atau di duplikat dia akan tereliminasi 
secara otomatis dan hanya menyisakan satu data yang sebenarnya. Lihat pada 
hasil print dari set dan inisialisasi nilainya, pada hasil print menampilkan hanya
beberapa nilai dari data set yang ada pada inisialisasi awal dan datanya juga sudah
terurut
[PENJELASAN TAMBAHAN]
saat kita mengprint nilai dari set dia akan secara otomatis terurut, dari yang
dari yang paling kecil sampai yang paling besar
"""
print("")

# MIN DAN MAX
print("min() dan max()")
contohListInt = [20,28,90,60,32,18,3,100,49,55,76,84]
contohListString = ["hello","world", "aaya", "zasih","disini"]
contohString = "halloworld"
print("Contoh list integer =",contohListInt)
print("Contoh string =",contohString)
print("Contoh list string =",contohListString)
print("Angka terkecil list integer =",min(contohListInt))
print("Angka terbesar list integer =",max(contohListInt))
print("Nilai string terkecil =",min(contohString))
print("Nilai string terbesar =",max(contohString))
print("Nilai list string terkecil =",min(contohListString))
print("Nilai list string terbesar =",max(contohListString))
"""
PENJELASAN: jadi min() dan max() itu untuk melihat nilai terendah dan nilai tertinggi
dari sebuah perkumpulan data atau data collection. khusus untuk string dia akan 
melihat angka decimal yang ada pada ascii code. untuk tipe data list string, dia akan
melihat index yang diawalan kata index tersebut mempunyai huruf yang bernilai rendah
atau bernilai tinggi. Jika ada isi index yang awalan character stringnya bernilai 
tinggi atau rendah pada angka decimal ascii code maka itu yang akan ditampilkan.
"""
print("")

# COUNT
print(".count()")
ganjil = [1,1,3,3,3,3,5,5,7,7,7,9,9,9,9,9,9,9,9,]
contohListString = ["hallo","hallo", "saya", "masih","disini"]
contohString = "Hallo semuanya kenalin nama saya grok"
print("Contoh list integer =",ganjil)
print("Contoh list string =", contohListString)
print("Contoh string =",contohString)
print("jumlah list integer 9 =",ganjil.count(9))
print("Jumlah list string hallo =",contohListString.count('hallo'))
print("Jumlah string l =",contohString.count('l'))
"""
PENJELASAN: jadi .count() itu dia akan menghitung jumlah data yang ada pada list
dengan catatan kita harus mengisinya, contoh: .ganjil.count(9), dia akan mencari
angka 9 kemudian menghitungnya. () ini harus diisi kalau tidak program akan error.
untuk list String kita harus memasukkan panjang katanya untuk mengetahui berapa
banyak kata tersebut muncul di list. untuk string biasa atau literal yang akan 
mencari karakter yang ingin kita cari, kemudian menghitungnya.
"""
print("")

# IN DAN NOT IN
print("in dan not in")
listGanjil = [1,1,3,3,3,3,5,5,7,7,7,9,9,9,9,9,9,9,9,]
contohListString = ["hallo","hallo", "saya", "masih","disini"]
contohString = "Hallo semuanya kenalin nama saya grok"
print("Contoh list integer =",listGanjil)
print("Contoh list string =", contohListString)
print("Contoh string =",contohString)
print("Nilai 10 di list ganjil =",10 in listGanjil)
print("Nilai 'saya' di list string =",'saya' in contohListString)
print("Nilai 'grok' di string literals dengan not in =",'grok' not in contohString)
"""
PENJELASAN: jadi in itu dia akan mengecek nilainya, jika tidak ditemukan,
maka dia akan mengembalikan nilai False, jika ditemukkan dia akan mengembalikan
nilai True. not in itu dia akan mengecek nilai yang dicari ada pada list,
jika ada, maka dia akan menghasilkan nilai false, jika tidak ada, maka dia akan
menghasilkan nilai true. Intinya dia akan mengembalikan nilai dari boolean.
"""
print("")