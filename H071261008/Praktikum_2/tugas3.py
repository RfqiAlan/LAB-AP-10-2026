nilai_tes = int(input("Masukkan nilai tes: "))
pengalaman_kerja = int(input("Masukkan pengalaman kerja (tahun): "))

if nilai_tes <= 0 and pengalaman_kerja < 0:
    print("Tidak logis")
elif nilai_tes >= 80:
    print("Lolos ke Tahap Wawancara")
elif nilai_tes <=80 and pengalaman_kerja >= 2:
    print("Lolos Bersyarat")
else:
    print("Tidak Lolos")