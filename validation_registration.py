from database import *
import pwinput

# ASSIGNMENT 1 ==== VALIDATION EMAIL ====

def validasi_email(Email):
    if Email.count("@") != 1:
        return "Format Email salah (harus memiliki '@')"
    
    bagian = Email.split("@")
    User = bagian[0]
    sisa = bagian[1]
    
    if User == "":
        return "Format Username tidak boleh kosong"
    
    if not User[0].isalnum():
        return "Format Username harus diawali huruf atau angka)"
    
    i = 0
    while i < len(User):
        char = User[i]
        if not (char.isalnum() or char == '_' or char == '.'):
            return "Format Username mengandung karakter tidak valid"
        i += 1
    
    if sisa.count(".") < 1:
        return "Format Email harus memiliki ekstensi"
    
    if sisa.count(".") > 2:
        return "Format Ekstensi maksimal 2 dot"
    
    parts = sisa.split(".")
    Hosting = parts[0]
    Ekstensi = parts[1:]
    
    if Hosting == "":
        return "Format Hosting tidak boleh kosong"
    
    i = 0
    while i < len(Hosting):
        if not Hosting[i].isalnum():
            return "Format Hosting hanya boleh huruf dan angka"
        i += 1
    
    idx = 0
    while idx < len(Ekstensi):
        ext = Ekstensi[idx]
        
        if ext == "":
            return "Format Ekstensi belum dimasukkan"
        
        if not ext.isalpha():
            return "Format Ekstensi hanya boleh huruf"
        
        if len(ext) > 5:
            return "Format Ekstensi maksimal 5 karakter"
        
        idx += 1
    
    return "Alamat Email yg anda Masukkan Valid"
    

# ASSIGNMENT 2 ==== ACCOUNT REGISTRATION ====
# REGISTER Validasi UserID & Password 
def registrasi():
    print("\n" + "=" * 50)
    print("REGISTER ACCOUNT".center(50))
    print("=" *50)
    print("Masukkan Data:".center(50))

    # Validasi UserID
    status_userid = "belum valid"
    while status_userid == "belum valid":
        userid = input("Masukkan User ID: ")

        jumlah_huruf = 0
        jumlah_angka = 0
        i = 0
        while i < len(userid):
            if userid[i].isalpha():
                jumlah_huruf += 1
            if userid[i].isdigit():
                jumlah_angka += 1
            i += 1
        if jumlah_huruf > 0 and jumlah_angka > 0:
            if userid.isalnum():
                if len(userid) >= 6 and len(userid) <= 20:
                    if userid in userid_terdaftar:
                        print("User ID sudah terdaftar. Masukkan User ID yg berbeda.")
                    else:
                        status_userid = "sudah valid"
                else:
                    print("User ID harus terdiri dari 6-20 karakter")
            else:
                print("User ID tidak boleh mengandung karakter lain")
        else:
            print("User ID harus kombinasi huruf dan angka")

        
    # Validasi Password           
    status_password = False
    while status_password == False:
        # password = input("Password: ")
        password = pwinput.pwinput(prompt='Password: ', mask='*')

        if len(password) < 8:
            print("Password minimal 8 karakter")
        else:
            jumlah_huruf_besar = 0
            jumlah_huruf_kecil = 0
            jumlah_angka = 0
            jumlah_karakter_khusus = 0
            char_khusus = "/.,@#$%"
            
            i = 0
            while i < len(password):
                char = password[i]
                    
                if char.isupper():
                    jumlah_huruf_besar += 1
                elif char.islower():
                    jumlah_huruf_kecil += 1
                elif char.isdigit():
                    jumlah_angka += 1
                elif char in char_khusus:
                    jumlah_karakter_khusus += 1
                i += 1
                    
            if jumlah_huruf_besar > 0 and jumlah_huruf_kecil > 0 and jumlah_angka > 0 and jumlah_karakter_khusus > 0:
                status_password = True
            else:
                print("Password harus kombinasi huruf besar, huruf kecil, angka, dan karakter khusus (/.,@#$%)")
    
    # ----- Validasi Email ----- (yg di Assignment 1 di paling atas)
    status_email = False
    while status_email == False:
        Email = input("Email: ")

        hasil = validasi_email(Email)
        print(hasil)
                
        if hasil == "Alamat Email yg anda Masukkan Valid":
            status_email = True
    
## ----- Profile Registration ----

    nama_valid = False
    while nama_valid == False:
        Nama = input("Masukkan nama Lengkap: ").title()

        if Nama.replace(" ", "").isalpha():
            nama_valid = True
        else:
            print("Nama hanya boleh mengandung huruf")
        
    gender_valid = False
    while gender_valid == False:
        Gender = input("Jenis Kelamin (Male/Female): ").capitalize()

        if Gender == "Male" or Gender == "Female":
            gender_valid = True
        else:
            print("Jenis Kelamin tidak valid. Harap masukkan 'Male' atau 'Female'")

    usia_valid = False
    while usia_valid == False:
        Usia = input("Masukkan usia Anda: ")

        if Usia.isdigit():
            Usia = int(Usia)
            if Usia < 17 or Usia > 80:
                print("Usia harus antara 17-80 tahun")
            else:
                usia_valid = True
        else:
            print("Usia harus berupa angka")

    pekerjaan_valid = False
    while pekerjaan_valid == False:
        Pekerjaan = input("Pekerjaan: ").title()

        if Pekerjaan.replace(" ", "").isalpha():
            pekerjaan_valid = True
        else:
            print("Pekerjaan hanya boleh mengandung huruf")

        
    hobi_valid = False
    while hobi_valid == False:
        Hobi = input("Hobi (pisahkan dengan koma jika lebih dari 1): ").title()

        Hobi = Hobi.replace(" ", "")
        list_hobi = Hobi.split(",")

        list_hobi_akhir = []
        i = 0
        while i < len(list_hobi):
            hobi_item = list_hobi[i].strip()
            if hobi_item != "":
                list_hobi_akhir.append(hobi_item)
            i += 1

        if len(list_hobi_akhir) < 3:
            print("Isi hobi minimal 3")
        else:
            jumlah_hobi_alfabet = 0
            i = 0
            while i < len(list_hobi_akhir):
                if list_hobi_akhir[i].isalpha():
                    jumlah_hobi_alfabet += 1
                i += 1

            if jumlah_hobi_alfabet == len(list_hobi_akhir):
                list_hobi = list_hobi_akhir
                hobi_valid = True
            else:
                print("Hobi berisi huruf saja.")


    print("\nAlamat: ")
    kota_valid = False
    while kota_valid == False:
        NamaKota = input("Nama Kota: ")

        if NamaKota.replace(" ", "").isalpha():
            kota_valid = True
        else:
            print("Nama Kota hanya boleh huruf saja")

    rt_valid = False
    while rt_valid == False:
        RT = input("RT: ")

        if RT.isdigit():
            RT = int(RT)
            rt_valid = True
        else:
            print("RT harus berupa angka")

    rw_valid = False
    while rw_valid == False:
        RW = input("RW: ")

        if RW.isdigit():
            RW = int(RW)
            rw_valid = True
        else:
            print("RW harus berupa angka")
        
    zipcode_valid = False
    while zipcode_valid == False:
        ZipCode = input("Zip Code: ")

        if len(ZipCode) != 5 or not ZipCode.isdigit():
            print("Zip Code harus 5 digit angka")
        else:
            ZipCode = int(ZipCode)
            zipcode_valid = True

    print("\nGeo: ")
    lat_valid = False
    while lat_valid == False:
        Lat = input("Latitude (contoh: -6.9175): ")

    
        try:
            Lat = float(Lat)
            lat_valid = True
        except:
            print("Latitude berupa angka desimal")
        
    longitude_valid = False
    while longitude_valid == False:
        Longitude = input("Longitude (contoh: 106.8456): ")

        try:
            Longitude = float(Longitude)
            longitude_valid = True
        except:
            print("Longitude berupa angka desimal")
        
        
    nohp_valid = False
    while nohp_valid == False:
        NoHp = input("No Hp: ")
            
        if len(NoHp) < 11 or len(NoHp) > 13 or not NoHp.isdigit():
            print("No Hp harus 11-13 digit angka")
        else:
            NoHp = int(NoHp)
            nohp_valid = True


    ### ----- Simpan Data -----
    status_simpan = False
    while status_simpan == False:
        SimpanData = input("\nSimpan Data? Y/N: ").upper()

        if SimpanData == "Y":
            userid_terdaftar.append(userid)
            password_terdaftar.append(password)
            email_terdaftar.append(Email)
            nama_terdaftar.append(Nama)
            gender_terdaftar.append(Gender)
            usia_terdaftar.append(Usia)
            pekerjaan_terdaftar.append(Pekerjaan)
            hobi_terdaftar.append(list_hobi)
            kota_terdaftar.append(NamaKota)
            rt_terdaftar.append(RT)
            rw_terdaftar.append(RW)
            zipcode_terdaftar.append(ZipCode)
            lat_terdaftar.append(Lat)
            long_terdaftar.append(Longitude)
            nohp_terdaftar.append(NoHp)
  
            print("Data berhasil disimpan")
            status_simpan = True

        elif SimpanData == "N":
            print("Data tidak disimpan")
            status_simpan = True
        else:
            print("Tidak valid. Silakan masukkan 'Y' atau 'N'")

# ===== LOGIN =====
def login():
    print("\n" + "=" * 50)
    print("LOGIN".center(50))
    print("=" *50)

    
    login_berhasil = False
    coba = 0
    batas_coba = 5
    idx_user = -1

    while not login_berhasil and coba < batas_coba:
        userid_login = input("Masukkan ID: ")
        # password_login = input("Masukkan Password: ")
        password_login = pwinput.pwinput(prompt='Masukkan Password: ', mask='*')

        if userid_login not in userid_terdaftar:
            coba += 1
            print("ID Tidak Terdaftar. Silakan registrasi.")
            print(f"Percobaan ke- {coba} dari {batas_coba}")
        else:
            # Ambil index user
            idx_user = userid_terdaftar.index(userid_login)

            if password_terdaftar[idx_user] == password_login:
                print("Login berhasil.")
                login_berhasil = True
 
                print("\n===== Data Anda =====")
                print("Nama:", nama_terdaftar[idx_user])
                print("Email:", email_terdaftar[idx_user])
                print("Gender:", gender_terdaftar[idx_user])
                print("Usia:", usia_terdaftar[idx_user])
                print("Pekerjaan:", pekerjaan_terdaftar[idx_user])
                print("Hobi:", ", ".join(hobi_terdaftar[idx_user]))
                print("Alamat:")
                print("  Nama Kota:", kota_terdaftar[idx_user])
                print("  RT:", rt_terdaftar[idx_user])
                print("  RW:", rw_terdaftar[idx_user])
                print("  Zip Code:", zipcode_terdaftar[idx_user])
                print("Geo:")
                print("  Lat:", lat_terdaftar[idx_user])
                print("  Longitude:", long_terdaftar[idx_user])
                print("No Hp:", nohp_terdaftar[idx_user])
            
            else:
                coba += 1
                print("Password yg dimasukkan Salah")
                print(f"Percobaan ke- {coba} dari {batas_coba}")
                print()

    if not login_berhasil:
        print("\n" + "=" * 50)
        print("Gagal Login sebanyak 5 kali. Silakan coba beberapa saat lagi.".center(50))
        print("Kembali ke Menu Utama".center(50))
        print("=" * 50)
        return None
    
    return idx_user
            

 
