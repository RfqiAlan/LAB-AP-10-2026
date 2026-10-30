def hitung_subtotal(harga, jumlah, adalah_member=False):
    """Menghitung subtotal satu barang. Member dapat diskon 10%."""
    subtotal = harga * jumlah
    if adalah_member:
        subtotal = subtotal * 90 // 100   
    return subtotal


print("Selamat datang di Kasir Minimarket!")
status = input("Apakah Anda member? (y/n): ")
member = status.lower() == "y"
print(f"member: {member}")

total = 0
while True:
    nama = input("Masukkan nama barang (kosongkan untuk selesai): ")
    if nama == "":
        break
    harga = int(input("Harga barang: "))
    jumlah = int(input("Jumlah barang: "))

    subtotal = hitung_subtotal(harga, jumlah, member)
    print(f"Subtotal {nama}: Rp{subtotal}")
    total += subtotal

print(f"Total belanja: Rp{total}")