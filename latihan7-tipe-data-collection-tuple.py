"""
TIPE DATA COLLECTION TUPLE
"""

x = ("Manusia", True, 1.2, 192, False, 1+5j)
print(type(x))
"""
tuple ini seperti tipe data collection list, dia memiliki index
dan di dalamnya bisa memasukkan tipe data campur. kita juga bisa melakukan
apa yang bisa di lakukan di tipe data collection list sebelumnya, tapi tuple
IMMUTABLE yang artinya tidak dapat diubah
"""
print(x[0])
print(x[:3])
# x[0] = "Hello World"
# print(x)