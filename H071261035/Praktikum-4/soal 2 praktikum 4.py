def hitung_statistik(*args):
    total = sum(args)
    rata_rata = total / len(args)
    nilai_tertinggi = max(args)
    nilai_terendah = min(args)
    
    return nilai_tertinggi, rata_rata, nilai_terendah

daftar_nilai = []

while True:
    input_nilai = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
    
    if input_nilai == "":
        break
        
    nilai = float(input_nilai)
    daftar_nilai.append(nilai)

if len(daftar_nilai) > 0:
    tertinggi,rata, terendah = hitung_statistik(*daftar_nilai)
    
    if tertinggi.is_integer():
        tertinggi = int(tertinggi)
    if terendah.is_integer():
        terendah = int(terendah)
        
    print(f"Rata-rata kelas: {rata}")
    print(f"Nilai tertinggi: {tertinggi}")
    print(f"Nilai terendah: {terendah}")
else:
    print("Data nilai tidak tersedia.")