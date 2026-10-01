list_nilai_ujian = []

def hitung_nilai(*daftar_nilai):
    total_nilai = sum(daftar_nilai)
    jumlah_nilai = len(daftar_nilai)
    rata_rata = total_nilai / jumlah_nilai
    
    max_nilai = max(daftar_nilai)
    min_nilai = min(daftar_nilai)
    
    return rata_rata, max_nilai, min_nilai

while True:
    try:
        input_user = input("Masukkan Nilai Ujian (kosongkan lalu Enter untuk selesai): ")
        
        if input_user.strip() == "":
            if list_nilai_ujian:
                rata_rata, max_nilai, min_nilai = hitung_nilai(*list_nilai_ujian)
                print('\n--- HASIL ANALISIS ---')
                print('Rata-Rata Kelas : ', rata_rata)
                print('Nilai Tertinggi : ', max_nilai)
                print('Nilai Terendah  : ', min_nilai)
                break
            else:
                print('Data tidak tersedia.')
                break
        
        nilai_ujian = input_user.split(",")
        
        for x in nilai_ujian:
            if x.strip() != "":
                nilai_angka = int(x.strip())
                list_nilai_ujian.append(nilai_angka)
                
    except ValueError:
        print("Input Tidak Valid! Pastikan hanya memasukkan angka dan koma.")
