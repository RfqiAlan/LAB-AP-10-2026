# #re.match(): cocok dari awal
# import re

# pattern = 'a...s$'
# test_string = 'abyss'
# result = re.match(pattern, test_string)

# if result:
#     print("search successfull.")
# else:
#     print("search unsuccessful.")

# import re

# pattern = 's...a$'
# test_string = 'semua'
# result = re.match(pattern, test_string)

# if result:
#     print("cocok")
# else:
#     print("tidak cocok")

# #metacharacters 
# import re
# teks = "siswa kelas saya ada B dan C."

# hasil = re.findall(r'[ABC]', teks)
# print(hasil)

# import re
# teks= "Nilai:  A,B,C,D,E."

# hasil = re.findall(r'[ABC]', teks)
# print(hasil)

# .period

# import re
# teks = "kotak, katak,  kitak, ktak"

# hasil =  re.findall(r'k.tak', teks)
# print(hasil)

# import re
# teks = "kapal, kopal,  kapur, kal"

# hasil =  re.findall(r'k...l', teks)
# print(hasil)

# # ^caret
# import re
# teks = "DD 1234 XY adalah mobil saya"
# if re.search(r'^DD', teks):
#     print("ini plat makassar")
# else:
#     print("bukan plat makassar")

# import re
# teks = "621234567890"
# if re.search(r'^08', teks):
#     print("Valid")
# else:
#     print("tidak valid")

# # $dollar
# import re
# file = "foto_liburan.jpg"
# if re.search(r'jpg$', file):
#     print("ini adalah file gambar.")
# else:
#     print("bukan file gambar.")

# import re
# file = "laporan,.pdf.exe"
# if re.search(r'pdf$', file):
#     print("diterima.")
# else:
#     print("ditolak.")

# # *star
# import re
# teks = "Gl, Gol, Goool, Goooooool"
# hasil = re.findall(r'Go*l', teks)
# print(hasil)

# import re
# teks = "1, 10, 100, 1000"
# hasil = re.findall(r'10*', teks)
# print(hasil)

# # +plus
# import re
# teks = "7, 42, 2024"
# hasil = re.findall(r'[0-9]+', teks)
# print(hasil)

# import re
# teks = "color, colour, colouur" 
# hasil = re.findall(r'colou?r', teks)
# print(hasil)

# import re
# teks = "PIN saya 1234 dan PIN dia 1234567"
# hasil = re.findall(r'\d{4,6}', teks)
# print(hasil)

# import re
# teks = "7, 42, 365"
# hasil = re.findall(r'\d{2,3}', teks)
# print(hasil)

# import re
# teks = "Meja 1 kopi, Meja 2 susu, Meja 3 teh"
# x = re.findall(r'kopi|teh|susu', teks)
# print(x)

# import re
# teks = "Senin, Sabtu, Minggu, Rabu"
# hasil= re.findall(r'Sabtu|Minggu', teks)
# print(hasil)

# import re
# teks = "file_saya.pdf, tugas.doc, tugas.docx"
# hasil = re.findall(r'tugas\.(docx?)', teks)
# print(hasil)

# import re
# teks = "ayam goreng, ayam bakar, ayam goreng"
# hasil = re.findall(r'ayam (goreng|bakar)', teks)
# print(hasil)

# import re
# teks = "harganya adalah ^100 dollar."
# hasil = re.findall(r'^[0-9]+', teks)
# print(hasil)

# import re
# teks = "pi = 3.14 dan 3x14, 8.767.71"
# hasil = re.findall(r'[0-9]\.[0-9][0-9]', teks)
# print(hasil)

# import re
# teks = "cat in the acategory"
# hasil = re.findall(r'Bcat', teks)
# print(hasil)

# import re
# teks = "Order A17 dan B205"
# hasil = re.findall(r'\d[0-9]+', teks)
# print(hasil)

# import re
# teks = "Kopi Rp15000, teh Rp 8000, susu Rp 12000"
# hasil = (re.findall(r'Rp\s?\d+', teks))
# print(hasil)
