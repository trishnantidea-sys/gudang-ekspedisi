import os
os.system("clear")

import datetime
from validation_registration import registrasi, login
from database import *
userid_terdaftar = [],
password_terdaftar = [],
email_terdaftar = [],
nama_terdaftar = [],
gender_terdaftar = [],
usia_terdaftar = [],
pekerjaan_terdaftar = [],
hobi_terdaftar = [],
kota_terdaftar = [],
rt_terdaftar = [],
rw_terdaftar = [],
zipcode_terdaftar = [],
lat_terdaftar = [],
long_terdaftar = [],
nohp_terdaftar = []
database_paket = []

print("Selamat datang di Aplikasi Gudang Ekspedisi (Dea & Lauzia)")
print("="*50)

# # login
# username = input("Masukkan email: ")
# password = input("Masukkan password: ")

# if username == "admin@mail.com" and password == "12345":
#     print("\n")
#     print("="*50)
#     print("Login berhasil")
# else:
#     print("Login gagal. Email atau password salah.")
#     exit()

### == Fungsi Paket ===
def pilih_kategori():
    print("\n===== Kategori Paket =====")
    print("1. Alat Olahraga")
    print("2. Kebutuhan Rumah Tangga")
    print("3. ATK (Alat Tulis Kantor)")
    print("4. Dokumen")
    print("5. Elektronik")
    print("6. Pakaian/Tekstil")
    print("7. Sparepart")

    kategori_valid = False
    while kategori_valid == False:
        pilihan_kategori = input("Pilih kategori (1-7): ")
        
        if pilihan_kategori == "1":
            return "Alat Olahraga"
        elif pilihan_kategori == "2":
            return "Kebutuhan Rumah Tangga"
        elif pilihan_kategori == "3":
            return "ATK (Alat Tulis Kantor)"
        elif pilihan_kategori == "4":
            return "Dokumen"
        elif pilihan_kategori == "5":
            return "Elektronik"
        elif pilihan_kategori == "6":
            return "Pakaian/Tekstil"
        elif pilihan_kategori == "7":
            return "Sparepart"
        else:
            print("Pilihan tidak valid. Silakan pilih 1-7.")

def hitung_tarif(berat, jenis_pengiriman):
    if jenis_pengiriman == "D&L Reguler":
        tarif_per_kg = 10000
    elif jenis_pengiriman == "D&L Eco (Ekonomis)":
        tarif_per_kg = 7000
    elif jenis_pengiriman == "D&L Super (Kilat)":
        tarif_per_kg = 15000
    elif jenis_pengiriman == "D&L Cargo":
        tarif_per_kg = 8000
    else:
        tarif_per_kg = 10000

    total_tarif = berat * tarif_per_kg
    return total_tarif

def pilih_jenis_pengiriman():
    print("\n===== Jenis Pengiriman =====")
    print("1. D&L Reguler (Estimasi 2-5 hari) - Rp 10.000/kg")
    print("2. D&L Eco/Ekonomis (Estimasi 3-7 hari) - Rp 7.000/kg")
    print("3. D&L Super/Kilat (Estimasi 1-2 hari) - Rp 15.000/kg")
    print("4. D&L Cargo - Rp 8.000/kg")
    
    jenis_valid = False
    while jenis_valid == False:
        pilihan = input("Pilih jenis pengiriman (1-4): ")
        
        if pilihan == "1":
            return "D&L Reguler", "2-5 hari"
        elif pilihan == "2":
            return "D&L Eco (Ekonomis)", "3-7 hari"
        elif pilihan == "3":
            return "D&L Super (Kilat)", "1-2 hari"
        elif pilihan == "4":
            return "D&L Cargo", "Sesuai jadwal"
        else:
            print("Pilihan tidak valid. Silakan pilih 1-4.")

def input_data_paket():
    while True:
        print("\n===== Input Data Paket =====")
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

        kategori = pilih_kategori()

        berat_valid = False
        while berat_valid == False:
            berat = input("Masukkan berat paket (kg): ")
            try:
                berat = float(berat)
                if berat <= 0:
                    print("Berat harus lebih dari 0 kg")
                else:
                    berat_valid = True
            except:
                print("Berat harus berupa angka")

        tgl_valid = False
        while tgl_valid == False:
            tgl_pengiriman = input("Masukkan tanggal pengiriman (DD-MM-YYYY): ")
            try:
                datetime.strptime(tgl_pengiriman, "%d-%m-%Y")
                tgl_valid = True
            except:
                print("Format tanggal salah. Gunakan format DD-MM-YYYY")

        jenis_pengiriman, estimasi = pilih_jenis_pengiriman()
        tarif = hitung_tarif(berat, jenis_pengiriman)

        print(f"\nTotal Tarif: Rp {tarif:,.0f}")
        print(f"Estimasi Tiba: {estimasi}")

        ## simpan data
        data_paket = {
            "resi": resi,
            "pengirim": pengirim,
            "no_hp_pengirim": no_hp_pengirim,
            "penerima": penerima,
            "no_hp_penerima": no_hp_penerima,
            "alamat_tujuan": alamat_tujuan,
            "kategori": kategori,
            "berat": berat,
            "tanggal_pengiriman": tgl_pengiriman,
            "jenis_pengiriman": jenis_pengiriman,
            "estimasi": estimasi,
            "tarif": tarif
        }

        database_paket.append(data_paket)
        print(f"\nData paket dengan resi {resi} berhasil diinput")

        lanjut = input("Tambahkan data lagi (y/n)? ")
        if lanjut.lower() != 'y':
            break

def lihat_data_paket():
    if not database_paket:
        print("Belum ada data paket yang diinput")
        return
    print("\n===== Pilihan Tampilan =====")
    print("1. Lihat Semua Paket")
    print("2. Lihat Berdasarkan Kategori")
    print("3. Lihat Berdasarkan Jenis Pengiriman")

    pilihan = input("Pilih tampilan (1-3): ")

    if pilihan == "1":
        # Tampilkan semua paket
        print("\n===== Semua Data Paket =====")
        for data in database_paket:
            tampilkan_detail_paket(data)
    
    elif pilihan == "2":
        # Tampilkan berdasarkan kategori
        print("\n===== Pilih Kategori =====")
        print("1. Alat Olahraga")
        print("2. Kebutuhan Rumah Tangga")
        print("3. ATK (Alat Tulis Kantor)")
        print("4. Dokumen")
        print("5. Elektronik")
        print("6. Pakaian/Tekstil")
        print("7. Sparepart")
        
        pilihan_kat = input("Pilih kategori (1-7): ")
        
        kategori_map = {
            "1": "Alat Olahraga",
            "2": "Kebutuhan Rumah Tangga",
            "3": "ATK (Alat Tulis Kantor)",
            "4": "Dokumen",
            "5": "Elektronik",
            "6": "Pakaian/Tekstil",
            "7": "Sparepart"
        }

        if pilihan_kat in kategori_map:
            kategori_pilihan = kategori_map[pilihan_kat]
            print(f"\n=== Paket Kategori: {kategori_pilihan} ===")
            ada_data == False
            for data in database_paket:
                if data["kategori"] == kategori_pilihan:
                    tampilkan_detail_paket(data)
                    ada_data = True
            if not ada_data:
                print(f"Tidak ada paket dengan kategori {kategori_pilihan}")
        else:
            print("Pilihan kategori tidak valid")

    elif pilihan == "3":
        print("\n===== Pilih Jenis Pengiriman =====")
        print("1. D&L Reguler")
        print("2. D&L Eco (Ekonomis)")
        print("3. D&L Super (Kilat)")
        print("4. D&L Cargo")
        
        pilihan_jenis = input("Pilih jenis pengiriman (1-4): ")
        
        jenis_map = {
            "1": "D&L Reguler",
            "2": "D&L Eco (Ekonomis)",
            "3": "D&L Super (Kilat)",
            "4": "D&L Cargo"
        }
        
        if pilihan_jenis in jenis_map:
            jenis_pilihan = jenis_map[pilihan_jenis]
            print(f"\n===== Paket Jenis Pengiriman: {jenis_pilihan} =====")
            ada_data = False
            for data in database_paket:
                if data["jenis_pengiriman"] == jenis_pilihan:
                    tampilkan_detail_paket(data)
                    ada_data = True
            
            if not ada_data:
                print(f"Tidak ada paket dengan jenis pengiriman {jenis_pilihan}")
        else:
            print("Pilihan jenis pengiriman tidak valid")
    
    else:
        print("Pilihan tidak valid")
        
    # if database_paket:
    #     for data in database_paket:
    #         print(f"Resi: {data['resi']}")
    #         print(f"Pengirim: {data['pengirim']}")
    #         print(f"No. HP Pengirim: {data['no_hp_pengirim']}")
    #         print(f"Penerima: {data['penerima']}")
    #         print(f"No. HP Penerima: {data['no_hp_penerima']}")
    #         print(f"Alamat Tujuan: {data['alamat_tujuan']}")
    #         print("="*50)
    # else:
    #     print

def tampilkan_detail_paket(data):
    print(f"\nResi: {data['resi']}")
    print(f"Pengirim: {data['pengirim']}")
    print(f"No. HP Pengirim: {data['no_hp_pengirim']}")
    print(f"Penerima: {data['penerima']}")
    print(f"No. HP Penerima: {data['no_hp_penerima']}")
    print(f"Alamat Tujuan: {data['alamat_tujuan']}")
    print(f"Kategori: {data['kategori']}")
    print(f"Berat: {data['berat']} kg")
    print(f"Tanggal Pengiriman: {data['tanggal_pengiriman']}")
    print(f"Jenis Pengiriman: {data['jenis_pengiriman']}")
    print(f"Estimasi Tiba: {data['estimasi']}")
    print(f"Tarif: Rp {data['tarif']:,.0f}")
    print("=" * 50)

def update_data_paket():
    print("\n=== Update Data Paket ===")
    resi = input("Masukkan nomor resi yang ingin diupdate: ")

    for data in database_paket:
        if data["resi"] == resi:
            print("\n--- Data Saat Ini ---")
            tampilkan_detail_paket(data)

            print("\n--- Masukkan Data Baru ---")
            pengirim = input("Masukkan nama pengirim: ")
            no_hp_pengirim = input("Masukkan no. HP pengirim: ")
            penerima = input("Masukkan nama penerima: ")
            no_hp_penerima = input("Masukkan no. HP penerima: ")
            alamat_tujuan = input("Masukkan alamat tujuan: ")

            ## update kategori
            kategori = pilih_kategori()

            ## update berat
            berat_valid = False
            while berat_valid == False:
                berat = input("Masukkan berat paket (kg): ")
                try:
                    berat = float(berat)
                    if berat <= 0:
                        print("Berat harus lebih dari 0 kg")
                    else:
                        berat_valid = True
                except:
                    print("Berat harus berupa angka")

            # Update tanggal
            tgl_valid = False
            while tgl_valid == False:
                tgl_pengiriman = input("Masukkan tanggal pengiriman (DD-MM-YYYY): ")
                try:
                    datetime.strptime(tgl_pengiriman, "%d-%m-%Y")
                    tgl_valid = True
                except:
                    print("Format tanggal salah. Gunakan format DD-MM-YYYY")
            
            # Update jenis pengiriman
            jenis_pengiriman, estimasi = pilih_jenis_pengiriman()
            
            # Hitung ulang tarif
            tarif = hitung_tarif(berat, jenis_pengiriman)
            print(f"\nTotal Tarif Baru: Rp {tarif:,.0f}")
            
            # update data
        
            data["pengirim"] = pengirim
            data["no_hp_pengirim"] = no_hp_pengirim
            data["penerima"] = penerima
            data["no_hp_penerima"] = no_hp_penerima
            data["alamat_tujuan"] = alamat_tujuan
            data["kategori"] = kategori
            data["berat"] = berat
            data["tanggal_pengiriman"] = tgl_pengiriman
            data["jenis_pengiriman"] = jenis_pengiriman
            data["estimasi"] = estimasi
            data["tarif"] = tarif

            print(f"\nData paket dengan resi {resi} berhasil diupdate")
            break
    else:
        print(f"Data paket dengan resi {resi} tidak ditemukan")

def hapus_data_paket():
    print("\n=== Hapus Data Paket ===")
    resi = input("Masukkan nomor resi yang ingin dihapus: ")

    for data in database_paket:
        if data["resi"] == resi:
            print("\n--- Data yang akan dihapus ---")
            tampilkan_detail_paket(data)

            konfirmasi = input("Yakin inin menghapus data ini? (y/n): ")
            if konfirmasi.lower() == "y":
                database_paket.remove(data)
                print(f"Data paket dengan resi {resi} berhasil dihapus")
            else:
                print("Penghapusan dibatalkan")
            break
    else:
        print(f"Data paket dengan resi {resi} tidak ditemukan")

def count_data_paket():
    return len(database_paket)


### === Menu Utama ===
def menu_utama():
    print("\n" + "=" * 50)
    print("Selamat Datang di Aplikasi Gudang Ekspedisi")
    print("(Dea & Lauzia)")
    print("=" * 50)
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    print("=" * 50)

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


## === Menu Admin Manajemen Paket ===
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
