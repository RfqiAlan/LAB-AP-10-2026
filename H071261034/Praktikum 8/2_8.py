import re

def cek_username(teks_username):
    pola = r"^[a-zA-Z][\w_]{4,11}$"
    
    if " " in teks_username:
        return False
        
    if re.match(pola, teks_username):
        return True
    return False

def main():
    print("=== Registrasi Username ===")
    print("Ketik 'SELESAI' untuk mengakhiri.\n")
    
    daftar_username_valid = []
    
    while True:
        input_pengguna = input("Masukkan username: ")
        
        if input_pengguna.upper() == "SELESAI":
            break
            
        if cek_username(input_pengguna):
            print("Username tersedia.")
            daftar_username_valid.append(input_pengguna)
        else:
            print("Username tidak valid!")
            
    print("\n=== Rekapitulasi ===")
    print("Username valid:")
    
    for nomor, nama_user in enumerate(daftar_username_valid, start=1):
        print(f"{nomor}. {nama_user}")
        
    print(f"\nJumlah username valid: {len(daftar_username_valid)}")

if __name__ == "__main__":
    main()