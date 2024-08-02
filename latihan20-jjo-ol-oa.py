"""
JENIS-JENIS OPERATOR
operator aritmatika,operator relasional,
operator logika, operator asiggnment
"""

# OPERATOR LOGIKA
print("OPERATOR LOGIKA")
a = True
b = False
print(a & b)    # LOGIKA AND (&)
print(a | b)    # LOGIKA OR (|)
print(not b)    # LOGIKA NOT
print("")
print("===AND===")
print("True and True =",True & True)
print("True and False =",True & False)
print("False and True =",False & True)
print("False and False =",False & False)
print("")

print("===OR===")
print("True or True =",True | True)
print("True or False =",True | False)
print("False or True =",False | True)
print("False or False =",False | False)
print("")

print("===NOT===")
print("not True =",not True)
print("not False =",not False)
print("")

# OPERATOR ASIGGNMENT
print("OPERATOR ASIGGNMENT")
# +=
print("====(+=)====")
x = 11
x += 5 # SAMA AJA DENGAN X = X + 5
print(x)

# -=
print("====(-=)====")
x = 11
x -= 5 # SAMA AJA DENGAN X = X - 5
print(x)

# *=
print("====(*=)====")
x = 11
x *= 5 # SAMA AJA DENGAN X = X * 5
print(x)

# /=
print("====(/=)====")
x = 11
x /= 5 # SAMA AJA DENGAN X = X / 5
print(x) # OTOMATIS MENJADI FLOAT

# %=
print("====(%=)====")
x = 11
x %= 5 # SAMA AJA DENGAN X = X % 5
print(x) # SISA BAGI DARI 11 BAHAGI 5

dico = 750000
membandingkan = dico > 500000
diskonBelanja = (dico * 10) // 100
dico -= diskonBelanja
print("total harga yang harus dibayar dico adalah =",dico)

x = 1960
y = 901
print(x % y)



















