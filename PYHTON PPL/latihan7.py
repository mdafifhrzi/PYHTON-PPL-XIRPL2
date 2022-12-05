# beberapa yang biasa digunakan untuk ngoding

# magic method init (konstruktor) berfungsi untuk mendahulukan gilira satu sekali jalan codingannya atau looping 
class halodunia:
    def _init_(self):
        print('Halo dunia')

# membuat instansiasi
# a = halodunia()


# magic method str, menampilkan string saat ketika dijadikan parameter
class segitiga:
    def _init_(self, a, t):
        self.a = a
        self.t = t

    def _str_(self):
        luas = 0.5 * self.a * self.t return f'segitiga (alas = {self.a}) (tinggi = {self.t}) (luas = {luas})'

# membuat instansiasinya
# a = segitiga(10,10)
# print(a)

# magic method len, len berfungsi untuk menghitung panjang dari objek yang kita buat

# class siswa
class siswa:
    def _init_(self):
        self.__list_siswa = []
    def tambah_siswa(self, siswa):
        self.__list_siswa.append(siswa)
    def _len_(self):
        return len(self.__list_siswa)

# buat instansiasi
grup1 = siswa()
grup1.tambah_siswa('putra')
grup1.tambah_siswa('boim')  

print(len(grup1))
# ['putra', 'boim']