class Pemain:
    def __init__(self, nama, id_pemain, role, kill, assist, objective):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.kill = kill
        self.assist = assist
        self.objective = objective

    def hitung_skor_akhir(self):
        skor = (0.3 * self.kill) + (0.3 * self.assist) + (0.4 * self.objective)
        return skor

    def status_performa(self):
        skor = self.hitung_skor_akhir()
        if skor >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"

    def tampilkan_data(self, no):
        print(f"| {no:<2} | {self.nama:<10} | {self.id_pemain:<10} | {self.role:<10} | {self.hitung_skor_akhir():<10.2f} | {self.status_performa():<14} |")


print("=== SISTEM PENILAIAN PERFORMA PEMAIN ===")
print()

data = []
jumlah = int(input("Masukkan jumlah pemain: "))

for i in range(jumlah):
    print()
    print(f"-- Data Pemain ke-{i + 1} --")
    nama = input("Nama: ")
    id_pemain = input("ID Pemain: ")
    role = input("Role: ")
    kill = float(input("Nilai Kill: "))
    assist = float(input("Nilai Assist: "))
    objective = float(input("Nilai Objective: "))

    p = Pemain(nama, id_pemain, role, kill, assist, objective)
    data.append(p)

garis = "=" * 78
print()
print("=== REKAPITULASI PERFORMA PEMAIN ===")
print(garis)
print(f"| {'No':<2} | {'Nama':<10} | {'ID Pemain':<10} | {'Role':<10} | {'Skor Akhir':<10} | {'Status':<14} |")
print(garis)

no = 1
for p in data:
    p.tampilkan_data(no)
    no += 1

print(garis)