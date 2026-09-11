menu = ["Kopi susu", "Matcha latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

sub_kopi = harga[-3] * jumlah[-3]
sub_matcha = harga[-1] * jumlah[-1]
sub_americano = harga[-2] * jumlah[-2]

subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]

total_pendapatan = sum(subtotal_pendapatan)
total_barang = sum(jumlah)

BIAYA_OPERASIONAL = 15000
pendapatan_bersih = total_pendapatan - BIAYA_OPERASIONAL

target = total_pendapatan>200000 and total_barang>10

print("subtotal kopi susu", sub_kopi)
print("subtotal matcha latte", sub_matcha)
print("subtotal americano", sub_americano)
print("pendapatan bersih", pendapatan_bersih)
print("hasil target", target)