def konversi_suhu(suhu, skala_asal, skala_tujuan):
    skala_valid = ['C', 'F', 'K']
    skala_asal = skala_asal.upper()
    skala_tujuan = skala_tujuan.upper()
    
    if skala_asal not in skala_valid or skala_tujuan not in skala_valid:
        raise ValueError("Skala suhu tidak dikenali.")
    

    if skala_asal == 'C':
        suhu_celsius = suhu
    elif skala_asal == 'F':
        suhu_celsius = (suhu - 32) * 5 / 9
    elif skala_asal == 'K':
        suhu_celsius = suhu - 273.15

    #Skala tujuan 
    if skala_tujuan == 'C':
        hasil = suhu_celsius
    elif skala_tujuan == 'F':
        hasil = (suhu_celsius * 9 / 5) + 32
    elif skala_tujuan == 'K':
        hasil = suhu_celsius + 273.15
        
    return hasil

def main():
    print("=== Konversi Suhu ===")
    while True:
        user_input = input("Masukkan suhu (atau 'selesai' untuk keluar): ")
        
        if user_input.strip().lower() == 'selesai':
            break
            
        try:
            suhu = float(user_input)
            skala_asal = input("Skala asal (C/F/K): ")
            skala_tujuan = input("Skala tujuan (C/F/K): ")
            
            hasil = konversi_suhu(suhu, skala_asal, skala_tujuan)
            
            print(f"Hasil: {suhu} {skala_asal.upper()} = {hasil} {skala_tujuan.upper()}")
            
        except ValueError as e:
            if str(e) == "Skala suhu tidak dikenali.":
                print(f"Error: {e}")
            else:
                print("Error: Masukkan nilai angka yang valid untuk suhu.")

if __name__ == "__main__":
    main()