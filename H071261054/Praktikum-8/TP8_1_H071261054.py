import re

def validasi_nim(nim):
    pattern = r'^H071\d{6}$'
    result = re.match(pattern, nim)
    if result:
        return True
    return False

def validasi_email(email):
    pattern = r'^[\w+\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$'
    result = re.match(pattern, email)
    if result:
        return True
    return False

def validasi_no(no):
    pattern = r'-'
    replace = ''
    hasil = re.sub(pattern,replace,no)
    if hasil.isdigit() and 10 <= len(hasil) <= 13:
        return True
    return False

def result_validasi(nim, email, no):
    is_nim_valid = validasi_nim(nim)
    is_email_valid = validasi_email(email)
    is_no_valid = validasi_no(no)
    
    print(f"Nim        : {'Valid' if is_nim_valid else 'Tidak Valid'}")
    print(f"Email      : {'Valid' if is_email_valid else 'Tidak Valid'}")
    print(f"No.Telepon : {'Valid' if is_no_valid else 'Tidak Valid'}\n")
    
    if is_nim_valid and is_email_valid and is_no_valid:
        print("Data Mahasiswa berhasil divalidasi")
    else:
        print("Data Mahasiswa Gagal divalidasi")

nim = input("Masukkan Nim: ")
email = input("Masukkan Email: ")
no = input("Masukkan No. Telepon: \n")

print("=== Validasi Mahasiswa ===")
result_validasi(nim,email,no)