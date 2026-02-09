# ASSIGNMENT 1 ==== VALIDATION EMAIL ====

def validasi_email(Email):
    # Cek jumlah @
    if Email.count("@") != 1:
        return "Format Email salah (harus memiliki '@')"
    
    # Split dengan @
    bagian = Email.split("@")
    User = bagian[0]
    sisa = bagian[1]
    
    # Validasi User tidak kosong
    if User == "":
        return "Format Username tidak boleh kosong"
    
    # User harus diawali huruf atau angka
    if not User[0].isalnum():
        return "Format Username harus diawali huruf atau angka)"
    
    # User hanya boleh huruf, angka, underscore, dan dot
    i = 0
    while i < len(User):
        char = User[i]
        if not (char.isalnum() or char == '_' or char == '.'):
            return "Format Username mengandung karakter tidak valid"
        i += 1
    
    # Cek apakah ada ekstensi (minimal 1 dot)
    if sisa.count(".") < 1:
        return "Format Email harus memiliki ekstensi"
    
    # Cek maksimal 2 dot untuk ekstensi
    if sisa.count(".") > 2:
        return "Format Ekstensi maksimal 2 dot"
    
    # Split hosting dan ekstensi
    parts = sisa.split(".")
    Hosting = parts[0]
    Ekstensi = parts[1:]
    
    # Validasi Hosting tidak boleh kosong
    if Hosting == "":
        return "Format Hosting tidak boleh kosong"
    
    # Hosting hanya boleh huruf dan angka
    i = 0
    while i < len(Hosting):
        if not Hosting[i].isalnum():
            return "Format Hosting hanya boleh huruf dan angka"
        i += 1
    
    # Validasi setiap ekstensi
    idx = 0
    while idx < len(Ekstensi):
        ext = Ekstensi[idx]
        
        if ext == "":
            return "Format Ekstensi belum dimasukkan"
        
        # Ekstensi hanya boleh huruf
        if not ext.isalpha():
            return "Format Ekstensi hanya boleh huruf"
        
        # Ekstensi maksimal 5 karakter
        if len(ext) > 5:
            return "Format Ekstensi maksimal 5 karakter"
        
        idx += 1
    
    return "Alamat Email yg anda Masukkan Valid"
    



# ASSIGNMENT 2 ==== ACCOUNT REGISTRATION ====

userid_terdaftar = []
password_terdaftar = []
email_terdaftar = []
nama_terdaftar = []
gender_terdaftar = []
usia_terdaftar = []
pekerjaan_terdaftar = []
hobi_terdaftar = []
kota_terdaftar = []
rt_terdaftar = []
rw_terdaftar = []
zipcode_terdaftar = []
lat_terdaftar = []
long_terdaftar = []
nohp_terdaftar = []

def menu_awal():
    print("Selamat Datang di Aplikasi Ekspedisi Gudang (Dea & Lauzia)")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

# Program Utama
program_berjalan = "ya"
while program_berjalan == "ya":
    menu_awal()
    opsi = input("Pilih Menu (1/2/3): ")

# ===== REGISTER Validasi UserID & Password =====
    if opsi == "1":
        print("----- Register -----")
        print("Masukkan Data:")

        # Validasi UserID
        status_userid = "belum valid"
        while status_userid == "belum valid":
            userid = input("Masukkan User ID: ")

            if userid.isalpha() or userid.isdigit():
                print("User ID harus kombinasi huruf dan angka")
            elif not userid.isalnum():
                print("User ID tidak boleh mengandung karakter lain")
            elif len(userid) < 6 or len(userid) > 20:
                print("User ID harus terdiri dari 6-20 karakter")
            elif userid in userid_terdaftar:
                print("User ID sudah terdaftar")
            else:
                userid_valid = "sudah valid"
        
        # Validasi Password           
        status_password = "belum valid"
        while status_password == "belum valid":
            password = input("Password: ")

            if len(password) < 8:
                print("Password minimal 8 karakter")
            else:
                #Cek kombinasi
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
                    status_password = "sudah valid"
                else:
                    print("Password harus kombinasi huruf besar, huruf kecil, angka, dan karakter khusus (/.,@#$%)")
    
        # ----- Validasi Email ----- (yg di Assingnment 1 di paling atas)
        status_email = "belum valid"

        while status_email == "belum valid":
            Email = input("Email: ")
            hasil = validasi_email(Email)
            print(hasil)
                
            if hasil == "Alamat Email yg anda Masukkan Valid":
                status_email = "sudah valid"



## ----- Profile Registration -----

        nama_valid = "belum"
        while nama_valid == "belum":
            Nama = input("Masukkan nama Lengkap: ").title()

            if Nama.replace(" ", "").isalpha():
                nama_valid = "sudah"
            else:
                print("Nama hanya boleh mengandung huruf")
        
        gender_valid = "belum"
        while gender_valid == "belum":
            Gender = input("Jenis Kelamin (Male/Female): ").capitalize()

            if Gender == "Male" or Gender == "Female":
                gender_valid = "sudah"
            else:
                print("Jenis Kelamin tidak valid. Harap masukkan 'Male' atau 'Female'")

        usia_valid = "belum"
        while usia_valid == "belum":
            Usia = input("Masukkan usia Anda: ")

            if Usia.isdigit():
                Usia = int(Usia)
                if Usia < 17 or Usia > 80:
                    print("Usia harus antara 17-80 tahun")
                else:
                    usia_valid = "sudah"
            else:
                print("Usia harus berupa angka")

        pekerjaan_valid = "belum"
        while pekerjaan_valid == "belum":
            Pekerjaan = input("Pekerjaan: ").title()

            if Pekerjaan.replace(" ", "").isalpha():
                pekerjaan_valid = "sudah"
            else:
                print("Pekerjaan hanya boleh mengandung huruf")

        
        hobi_valid = "belum"
        while hobi_valid == "belum":
            Hobi = input("Hobi (pisahkan dengan koma jika lebih dari 1): ").title()
            list_hobi = Hobi.split(", ")

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
                    if list_hobi_akhir[i].replace(" ", "").isalpha():
                        jumlah_hobi_alfabet += 1
                    i += 1

                if jumlah_hobi_alfabet == len(list_hobi_akhir):
                    list_hobi = list_hobi_akhir
                    hobi_valid = "sudah"
                else:
                    print("Hobi berisi huruf saja.")


        print("Alamat: ")

        kota_valid = "belum"
        while kota_valid == "belum":
            NamaKota = input("Nama Kota: ")

            if NamaKota.replace(" ", "").isalpha():
                kota_valid = "sudah"
            else:
                print("Nama Kota hanya boleh huruf saja")

        rt_valid = "belum"
        while rt_valid == "belum":
            RT = input("RT: ")

            if RT.isdigit():
                RT = int(RT)
                rt_valid = "sudah"
            else:
                print("RT berupa angka")

        rw_valid = "belum"
        while rw_valid == "belum":
            RW = input("RT: ")

            if RW.isdigit():
                RW = int(RW)
                rw_valid = "sudah"
            else:
                print("RW berupa angka")
        
        zipvode_valid = "belum"
        while rt_valid == "belum":
            ZipCode = int(input("Zip Code: "))

            if len(ZipCode) != 5:
                print("Zip Code minimal 5 digit angka")
            else:
                print("Zip Code berupa angka")
                zipvode_valid = "sudah"

        print("Geo: ")
        lat_valid = "belum"
        while lat_valid == "belum":
            Lat = input("Latitude: ")

            konversi_lat = "ya"
            if konversi_lat == "ya":
                try:
                    Lat = float(Lat)
                    lat_valid = "sudah"
                except:
                    print("Latitude berupa angka desimal")
        
        longitude_valid = "belum"
        while longitude_valid == "belum":
            Longitude = input("Longitude: ")

            konversi_longitude = "ya"
            if konversi_longitude == "ya":
                try:
                    Longitude = float(Longitude)
                    longitude_valid = "sudah"
                except:
                    print("Longitude berupa angka desimal")
        
        
        nohp_valid = "belum"
        while nohp_valid == "belum":
            NoHp = int(input("NoHp: "))

            if len(NoHp) < 11 or len(NoHp) > 13:
                print("NoHp harus terdiri dari 11-13 digit angka")
            else:
                nohp_valid = "sudah"


        ## ----- Simpan Data -----
        status_simpan = "belum"

        while status_simpan == "belum":
            # print("Tidak valid. Silakan masukkan 'Y' atau 'N'.")
            SimpanData = input("Simpan Data? Y/ N): ").upper()

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
                status_simpan = "sudah"
                menu_awal()

            else:
                print("Data tidak disimpan")
                status_simpan = "belum"
                menu_awal()

# ===== LOGIN =====
    elif opsi == "2":
        print("\n----- Login -----")
        
        login_berhasil = "belum"
        batas_login = 5

        while login_berhasil == "belum" and batas_login <= 5:
            userid_login = input("Masukkan ID: ")
            password_login = input("Masukkan Password: ")

        # cek id terdaftar/belum    
        if userid_login not in userid_terdaftar:
            print("ID Tidak Terdaftar. Silakan registrasi.")
            print("Sisa percobaan login:", 3 - batas_login)
            batas_login -= 1
        else:
        # Ambil index user
            idx_user = userid_terdaftar.index(userid_login)

        # cek password
            coba = 1
            batas_coba = 5

            if coba <= batas_coba:
                print(f"Password Salah. Percobaan ke-{coba} dari {batas_coba}")
                password_login = input("Masukkan Password: ")
                coba += 1
            elif password_terdaftar[idx_user] != password_login and coba == batas_coba:
                coba += 1
                print("Password salah. Kesempatan Habis. Silakan coba beberapa saat lagi.")
            else:
                print("Anda Berhasil Login")
                login_berhasil = "sudah"
                            
                # Tampilkan Data User
                print("===== Data Anda =====")
                print("Nama:", nama_terdaftar[idx_user])
                print("Email:", email_terdaftar[idx_user])
                print("Gender:", gender_terdaftar[idx_user])
                print("Usia:", usia_terdaftar[idx_user])
                print("Pekerjaan:", pekerjaan_terdaftar[idx_user])
                print("Hobi:", ", ".join(hobi_terdaftar[idx_user]))
                print("Alamat:")
                print("Nama Kota:", kota_terdaftar[idx_user])
                print("RT:", rt_terdaftar[idx_user])
                print("RW:", rw_terdaftar[idx_user])
                print("Zip Code:", zipcode_terdaftar[idx_user])
                print("Geo:")
                print("Lat:", lat_terdaftar[idx_user])
                print("Longitude:", long_terdaftar[idx_user])
                print("No Hp:", nohp_terdaftar[idx_user])
        
        if login_berhasil == "belum" and batas_login == 0:
            print("Kesempatan login habis. Silakan coba beberapa saat lagi.")
        
        


# ===== EXIT =====
    elif opsi == "3":
        print("----- Exit -----")
        print("Terima Kasih telah menggunakan Aplikasi Ekspedisi Gudang (Dea & Lauzia)")
    else:
        print("Opsi tidak valid. Silakan pilih 1, 2, atau 3.")

 





