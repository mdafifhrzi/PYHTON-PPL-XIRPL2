# ada 3 kategori enkapsulasi yaitu : public, protected, private

#contoh class public
class segitiga:
    def _init_(self, alas, tinggi):
        self.alas = alas 
        self.tinggi = tinggi
        self.luas = 0.5 * alas * tinggi

#buat instansiasinya
# segitiga_besar = segitiga(100,80)
# print(f'alas : {segitiga_besar.alas}')
# print(f'tinggi : {segitiga_besar.tinggi}')
# print(f'luas : {segitiga_besar.luas}')

#contoh class protected
class mobil:
    def _init_(self, merk):
        self._merk = merk

class mobilefwan(mobil):
    def _init_(self, merk, total_gear):
        super()._init_(merk)
        self._total_gear = total_gear

    #akses _merk dari subclass (kelas turunan)
    def pamer(self):
        print(f'Mobil {self._merk} dengan total gear {self._total_gear}')

# redbull = mobilefwan('Redbull Racing',8)
# redbull.pamer()

#class si paling sulid di akses (private)
class motor:
    def _init_(self,merk):
        self.__merk = merk

    def tampilkan_merk(self):
        print(f'Merk motornya: {self.__merk}')

# ducati = motor('Ducati')   
# ducati.tampilkan_merk()

# sedan = mobil('toyota')

# #tampilkan merk dari luar kelas
# print (f'Merk Mobil : {sedan._merk}')