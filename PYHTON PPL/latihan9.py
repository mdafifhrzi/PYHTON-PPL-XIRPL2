# chest penyimpanan buku
buku = []

# fungsi untuk menampilkan menu
def show_menu():
    print("---MENU---")
    print("1. Show Buku")
    print("2. Insert Buku")
    print("3. Edit Buku")
    print("4. Delete Buku")
    print("5. Exit")

    menu = int(input("Pilih Menu : "))
    print("\n")
    if menu == 1:
        show_buku()
    elif menu == 2:
        insert_buku()
    elif menu == 3:
        edit_buku()
    elif menu == 4:
        delete_buku()
    elif menu == 5:
        exit()
    else:
        print("Ente salah pilih")

    
# fungsi untuk meng-insert buku
def insert_buku():
    buku_baru = input("Masukan Judul : ")
    buku.append(buku_baru)


# fungsi untuk menampilkan isi buku
def show_buku():
    if len(buku) <= 0:
        print("Belum Ada Data")
    else:
        for indeks in range(len(buku)):
            print("[{}] {}".format(indeks, buku[indeks]))


# fungsi untuk menghapus bukunya
def delete_buku():
    show_buku()
    indeks = int(input("inputkan ID Buku : "))
    if indeks > len(buku):
        print("ID Salah")
    else:
        buku.remove(buku[indeks])


if _name_ == "_main_":
    while True:
        show_menu()