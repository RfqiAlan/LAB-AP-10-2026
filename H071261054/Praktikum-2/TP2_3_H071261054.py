# Nomor 3
print("KRITERIA KELOLOSAN PELAMAR")
print("==========================")


umur = int(input("Masukkan Usia Anda"))

if umur > 21:
    nilai = int(input("Masukkan Nilai Tes : "))
    pengalaman = int(input("Masukkan Pengalaman Kerja (tahun) : "))
    
    if nilai>=80:
        status = "Lolos ke Tahap Wawancara"
    elif nilai>=65 and pengalaman >=2:
        status = "Lolos Bersyarat"
    else:
        status = "Tidak Lolos"
else:
    print("Umur Belum Cukup")

print(status)

# tambahkan syrat usia > 21 ketika ndak memnuhi umur tidak memenuhi tidak bisa tes