## database untuk paket dan user yg terdaftar

userid_terdaftar = ["admin123", "dea2026", "lauzia99", "user456"]
password_terdaftar = ["Admin@123", "Dea#2026", "Lauzia@99", "User@456"]
email_terdaftar = ["admin@mail.com", "dea@gmail.com", "lauzia@yahoo.com", "user@hotmail.com"]
nama_terdaftar = ["Admin Utama", "Dea Trishnanti", "Lauzia Fadhila", "Budi Santoso"]
gender_terdaftar = ["Male", "Female", "Female", "Male"]
usia_terdaftar = [30, 25, 23, 28]
pekerjaan_terdaftar = ["Manager", "Staff Gudang", "Admin", "Kurir"]
hobi_terdaftar = [
    ["Membaca", "Traveling", "Fotografi"],
    ["Memasak", "Menyanyi", "Berkebun"],
    ["Olahraga", "Menggambar", "Menulis"],
    ["Masak", "Membaca", "Coding"]
]
kota_terdaftar = ["Jakarta", "Bandung", "Surabaya", "Yogyakarta"]
rt_terdaftar = [5, 3, 7, 2]
rw_terdaftar = [10, 8, 12, 6]
zipcode_terdaftar = [12345, 40123, 60271, 55281]
lat_terdaftar = [-6.2088, -6.9175, -7.2575, -7.7956]
long_terdaftar = [106.8456, 107.6191, 112.7521, 110.3695]
nohp_terdaftar = [81234567890, 85678901234, 87654321098, 89012345678]

database_paket = [
    {
        "resi": "EXP001",
        "pengirim": "Ahmad Wijaya",
        "no_hp_pengirim": "081234567890",
        "penerima": "Siti Rahayu",
        "no_hp_penerima": "085678901234",
        "alamat_tujuan": "Jl. Merdeka No. 10, Jakarta Pusat",
        "kategori": "Elektronik",
        "berat": 2.5,
        "tanggal_pengiriman": "15-02-2026",
        "jenis_pengiriman": "D&L Super (Kilat)",
        "estimasi": "1-2 hari",
        "tarif": 37500
    },
    {
        "resi": "EXP002",
        "pengirim": "Budi Santoso",
        "no_hp_pengirim": "082345678901",
        "penerima": "Ani Kusuma",
        "no_hp_penerima": "087654321098",
        "alamat_tujuan": "Jl. Sudirman No. 25, Bandung",
        "kategori": "Pakaian/Tekstil",
        "berat": 1.2,
        "tanggal_pengiriman": "14-02-2026",
        "jenis_pengiriman": "D&L Reguler",
        "estimasi": "2-5 hari",
        "tarif": 12000
    },
    {
        "resi": "EXP003",
        "pengirim": "Dewi Lestari",
        "no_hp_pengirim": "089012345678",
        "penerima": "Rudi Hartono",
        "no_hp_penerima": "081234567890",
        "alamat_tujuan": "Jl. Gatot Subroto No. 50, Surabaya",
        "kategori": "Dokumen",
        "berat": 0.5,
        "tanggal_pengiriman": "16-02-2026",
        "jenis_pengiriman": "D&L Super (Kilat)",
        "estimasi": "1-2 hari",
        "tarif": 7500
    }
]

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