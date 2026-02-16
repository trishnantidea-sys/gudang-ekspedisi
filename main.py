from validation_registration import registrasi, login

import os
os.system("clear")

print("Selamat datang di Aplikasi Gudang Ekspedisi (Dea & Lauzia)")
print("="*50)

database_paket = []

# login
username = input("Masukkan email: ")
password = input("Masukkan password: ")

if username == "admin@mail.com" and password == "12345":
    print("\n")
    print("="*50)
    print("Login berhasil")
else:
    print("Login gagal. Email atau password salah.")
    exit()

def input_data_paket():
    while True:
        print("Input Data Paket")
        resi = input("Masukkan nomor resi: ")

        duplicate = False
        for data in database_paket:
            if data["resi"] == resi:
                print("Resi sudah terdaftar. Silakan masukkan resi yang berbeda.")
                duplicate = True

        if duplicate == True:
            continue

        pengirim = input("Masukkan nama pengirim: ")
        no_hp_pengirim = input("Masukkan no. HP pengirim: ")
        penerima = input("Masukkan nama penerima: ")
        no_hp_penerima = input("Masukkan no. HP penerima: ")
        alamat_tujuan = input("Masukkan alamat tujuan: ")

        data_paket = {
            "resi": resi,
            "pengirim": pengirim,
            "no_hp_pengirim": no_hp_pengirim,
            "penerima": penerima,
            "no_hp_penerima": no_hp_penerima,
            "alamat_tujuan": alamat_tujuan
        }

        database_paket.append(data_paket)
        print(f"\nData paket dengan resi {resi} berhasil diinput")

        lanjut = input("Tambahkan data lagi (y/n)? ")
        if lanjut.lower() != 'y':
            break

def lihat_data_paket():
    if database_paket:
        for data in database_paket:
            print(f"Resi: {data['resi']}")
            print(f"Pengirim: {data['pengirim']}")
            print(f"No. HP Pengirim: {data['no_hp_pengirim']}")
            print(f"Penerima: {data['penerima']}")
            print(f"No. HP Penerima: {data['no_hp_penerima']}")
            print(f"Alamat Tujuan: {data['alamat_tujuan']}")
            print("="*50)
    else:
        print("Belum ada data paket yang diinput")

def update_data_paket():
    print("Update Data Paket")
    resi = input("Masukkan nomor resi yang ingin diupdate: ")

    for data in database_paket:
        if data["resi"] == resi:
            print(f"Resi: {data['resi']}")
            print(f"Pengirim: {data['pengirim']}")
            print(f"No. HP Pengirim: {data['no_hp_pengirim']}")
            print(f"Penerima: {data['penerima']}")
            print(f"No. HP Penerima: {data['no_hp_penerima']}")
            print(f"Alamat Tujuan: {data['alamat_tujuan']}")

            pengirim = input("Masukkan nama pengirim: ")
            no_hp_pengirim = input("Masukkan no. HP pengirim: ")
            penerima = input("Masukkan nama penerima: ")
            no_hp_penerima = input("Masukkan no. HP penerima: ")
            alamat_tujuan = input("Masukkan alamat tujuan: ")

            data["pengirim"] = pengirim
            data["no_hp_pengirim"] = no_hp_pengirim
            data["penerima"] = penerima
            data["no_hp_penerima"] = no_hp_penerima
            data["alamat_tujuan"] = alamat_tujuan

            print(f"Data paket dengan resi {resi} berhasil diupdate")
            break
    else:
        print(f"Data paket dengan resi {resi} tidak ditemukan")

def hapus_data_paket():
    print("Hapus Data Paket")
    resi = input("Masukkan nomor resi yang ingin dihapus: ")

    for data in database_paket:
        if data["resi"] == resi:
            database_paket.remove(data)
            print(f"Data paket dengan resi {resi} berhasil dihapus")
            break
    else:
        print(f"Data paket dengan resi {resi} tidak ditemukan")

def count_data_paket():
    return len(database_paket)


### === Menu Utama
def menu_utama():
    print("\n" + "=" * 50)
    print("Selamat Datang di Aplikasi Gudang Ekspedisi")
    print("(Dea & Lauzia)")
    print("=" * 50)
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    print("=" * 50)

def menu_paket():
    print("\n" + "=" * 50)
    while True:
        print("\n")
        print("="*50)
        print("=== MENU MANAJEMEN PAKET ===")
        print("="*50)
        print("1. Input Data Paket")
        print(f"2. Lihat Data Paket ({count_data_paket()} data)")
        print("3. Update Data Paket")
        print("4. Hapus Data Paket")
        print("5. Keluar")
        print("="*50)

        pilihan = input("Masukkan pilihan: ")

        if pilihan == "1":
            input_data_paket()
        elif pilihan == "2":
            lihat_data_paket()
        elif pilihan == "3":
            update_data_paket()
        elif pilihan == "4":
            hapus_data_paket()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan aplikasi Gudang Ekspedisi")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")

## === Program Utama ===
program_berjalan = True

while program_berjalan:
    menu_utama()
    
    opsi = input("Pilih Menu (1/2/3): ")
    
    if opsi == "1":
        registrasi()
    
    elif opsi == "2":
        idx_user = login()
        if idx_user is not None:
            # Jika login berhasil, masuk ke menu paket
            menu_paket()
    
    elif opsi == "3":
        print("\n----- Exit -----".center(50))
        print("Terima Kasih telah menggunakan Aplikasi Ekspedisi Gudang (Dea & Lauzia)".center(50))
        program_berjalan = False
    
    else:
        print("Opsi tidak valid. Silakan pilih 1, 2, atau 3.")