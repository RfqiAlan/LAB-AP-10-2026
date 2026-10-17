def konversi(suhu, asal: str, tujuan: str):
    if asal == "C":
        if tujuan == "F":
            nilai = (suhu * 1.8) + 32
            
        elif tujuan == "K":
            nilai = suhu + 273.15
            
        else:
            nilai = suhu
            
    if asal == "F":
        if tujuan == "C":
            nilai = (suhu - 32) * 5 / 9
            
        if tujuan == "K":
            nilai = (suhu -32) * 5 / 9 + 273.15
            
        else:
            nilai = suhu
            
    if asal == "K":
        if tujuan == "C":
            nilai = suhu - 273.15
            
        if tujuan == "F":
            nilai = (suhu - 273.15) * 1.8 + 32
            
        else:
            nilai = suhu

    return nilai


print("=== Konversi Suhu ===")
while True:
    try:
        nilai_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ")
        if nilai_suhu == "selesai":
            break
        suhu = float(nilai_suhu)
        try:
            skala_asal = input("Skala asal (C/F/K): ")
            skala_tujuan = input("Skala tujuan (C/F/K): ")
            if skala_asal != "C" or skala_asal != "F" or skala_asal != "K":
                pass
            if skala_tujuan != "C" or skala_tujuan != "F" or skala_tujuan != "K":
                pass
            konversi_akhir = konversi(suhu, skala_asal, skala_tujuan)
            print(f"Hasil: {suhu} {skala_asal} = {konversi_akhir} {skala_tujuan}")
        except:
            print("Error: Skala suhu tidak dikenali.")
            continue
    except:
        print("Input yang anda masukkan tidak valid")
        continue

