menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

sub_kopi = harga[0] * jumlah[0]
sub_matcha = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]

subtotal_pendapatan = [sub_kopi, sub_matcha, sub_americano]

BIAYA_OPERASIONAL = 15000
total_seluruh = sum(subtotal_pendapatan)
pendapatan_bersih = total_seluruh - BIAYA_OPERASIONAL

jumlah_barang = sum(jumlah)
target_tercapai = total_seluruh > 213000 or jumlah_barang > 10

print("Subtotal Kopi Susu:", sub_kopi)
print("Subtotal Matcha Latte:", sub_matcha)
print("Subtotal Americano:", sub_americano)
print("Pendapatan Bersih:", pendapatan_bersih)
print("Target Tercapai:", target_tercapai)
print("Total Seluruh:", total_seluruh)