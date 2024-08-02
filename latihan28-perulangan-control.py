"""
PERULANGAN
"""

print("PERULANGAN")
print("CONTROL PERULANGAN\n")


print("BREAK STATEMENT")
for i in range(6):      # Perulangan tingkat pertama
    print("Perulangan luar:", i)
    for j in range(10):     # Perulangan tingkat kedua
        print("Perulangan dalam:", j)
        if j == 1:
            break       # Menghentikan perulangan dalam (kedua) jika j = 1

"""
PENJELASAN: jadi perulangan luar tetap akan dieksekusi, artinya break ini hanya 
menghentikan perulangan dalam(perulangan tingkat kedua) jika perulangan dalam == 1 maka
perulangan dalam berhenti. Kemudian, lihat hasil outoputnya pada perulangan dalam angka
1 tetap ditampilkan, artinya selain nilai saat sampai pada nilai ke-1 dia akan dicetak
dan lakukan break. Contoh lainnya ada pada String pada baris kode dibawah ini 
"""
print("")

for huruf in "Hello world":
    if huruf == " ":
        break
    print("Huruf saat ini: {}".format(huruf))

"""
PENJELASAN: jadi baris kode print itu masih termasuk blok kode dari if, dia akan dieksekusi
saat operasi sekuensial sudah sampai pada if. Saat perulangan terjadi, kemudia di if 
bertemu dengan spasi(" ") maka break atau berhenti, jadi huruf selanjutnya tidak akan 
dicetak dan langsung keluar dari blok kode looping
"""

print("\nCONTINUE STATEMENT")
for huruf in "Hello world":
    if huruf == " ":
        continue
    print("Huruf saat ini: {}".format(huruf))
"""
PENJELASAN: perhatikan outputnya, spasi tidak tercetak. Artinya continue ini akan
melanjutkan looping namun dengan melewati spasi(" "). Saat "Hello" sudah dieksekusi dan
ditampilkan, selanjutnya saat masuk pada spasi(" "), maka ifnya akan bernilai true dan 
mengeksekusi continue sehingga spasi(" ") dilewati dan melanjutkan eksekusi selanjutnya
"world"  
"""

print("\nELSE SETELAH FOR")

numbers = [1,2,3,4,5]
for num in numbers:
    if num == 6:
        print("Angka ditemukan! Program berhenti!")
else:
    print("Angka tidak ditemukan.")

"""
PENJELASAN: jadi saat operasi sekuensial masuk pada looping, dia akan menyimpan numbers pada
variabel num, kemudian cek pada variabel num jika terdapat angka 6 lakukan print angka 
ditemukan, jika tidak lakukan print angka tidak ditemukkan. Pada perintah else, itu termasuk
bagian blok kode dari for bukan dari if, jadi setelah melakukan looping dia akan mencetak 
else dan menampilkan output. Namun saat kita mengganti nilai dari varibael num dengan angka
4 maka yang terprint adalah angka ditemukan, selanjutnya dia akan tetap mengeksekusi else
dan mengprint angka tidak ditemukkan, hal ini dapat diatasi dengan break
[PENJELASAN TAMBAHAN]
Perlu diperhatikan oleh Anda, if dan else pada contoh tersebut berkaitan walaupun berbeda 
blok. Pada else setelah for, statement else tidak akan dieksekusi saat if pernah sekali 
saja benar. Dengan kata lain, break dalam if harus tidak terjadi untuk memicu else setelah 
for. Intinya if dan else yang ada pada perulangan ini saling berkaitan. Else di for harus
melakukan pengecekekan terlebih dahulu pada if
"""






