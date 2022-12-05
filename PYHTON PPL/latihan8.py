# Buat Judul dan Input
def garis():
    print("--------------------------------")


print("--JDOORS (layanan hotel berjedorjedor)--")
print("-----Silahkan untuk pilih tipe kamar----")
print("------1--Reguler--Rp.150.000/Malam------")
print("------2--VIP------Rp.300.000/Malam------")
print("------3--VVIP-----Rp.600.000/Malam------")
print("------4--Kingdom--Rp.1.200.000/Malam----")
print("--PROMO! NGINEP SEMINGGU BONUS SEHARI---")

# Input dari customer
garis()     
tipe = int(input("Silahkan pilih tipe : "))
inap = int(input("Berapa malam menginap : "))
cust = input("Masukan Nama Anda : ")

# Kalkulasi tipe kamar
if tipe == 1:
    tipe_kamar = ("Reguler")
elif tipe == 2:
    tipe_kamar = ("VIP")
elif tipe == 3:
    tipe_kamar = ("VVIP")
elif tipe == 4:
    tipe_kamar = ("Kingdom")
else:
    tipe_kamar = ("Yang bener??")

#kalkulasi tipe regular
if tipe == 1:
    total_harga = inap*150000
#kalkulasi tipe VIP
elif tipe == 2:
    total_harga = inap*300000
#kalkulasi tipe VVIP
elif tipe == 3:
    total_harga = inap*600000
#kalkulasi tipe Kingdom
elif tipe == 4:
    total_harga = inap*1200000

# Outputnya
garis()
print("Terima Kasih ", cust, " Atas menggunakan layanan kami")
print("Tipe kamar yang anda pilih : ", tipe_kamar)
print("Total Harga : Rp", total_harga)

#Bonus Inap
if inap >= 7:
    print("SELAMAT ANDA MENDAPATKAN BONUS 1 HARI")
    print("Terima Kasih telah menginap di Hotel Jdoors!")
    total_inap = inap+1
elif inap < 7:
    print("Terima Kasih telah menginap di Hotel Jdoors!")
    total_inap = inap

print("Total Lama Menginap : ", total_inap, "Hari")