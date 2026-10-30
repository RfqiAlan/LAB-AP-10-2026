def hitung_nilai_ujian(*args):
    if not args:
        return None
    
    total = sum(args)
    jumlah_data = len(args)
    rata_rata = total / jumlah_data
    nilai_tertinggi = max(args) 
    nilai_terendah = min(args)
    
    return rata_rata, nilai_tertinggi, nilai_terendah

def main():
    daftar_nilai = []
    
    while True:
        try:
            user_input = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
            
            if user_input.strip() == "":
                break
            nilai = float(user_input)
            if nilai<0 or nilai> 100:
                print("Angka harus berada di antara 0 dan 100")
                continue
            daftar_nilai.append(nilai)
        except ValueError:
            print("Masukkan angka yang valid!")


    if len(daftar_nilai) == 0:
        print("Data nilai tidak tersedia.")
    else:
        rata, tertinggi, terendah = hitung_nilai_ujian(*daftar_nilai)
        
        print(f"Rata-rata kelas: {rata}")
        print(f"Nilai tertinggi: {tertinggi}")
        print(f"Nilai terendah: {terendah}")


if __name__ == "__main__":
    main()