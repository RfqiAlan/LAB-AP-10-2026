def hitung_statistik(*args):
    if not args:
        return None, None, None

    rata_rata = sum(args) / len(args)
    nilai_tertinggi = max(args)
    nilai_terendah = min(args)

    return nilai_tertinggi, rata_rata, nilai_terendah


daftar_nilai = []

while True:
    input_user = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
    
    

    if input_user.strip() == "":
        break
   

    try:
        nilai = float(input_user)
        if nilai < 0 or nilai >100:
            print("input tidak valid")
            continue
        daftar_nilai.append(nilai)
    except ValueError:
        print("Input tidak valid! Harap masukkan angka.")

if daftar_nilai:
    rata_rata, tertinggi, terendah = hitung_statistik(*daftar_nilai)
    print(f"Rata-rata kelas: {rata_rata}")
    print(f"Nilai tertinggi: {int(tertinggi) }")
    print(f"Nilai terendah: {int(terendah) }")
else:
    print("Data nilai tidak tersedia.")