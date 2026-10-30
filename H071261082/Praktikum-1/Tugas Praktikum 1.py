#Data Penjualan Kopi Senja
menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]
perubahan_harga = harga[2] + 15000
#         0  1  2

#1
sub_kopi = harga[0] * jumlah[0]
sub_matcha = harga[1] * jumlah[1] 
sub_americano = perubahan_harga * jumlah[2]

#2
subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]

#3
total_seluruh = sum(subtotal_pendapatan)
biaya_operasional = 15000
pendapatan_bersih = total_seluruh - biaya_operasional

#4
jumlah_barang = sum(jumlah)
target_tercapai = total_seluruh > 288000 or jumlah_barang > 10

#5
print("Laporan Penjualan Kopi Senja")
print(f"Subtotal Kopi Susu : Rp{sub_kopi:,}")
print(f"Subtotal Matcha Latte : Rp{sub_matcha:,}")
print(f"Subtotal Americano : Rp{sub_americano:,}")
print(f"Total Seluruh : Rp{total_seluruh:,}")
print(f"Pendapatan Bersih : Rp{pendapatan_bersih:,}")
print(f"Jumlah Barang Terjual : {jumlah_barang}")
print(f"Target Tercapai : {target_tercapai}")