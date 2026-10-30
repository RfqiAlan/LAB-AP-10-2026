def rekap_nilai(*args):
    """Mengembalikan (rata-rata, tertinggi, terendah) dari semua nilai."""
    rata = sum(args) / len(args)
    return rata, max(args), min(args)


daftar_nilai = []
while True:
    teks = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
    if teks == "":
        break
    try:
        nilai = int(teks)
        daftar_nilai.append(nilai)
    except ValueError:
        print("Input tidak valid")

if len(daftar_nilai) == 0:
    print("Data nilai tidak tersedia.")
else:
    rata, tertinggi, terendah = rekap_nilai(*daftar_nilai)
    print(f"Rata-rata kelas: {rata}")
    print(f"Nilai tertinggi: {tertinggi}")
    print(f"Nilai terendah: {terendah}")