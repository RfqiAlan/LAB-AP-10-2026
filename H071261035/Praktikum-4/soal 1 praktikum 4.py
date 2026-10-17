def hitung_subtotal(harga, jumlah, adalah_member=False):
    subtotal = harga * jumlah
    if adalah_member:
        # Jika member, dapat diskon 10%
        subtotal = subtotal * 0.9
    return int(subtotal)

print("Selamat datang di Kasir Minimarket!")
status = input("Apakah Anda member? (y/n): ")

is_member = False
if status.lower() == 'y':
    is_member = True

total_belanja = 0

while True:
    nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ")
    
    if nama_barang == "q":
        break
        
    harga = int(input("Harga barang: "))
    jumlah = int(input("Jumlah barang: "))
    
    subtotal = hitung_subtotal(harga, jumlah, is_member)
    print(f"Subtotal {nama_barang}: Rp{subtotal}")
    
    total_belanja += subtotal

print(f"Total belanja: Rp{total_belanja}")