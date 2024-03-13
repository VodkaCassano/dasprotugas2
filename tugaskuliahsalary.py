class Karyawan:
    def __init__(self, nama, gaji_per_jam):
        self.nama = nama
        self.gajiperjam = gaji_per_jam

    def hitung_gaji_per_hari(self):
        return self.gajiperjam * 8

    def hitung_gaji_per_minggu(self):
        return self.hitung_gaji_per_hari() * 6 

    def hitung_gaji_per_bulan(self):
        return self.hitung_gaji_per_minggu() * 4  


def main():
    try:
        nama_karyawan = input("Masukkan nama karyawan: ")
        gajiperjam = float(input("Masukkan gaji per jam: "))

        karyawan = Karyawan(nama_karyawan, gajiperjam)

        print("\nGaji", karyawan.nama)
        print("Gaji per hari: Rp.", karyawan.hitung_gaji_per_hari())
        print("Gaji per minggu: Rp.", karyawan.hitung_gaji_per_minggu())
        print("Gaji per bulan: Rp.", karyawan.hitung_gaji_per_bulan())
    except ValueError:
        print("Error: Masukkan gaji per jam dalam format numerik yang benar.")


if __name__ == "__main__":
    main()
