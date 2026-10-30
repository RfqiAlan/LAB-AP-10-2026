menu = ['Kopi Susu', 'Matcha Latte', 'Americano']
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

sub_kopi = [harga[0]*jumlah[0]]
sub_matcha = [harga[1]*jumlah[1]]
sub_americano = [harga[2]*jumlah[2]]

subtotal_pendapatan = sum(sub_kopi + sub_matcha + sub_americano)

BIAYA_OPERASIONAL = 15000
total_seluruh = subtotal_pendapatan - BIAYA_OPERASIONAL


jumlah_barang = ( jumlah[0] + jumlah[1] + jumlah[2])
target_tercapai = subtotal_pendapatan > 200000 and jumlah_barang > 10

print("Subtotal Pendapatan RP:", subtotal_pendapatan)
print("Pendapatan Bersih RP:", total_seluruh)
print("Hasil Target :", target_tercapai)