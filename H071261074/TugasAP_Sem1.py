menu = ['Kopi Susu', 'Matcha Latte', 'Americano']
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]
harga[1] = 25000 
latte = harga[1] + 5000

# Soal NO 1 : Menghitung subtotal pendapatan 
sub_kopi = harga[0]*jumlah[0]
sub_matcha = harga[1]* jumlah[1]
sub_americano = harga[2]*jumlah[2]

# Soal NO 2 : Menghitung total pendapatan bersih 
subtotal_pendapatan = sum ([sub_kopi, sub_matcha, sub_americano])

# Soal NO 3 : Menghitung total pendapatan bersih 
BIAYA_OPERASIONAL = 15000

total_seluruh = subtotal_pendapatan - BIAYA_OPERASIONAL
pendapatan_bersih = total_seluruh

# Soal NO 4 : Membuat kondisi apakah target tercapai atau tidak 
jumlah_barang = jumlah[0]+jumlah[1]+jumlah[2]
target_tercapai = subtotal_pendapatan > 213000 and jumlah_barang > 10

# Menampilkan hasil 
print("Subtotal Pendapatan: Rp", subtotal_pendapatan)
print("Pendapatan Bersih: Rp", pendapatan_bersih)
print("Target Tercapai:", target_tercapai)