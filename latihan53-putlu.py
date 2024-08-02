import unittest
"""
PENERAPAN UNIT TEST DENGAN LIBRARY UNITEST
"""

class TestStringMethods(unittest.TestCase):
    # Ini adalah test case pertama (1)
    def test_strip(self):
        self.assertEqual('www.dicoding.com'.strip('c.mow'), 'dicoding')

    # Test case kedua (2)
    def test_isalnum(self):
        self.assertTrue('c0d1ng'.isalnum())
        self.assertTrue('c0d!ng'.isalnum())

    # Test case ketiga (3)
    def test_index(self):
        s = 'dicoding'
        self.assertEqual(s.index('coding'), 2)
        # cek s.index gagal ketika tidak ditemukan
        with self.assertRaises(ValueError):
            s.index('decode')


if __name__ == '__main__':
    # Test Runner
    unittest.main()
"""
PENJELASAN: pada kode diatas kita telah berhasil menjalankan Unit Test menggunakan
library "unittest", pada library ini terdapat banyak objek dan fungsi tambahan untuk
melakukan pengetesan, contohnya pada kodingan diatas. Misalnya, pada baris kode ke-14
kita mengubah "assertFalse" menjadi "assertTrue" sehingga saat dilakukan pengetesan
terdapat kesalahan. Ketika kita menjalankan biasa tanpa penggunaan library unit test
program akan berjalan dengan normal.
"""







