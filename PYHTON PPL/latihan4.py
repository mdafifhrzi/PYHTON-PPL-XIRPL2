# kelas induk = kendaraan , kelas turunan = mobil
# kendaraan mempunyai sifat berjalan(), mobil mempunyai sifat berjalan() tapi lebih spesifik

class kendaraan:
    def berjalan(self):
        print('Berjalan')

class mobil(kendaraan):
    def berjalan(self, kecepatan, satuan = 'km/j'):
        print(f'Berjalan Lebih Ngebut {kecepatan} {satuan}')


# instansiasi (memanggil fungsi dan kelas)
sepeda = kendaraan()
sedan = mobil()

sepeda.berjalan()
sedan.berjalan(200)