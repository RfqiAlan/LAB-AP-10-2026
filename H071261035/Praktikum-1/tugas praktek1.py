# Data awal
menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

# 1. Menentukan subtotal untuk masing-masing menu
sub_kopi = harga[0] * jumlah[0]
sub_matcha = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]

# 2. Memasukkan subtotal ke dalam list
# subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]

# 3. Menghitung total seluruh pendapatan dan pendapatan bersih
BIAYA_OPERASIONAL = 15000
total_seluruh = (sub_kopi + sub_matcha + sub_americano)
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

# 4. Menghitung jumlah barang terjual dan evaluasi target
total_barang = (jumlah [0] + jumlah [1] + jumlah [2])
target_tercapai = total_seluruh == 213000 and total_barang > 10

# Output hasil
print(f"Subtotal Pendapatan per Menu:")
print(f"- {menu[0]}: Rp{sub_kopi:,}")
print(f"- {menu[1]}: Rp{sub_matcha:,}")
print(f"- {menu[2]}: Rp{sub_americano:,}")
print("-" * 30)
print(f"Total Seluruh Pendapatan : Rp{total_seluruh:,}")
print(f"Biaya Operasional        : Rp{BIAYA_OPERASIONAL:,}")
print(f"Pendapatan Bersih        : Rp{pendapatan_bersih:,}")
print(f"Total Barang Terjual     : {total_barang} item")
print(f"Target Tercapai (>200rb & >10 item) : {target_tercapai}")