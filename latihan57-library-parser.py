"""
LIBRARY PARSER
"""
import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument('-o', '--output', action='store_true', help="tampilkan output")
# args = parser.parse_args()
#
# if args.output:
#     print("Halo ini adalah sebuah output dari latihan57-libray-parser.py")



"""
PENJELASAN: jadi pada kodingan diatas kita telah berhasil mengimport library "argparse"
yang kegunaan sebagai untuk menglihat hasil outputnya di terminal. Baris program yang
akan dipanggil hanya baris yang menerima parameter args, misalnya pada kodingan diatas
ada statement "if args.output:", "args.output" inilah yang menjadi parameter untuk 
menglihat hasil yang ada di dalam dari sebuah terminal. "args.output" itu harus sesuai
dengan "parser.add_argument()" yakni "--output" sebagai parameter pemanggilannya
"""

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nama', required=True, help="Masukkan Nama Anda")
parser.add_argument('-u', '--umur', required=True, help="Masukkan umur anda")
args = parser.parse_args()

print("Terima kasih telah menggunakan latihan57-library-parser.py, hallo " + args.nama + "\numur kamu = " + args.umur )
"""
PENJELASAN: pada kodingan diatas kita telah meanmbahkan beberapa input pada terminal, nama dan umur.

"""











