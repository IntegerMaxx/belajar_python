import pandas as pd
"""
LIBRARY PENGOLAHAN DATA
"""
print("LIBRARY PENGOLAHAN DATA")

print("pandas Version =",pd.__version__)
data = {
    'nama' : ['John','Jane','Bob','Alice'],
    'usia' : [25,30,22,28],
    'pekerjaan' : ['Engineer','Teacher','Designer','Doctor']
}
df = pd.DataFrame(data)
print(df)
"""
PENJELASAN: pada kodingan diatas kita telah berhasil mengimport dan menggunakan library dari
"pandas" yang kita singkat menjadi "as". Kemudian kita membuat sebuah data dictionary yang 
dimana mempunyai key dan value, pada kodingan diatas kita mempunyai key 'nama','usia', dan
'pekerjaan'. Kita juga mempunyai value, valuenya setelah key. Kemudian kita memanggil
library 'pandas' yang sudah kita singkat tadi, kita memanggilnya pada baris kode ke-13
'pd.DataFrame(data)'. 'pd' itu nama librarynya, 'DataFrame()' itu nama fungsinya, '(data)'
itu sebagai parameter dari fungsi 'DataFrame()'.
"""

"""
"Mathematical Plotting Library". >> matplotlib
"""

import matplotlib.pyplot as plt
import seaborn as sns
# print("matplotlib Version =",plt.__version__)

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Membuat plot garis
plt.plot(x, y)

# Menambahkan judul dan label sumbu
plt.title("Contoh Plot Garis")
plt.xlabel("Sumbu X")
plt.ylabel("Sumbu Y")

# Menampilkan plot
plt.show()

# Contoh data
tips = sns.load_dataset('tips')  # Memuat dataset tips dari Seaborn

# Contoh plot histogram
sns.histplot(tips['total_bill'], kde=True)
plt.title('Histogram Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.show()





































