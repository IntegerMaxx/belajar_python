"""
TIPE DATA COLLECTION SET
"""
"""
tipe data ini tidak mempunyai index sehingga tidak bisa melakukan indexing. 
tipe data ini juga bersifat unik, jika ada nilai yang di duplikat, maka dia 
tidak akan di ambil, seperti 2 yang ada dibawah ini nilainya sudah lebih dari
1 yakni sebanyak 3 maka yang akan diambil hanya satu nilai 2 saja. kita bisa 
memanfaatkannya untuk menghilangkan duplikat pada suatu data. Kita dapat
menggunakan set untuk melakukan penggabungan (union) dan irisan (intersection)
"""
x = {1,2,6,3,8,11,9,2,2}
print(x)
print(type(x))
# UNION
set1 = {1,2,3,4,5}
set2 = {6,7,8,9,10}
unionTest = set1.union(set2)
print("union = ", unionTest)
# INTERSECTION
set3 = {1,2,3,4,5}
set4 = {3,4,5,6,7}
intersectionTest = set3.intersection(set4)
print("intersection = ",intersectionTest)

