def celcius_ke_fahrenheit(c):
    return (c * 9/5) + 32

def celcius_ke_kelvin(c):
    return c + 273.15

def fahrenheit_ke_celcius(f):
    return (f - 32) * 5/9

def fahrenheit_ke_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_ke_celcius(k):
    return k - 273.15

def kelvin_ke_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def konversi_suhu(suhu, dari_skala, ke_skala):
    if dari_skala == ke_skala:
        return suhu
        
    if dari_skala == 'C' and ke_skala == 'F':
        return celcius_ke_fahrenheit(suhu)
    elif dari_skala == 'C' and ke_skala == 'K':
        return celcius_ke_kelvin(suhu)
    elif dari_skala == 'F' and ke_skala == 'C':
        return fahrenheit_ke_celcius(suhu)
    elif dari_skala == 'F' and ke_skala == 'K':
        return fahrenheit_ke_kelvin(suhu)
    elif dari_skala == 'K' and ke_skala == 'C':
        return kelvin_ke_celcius(suhu)
    elif dari_skala == 'K' and ke_skala == 'F':
        return kelvin_ke_fahrenheit(suhu)
    else:
        return None

print("=== Masukkan Suhu ===")

while True:
    suhu = input("Masukkan Suhu (atau 'selesai' untuk berhenti) ")
    if suhu != 'selesai':
        suhu_float = float(suhu)
        skala_asal = input('Masukkan Skala Asal(C/F/K)').upper()
        skala_tujuan = input('Masukkan Skala Tujuan(C/F/K)').upper()
        
        hasil_konversi = konversi_suhu(suhu_float, skala_asal, skala_tujuan)
        
        if hasil_konversi:
            print(f"hasil: {suhu_float} {skala_asal} = {hasil_konversi} {skala_tujuan}")
        else:
            print("Error : skala tidak ditemukan")
    else:
        break
    
    