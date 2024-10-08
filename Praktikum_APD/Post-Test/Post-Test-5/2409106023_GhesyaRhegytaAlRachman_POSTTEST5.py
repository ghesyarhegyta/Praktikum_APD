kucing = [["admin", "password", ["nyonyo", "amoi", "bumbu"]], ["user", "password", ["nyonyo", "amoi", "bumbu"]]]

while True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    pilih = input("Choose an option: ")
    
    if pilih == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        for user in kucing:
            if user[0] == username:
                print("Username sudah ada")
                break
        else:
            kucing.append([username, password, []])
            print("registrasi berhasil")
            
    elif pilih == "2":
        username = input("Enter username:")
        password = input("Enter password: ")
        for user in kucing:
            if user[0] == username and user[1] == password:
                while True:
                    print("1. Buat nama kucing")
                    print("2. Lihat nama-nama kucing")
                    print("3. Perbarui data nama kucing")
                    print("4. Hapus data nama kucing")
                    print("5. Logout")
                    pilih = input("Input pilihan user: ")
                    
                    if pilih == "1":
                        nama_kucing = input("Input nama kucing: ")
                        user[2].append(nama_kucing)
                        print("Nama kucing berhasil ditambahkan")
                    elif pilih == "2":
                        print("Nama kucing: ")
                        for nama_kucing in user[2]:
                            print(nama_kucing)
                    elif pilih == "3":
                        namalama = input("Input nama kucing lama: ")
                        namabaru = input("Input nama kucing baru: ")
                        if namalama in user[2]:
                            user[2][user[2].index(namalama)] = namabaru
                            print("Nama kucing berhasil diperbarui!")
                        else:
                            print("Nama kucing tidak terdatar")
                    elif pilih == "4":
                        nama_kucing = input("Input nama kucing: ")
                        if nama_kucing in user[2]:
                            user[2].remove(nama_kucing)
                            print("Nama kucing berhasil dihapus")
                        else:
                            print("Nama kucing tidak ditemukan")
                    elif pilih == "5":
                        break
                    else:
                        print("Pilihan anda tidak tersedia")
                break
        else:
            print("Username dan Password tidak sesuai")
            
    elif pilih == "3":
        break
    else:
        print("Pilihan tidak tersedia")