import re

list_username = []

def validasi_username(daftar_username,username):
    pattern = r'^[a-zA-Z]\w{4,11}$'
    hasil = re.match(pattern,username)
    if hasil:
        daftar_username.append(username)
        return "Username Tersedia"
    else:
        return "Username Tidak Valid"
    
while True:
    username = input("Masukkan Username: ")
    if username == 'SELESAI':
        break
    
    status = validasi_username(list_username,username)
    print(status,"\n")
    
print("=== Rekapitulasi ===")
print("Username Valid: ")
for idx,item in enumerate(list_username, 1):
    print(f"{idx}. {item}")
print(f"Jumlah Username Valid: {len(list_username)}")
    
    
    