umur = int(input("Masukkan umur anda: "))
if umur >=21 and umur <=35:
    nilai = int(input())
    pengalaman = int(input())
    if nilai >= 80:
        print("Langsung lolos ke tahap wawancara")
    elif nilai >= 65 and pengalaman >=2:
       print("Bisa mengikuti tes")
    else:
       print("Tidak bisa mengikuti tes")
       



else:
    print("Tidak bisa mengikuti tes")
