usia = int(input('Masukkan umur: '))
if 21 < usia < 35 :
    nilai = int(input("Masukkan nilai tes:"))
    pengalaman = int(input("Masukkan pengalaman kerja (tahun) :"))

    if nilai > 0 :
        if nilai >= 80:
            print('Lolos ke Tahap Wawancara')
        elif nilai > 65 and pengalaman > 2:
            print('Lolos Bersyarat')
    else:
        print("Tidak Lolos")
else:
    print('Tidak Lolos')