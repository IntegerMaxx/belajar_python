"""
OPERASI PADA LIST, SET, DAN STRING
"""

# MEMBERIKAN NILAI UNTUK MULTIPLE VARIABLE
print("MEMBERIKAN NILAI UNTUK MULTIPLE VARIABLE")
data = ["apel","mangga","pisang"]
akuPengen1 = data[0]
akuPengen2 = data[1]
akuPengen3 = data[2]
print("aku pengen =",akuPengen1)
print("aku pengen =",akuPengen2)
print("aku pengen =",akuPengen3)
"""
PENJELASAN: untuk mengakses nilai index yang ada di dalam variabel dengan tipe data 
list. kita bisa mengaksesnya dengan cara seperti diatas. Jika ingin mengakses datanya
secara terurut bisa menggunakan cara diatas atau bisa menggunakan cara yang lebih
sederhana seperti yang ada di bawah ini. lihat variabelnya terurut sesuai index.
variabel yang menyimpan data harus sama banyaknya dengan index.
"""
dataTest = ["apel","mangga","pisang"]
akuIngin1,akuIngin2,akuIngin3 = dataTest;
print(dataTest)
print("aku ingin =",akuIngin1)
print("aku ingin =",akuIngin2)
print("aku ingin =",akuIngin3,"\n")

# SORT
print(".sort()")
listBuah = ["d.apel", "e.jeruk", "b.lemon", "a.mangga", "c.nanas"]
listAngka = [9,4,10,6,2,3,5,8,7,6,1]
print("list buah sebelum di sort =",listBuah)
print("list angka sebelum di sort =",listAngka)
listBuah.sort()
listAngka.sort()
print("list buah setelah di sort =",listBuah)
listBuah.sort(reverse=True)
print("list buah setelah di sort terbalik =",listBuah)
print("list angka setelah di sort =",listAngka)
listAngka.sort(reverse=True)
print("list angka setelah di sort terbalik =",listAngka)
"""
PENJELASAN: jadi fungsi tambahan .sort() untuk membuat nilai yang ada di dalam list 
integer terurut dari yang paling kecil sampai yang paling besar. Untuk list string 
dia akan mengurutkan nilai index yang memiliki awalan huruf sesuai abjad, dari 'a' 
sampai 'z'. .sort() tidak bisa digunakan untuk mengurutkan list yang memiliki tipe
data yang berbeda untuk membuktikannya kita bisa mencobanya pada list dibawah ini.
Saya membuat komentar agar program bisa terus berjalan
"""
# listBerbeda = [20,1,True,"Hello",7.2,'w','o','r','d']
# listBerbeda.sort()
# print(listBerbeda)

