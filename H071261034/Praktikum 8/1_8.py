import re

def validasi_nim(nim):
    pola = r"^H071\d{6}$"
    if re.match(pola, nim):
        return True
    return False

def validasi_email(email):
    pola = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(pola, email):
        return True
    return False

def validasi_telepon(no_telp):
    pola = r"^\d{10,13}$"
    if re.match(pola, no_telp):
        return True
    return False

def main():
    print("=== Validasi Data Mahasiswa ===")
    
    # Input dari pengguna
    nim_input = input("Masukkan NIM: ")
    email_input = input("Masukkan Email: ")
    telp_input = input("Masukkan No. Telp: ")
    
    # Proses validasi menggunakan fungsi
    status_nim = validasi_nim(nim_input)
    status_email = validasi_email(email_input)
    status_telp = validasi_telepon(telp_input)
    
    print("\n--- Hasil Validasi ---")
    print(f"NIM: {'Valid' if status_nim else 'Format NIM tidak valid!'}")
    print(f"Email: {'Valid' if status_email else 'Format email tidak valid!'}")
    print(f"No. Telepon: {'Valid' if status_telp else 'Nomor telepon tidak valid!'}")
    
    # Pengecekan jika seluruh data valid
    if status_nim and status_email and status_telp:
        print("Data mahasiswa berhasil diverifikasi!")

if __name__ == "__main__":
    main()