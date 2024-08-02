print("===LATIHAN ARRAY===")
array = [20,10,50,30,40]
print(array)

print("\n====MENGAKSES NILAI ARRAY====")
for i in range(len(array)):
    index_saat_ini = array[i]
    index_selanjutnya = i+1

    if index_selanjutnya < len(array):
        elemen_selanjutnya = array[index_selanjutnya]
    else:
        elemen_selanjutnya = None
    print(f"elemen array saat ini {index_saat_ini}, elemen array berikutnya {elemen_selanjutnya}")


print("\n====MENGURUTKAN NILAI ARRAY====")



def kecil_ke_besar(array2):
    for i in range(len(array2)):
        for j in range(len(array2) - 1):
            if array2[j] > array2[j + 1]:
                buffer = array2[j]
                array2[j] = array2[j + 1]
                array2[j + 1] = buffer
    return array2

def besar_ke_kecil(array2):
    for i in range(len(array2)):
        for j in range(len(array2) - 1):
            if array2[j] < array2[j + 1]:
                buffer = array2[j]
                array2[j] = array2[j + 1]
                array2[j + 1] = buffer
    return array2

def mencari_nilai_terbesar(array3):
    pointer_kiri = array3[0]
    for i in range(len(array3) - 1):
        pointer_kanan = array3[i + 1]
        if pointer_kanan > pointer_kiri:
            pointer_kiri = pointer_kanan
    print(pointer_kiri)

array3 = [20,10,50,30,40]

print("==KECIL KE BESAR==")
hasil_urutan = kecil_ke_besar(array3)
print(hasil_urutan)

print(("==BESAR KE KECIL=="))
hasil_urutan = besar_ke_kecil(array3)
print(hasil_urutan)

print(mencari_nilai_terbesar(array3))
























