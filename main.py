import os
os.system("clear")

import datetime
from validation_registration import registrasi, login
from database import *

# print("Selamat datang di Aplikasi Gudang Ekspedisi".center(50))
# print("D & L".center(50))
# print("="*50)

lebar = 52

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

def validasi_resi(resi):
    if len(resi) != 6:
        return False, "Resi harus terdiri dari 6 karakter (contoh: EXP001)"
    if not resi.startswith("EXP"):
        return False, "Resi harus dimulai dengan 'EXP' (huruf kapital)"
    
    angka_bagian = resi[3::]
    i = 0
    while i < len(angka_bagian):
        if not angka_bagian[i].isdigit():
            return False, "3 karakter setelah 'EXP' harus berupa angka (contoh: EXP001)"
        i += 1

    return True, "Resi Valid"

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
        
        resi_valid = False
        while resi_valid == False:
            resi = input("Masukkan nomor resi (format: EXP + 3 angka, contoh: EXP001): ").strip()

            format_ok, pesan = validasi_resi(resi)
            if not format_ok:
                print(f"Format resi tidak valid: {pesan}")
                continue

            duplicate = False
            for data in database_paket:
                if data["resi"] == resi:
                    print("Resi sudah terdaftar. Silakan masukkan resi yang berbeda.")
                    duplicate = True
                    break

            if duplicate == True:
                continue

            resi_valid = True

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
                datetime.datetime.strptime(tgl_pengiriman, "%d-%m-%Y")
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
        tampilkan_tabel_paket(database_paket, "SEMUA DATA PAKET")
    
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
            hasil_filter = []
    
            for data in database_paket:
                if data["kategori"] == kategori_pilihan:
                    hasil_filter.append(data)
            if hasil_filter:
                tampilkan_tabel_paket(hasil_filter, f"Paket Kategori: {kategori_pilihan.upper()}")
            else:
                print(f"\nTidak ada paket dengan kategori {kategori_pilihan}")
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
            hasil_filter = []

            for data in database_paket:
                if data["jenis_pengiriman"] == jenis_pilihan:
                    hasil_filter.append(data)
            if hasil_filter:
                tampilkan_tabel_paket(hasil_filter, f"Paket Jenis: {jenis_pilihan.upper()}")
            else:
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

def tampilkan_tabel_paket(list_data, judul="DATA PAKET"):
    if not list_data:
        print("Tidak ada data untuk ditampilkan")
        return
    
    ## untuk membuat lebar kolom (tetap)
    w_no    = 4
    w_resi  = 7
    w_krm   = 16
    w_trm   = 16
    w_kat   = 22
    w_brt   = 7
    w_jns   = 20
    w_tgl   = 12
    w_est   = 10
    w_tarif = 14

    def baris_pembatas(isi="-"):
        cols = ["|"]
        widths = [w_no, w_resi, w_krm, w_trm, w_kat, w_brt, w_jns, w_tgl, w_est, w_tarif]
        i = 0
        while i < len(widths):
            cols.append(isi * (widths[i] + 2))
            cols.append("|")
            i += 1
        print("".join(cols))

    def sel(teks, lebar, rata="kiri"):
        teks = str(teks)
        if len(teks) > lebar:
            teks = teks[:lebar - 1] + "~"
        if rata == "kanan":
            return f" {teks.rjust(lebar)} "
        elif rata == "tengah":
            return f" {teks.center(lebar)} "
        else:
            return f" {teks.ljust(lebar)} "
        
    lebar_total = (w_no + w_resi + w_krm + w_trm + w_kat + w_brt + w_jns + w_tgl + w_est + w_tarif) + (10 * 2) + 11

    print()
    print("|" + judul.center(lebar_total - 2) + "|")
    print("=" * lebar_total)

    header = ("|" + sel("No",      w_no,    "tengah") +
              "|" + sel("Resi",    w_resi,  "tengah") +
              "|" + sel("Pengirim",w_krm,   "tengah") +
              "|" + sel("Penerima",w_trm,   "tengah") +
              "|" + sel("Kategori",w_kat,   "tengah") +
              "|" + sel("Berat",   w_brt,   "tengah") +
              "|" + sel("Jenis Pengiriman", w_jns, "tengah") +
              "|" + sel("Tgl Kirim",w_tgl,  "tengah") +
              "|" + sel("Estimasi",w_est,   "tengah") +
              "|" + sel("Tarif (Rp)",w_tarif,"tengah") +
              "|")
    print(header)
    baris_pembatas("=")

    ## untuk baris data
    no = 1
    i = 0
    while i < len(list_data):
        data = list_data[i]
        baris = ("|" + sel(no,                         w_no,    "tengah") +
                 "|" + sel(data["resi"],                w_resi,  "tengah") +
                 "|" + sel(data["pengirim"],             w_krm,  "kiri")   +
                 "|" + sel(data["penerima"],             w_trm,  "kiri")   +
                 "|" + sel(data["kategori"],             w_kat,  "kiri")   +
                 "|" + sel(f"{data['berat']} kg",        w_brt,  "kanan")  +
                 "|" + sel(data["jenis_pengiriman"],     w_jns,  "kiri")   +
                 "|" + sel(data["tanggal_pengiriman"],   w_tgl,  "tengah") +
                 "|" + sel(data["estimasi"],             w_est,  "tengah") +
                 "|" + sel(f"{data['tarif']:,.0f}",      w_tarif,"kanan")  +
                 "|")
        print(baris)
        if i < len(list_data) - 1:
            baris_pembatas("-")
        no += 1
        i += 1

    baris_pembatas("=")
    print(f"  Total: {len(list_data)} paket\n")

def baris(label, nilai):
    label_lebar = 20
    nilai_lebar = lebar - label_lebar - 5
    label_str = str(label).ljust(label_lebar)
    nilai_str = str(nilai)
    if len(nilai_str) > nilai_lebar:
        print(f"| {label_str} | {nilai_str[:nilai_lebar]} |")
        sisa = nilai_str[nilai_lebar:]
        while sisa:
            print(f"| {''.ljust(label_lebar)} | {sisa[:nilai_lebar].ljust(nilai_lebar)} |")
            sisa = sisa[nilai_lebar:]
    else:
        print(f"| {label_str} | {nilai_str.ljust(nilai_lebar)} |")

def tampilkan_detail_paket(data):
    print()
    print("=" * lebar)
    print("|" + " DETAIL PAKET ".center(lebar - 2) + "|")
    print("=" * lebar)

    print("-" * lebar)
    baris("Nomor Resi",       data["resi"])
    print("-" * lebar)
    baris("[1] Pengirim",         data["pengirim"])
    baris("[2] No. HP Pengirim",  data["no_hp_pengirim"])
    print("-" * lebar)
    baris("[3] Penerima",         data["penerima"])
    baris("[4] No. HP Penerima",  data["no_hp_penerima"])
    baris("[5] Alamat Tujuan",    data["alamat_tujuan"])
    print("-" * lebar)
    baris("[6] Kategori",         data["kategori"])
    baris("[7] Berat",            f"{data['berat']} kg")
    baris("[8] Tgl Pengiriman",   data["tanggal_pengiriman"])
    baris("[9] Jenis Pengiriman", data["jenis_pengiriman"])
    baris("Estimasi Tiba",    data["estimasi"])
    baris("Tarif",            f"Rp {data['tarif']:,.0f}")
    print("=" * lebar)

def update_data_paket():
    print("\n=== Update Data Paket ===")

    resi_valid = False
    while resi_valid == False:
        resi = input("Masukkan nomor resi yang ingin diupdate: ").strip()
        format_ok, pesan = validasi_resi(resi)
        if not format_ok:
            print(f"Format resi tidak valid: {pesan}")
        else:
            resi_valid = True

    for data in database_paket:
        if data["resi"] == resi:
            pengirim = data['pengirim']
            no_hp_pengirim = data['no_hp_pengirim']
            penerima = data['penerima']
            no_hp_penerima = data['no_hp_penerima']
            alamat_tujuan = data['alamat_tujuan']
            kategori = data['kategori']
            berat = data['berat']
            tanggal_pengiriman = data['tanggal_pengiriman']
            jenis_pengiriman = data['jenis_pengiriman']
            estimasi = data['estimasi']
            tarif = data['tarif']

            input_done = False
            while input_done == False:
                print("\n--- Data Saat Ini ---")
                tampilkan_detail_paket(data)

                print("\n--- Pilih data yang ingin di ubah. ---")
                print("--- Jika ada lebih dari satu pilihan, pisahkan dengan tanda koma (,) ---")
                choice = input("Masukkan pilihan [1-10]: ")

                choice_str = choice.replace(" ","").split(",")
                choice_valid = True
                for cs in choice_str:
                    if int(cs) > 10 or int(cs) < 1:
                        choice_valid = False
                        os.system("clear")
                        print("Pilihan tidak tersedia. Coba lagi.")
                        break

                if choice_valid == False:
                    continue

                print("\n--- Masukkan Data Baru ---")
                for cs in choice_str:
                    if int(cs) == 1:
                        pengirim = input("Masukkan nama pengirim: ")
                    elif int(cs) == 2:
                        no_hp_pengirim = input("Masukkan no. HP pengirim: ")
                    elif int(cs) == 3:
                        penerima = input("Masukkan nama penerima: ")
                    elif int(cs) == 4:
                        no_hp_penerima = input("Masukkan no. HP penerima: ")
                    elif int(cs) == 5:
                        alamat_tujuan = input("Masukkan alamat tujuan: ")
                    elif int(cs) == 6:
                        ## update kategori
                        kategori = pilih_kategori()
                    elif int(cs) == 7:
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
                    elif int(cs) == 8:
                        # Update tanggal
                        tgl_valid = False
                        while tgl_valid == False:
                            tanggal_pengiriman = input("Masukkan tanggal pengiriman (DD-MM-YYYY): ")
                            try:
                                datetime.datetime.strptime(tgl_pengiriman, "%d-%m-%Y")
                                tgl_valid = True
                            except:
                                print("Format tanggal salah. Gunakan format DD-MM-YYYY")
                    elif int(cs) == 9:
                        # Update jenis pengiriman
                        jenis_pengiriman, estimasi = pilih_jenis_pengiriman()
                    
                        # Hitung ulang tarif
                        tarif = hitung_tarif(berat, jenis_pengiriman)
                        print(f"\nTotal Tarif Baru: Rp {tarif:,.0f}")

                input_done = True

            # update data
            data["pengirim"] = pengirim
            data["no_hp_pengirim"] = no_hp_pengirim
            data["penerima"] = penerima
            data["no_hp_penerima"] = no_hp_penerima
            data["alamat_tujuan"] = alamat_tujuan
            data["kategori"] = kategori
            data["berat"] = berat
            data["tanggal_pengiriman"] = tanggal_pengiriman
            data["jenis_pengiriman"] = jenis_pengiriman
            data["estimasi"] = estimasi
            data["tarif"] = tarif

            print(f"\nData paket dengan resi {resi} berhasil diupdate")
            print("Data telah diperbarui :")
            print("-" * lebar)
            baris("Nomor Resi",       data["resi"])
            print("-" * lebar)
            baris("[1] Pengirim",         data["pengirim"])
            baris("[2] No. HP Pengirim",  data["no_hp_pengirim"])
            print("-" * lebar)
            baris("[3] Penerima",         data["penerima"])
            baris("[4] No. HP Penerima",  data["no_hp_penerima"])
            baris("[5] Alamat Tujuan",    data["alamat_tujuan"])
            print("-" * lebar)
            baris("[6] Kategori",         data["kategori"])
            baris("[7] Berat",            f"{data['berat']} kg")
            baris("[8] Tgl Pengiriman",   data["tanggal_pengiriman"])
            baris("[9] Jenis Pengiriman", data["jenis_pengiriman"])
            baris("Estimasi Tiba",    data["estimasi"])
            baris("Tarif",            f"Rp {data['tarif']:,.0f}")
            print("=" * lebar)
            break
    else:
        print(f"Data paket dengan resi {resi} tidak ditemukan")

def hapus_data_paket():
    print("\n=== Hapus Data Paket ===")
    resi_valid = False
    while resi_valid == False:
        resi = input("Masukkan nomor resi yang ingin dihapus: ").strip()
        format_ok, pesan = validasi_resi(resi)
        if not format_ok:
            print(f"Format resi tidak valid: {pesan}")
        else:
            resi_valid = True

    for data in database_paket:
        if data["resi"] == resi:
            print("\n--- Data yang akan dihapus ---")
            tampilkan_detail_paket(data)

            konfirmasi = input("Yakin ingin menghapus data ini? (y/n): ")
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
    print("Selamat Datang di Aplikasi Gudang Ekspedisi".center(50))
    print("D & L".center(50))
    print("=" * 50)
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    print("=" * 50)


## === Menu Admin Manajemen Paket ===
def menu_paket():
    print("\n" + "=" * 50)
    while True:
        print("\n")
        print("="*50)
        print("MENU MANAJEMEN PAKET".center(50))
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
            print("\nTerima kasih telah menggunakan aplikasi Gudang Ekspedisi")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")


program_berjalan = True
while program_berjalan:
    menu_utama()
        
    opsi = input("Pilih Menu (1/2/3): ")
        
    if opsi == "1":
        registrasi()
        
    elif opsi == "2":
        idx_user = login()
        if idx_user is not None:
            menu_paket()  # Jika login berhasil, masuk ke menu paket
        
    elif opsi == "3":
        print("\n" + "Exit".center(50))
        print("Terima Kasih".center(50))
        program_berjalan = False
    else:
        print("Opsi tidak valid. Silakan pilih 1, 2, atau 3.")
