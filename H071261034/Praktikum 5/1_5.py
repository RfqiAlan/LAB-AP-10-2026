def bersihkan_teks(teks):
    hasil = ""
    alfabet = "abcdefghijklmnopqrstuvwxyz"

    for huruf in teks.lower():
        if huruf in alfabet:
            hasil += huruf

    return hasil


def cek_palindrome(teks):
    return teks == teks[::-1]


def inti_palindrome(teks):
    terbalik = ""

    for i in range(len(teks)):
        for j in range(i + 1, len(teks) + 1):
            kata = teks[i:j]

            if cek_palindrome(kata):
                if len(kata) > len(terbalik):
                    terbalik = kata

    return {
        "teks": terbalik,
        "panjang": len(terbalik),
        "indeks_awal": teks.index(terbalik)
    }


teks = input("Masukkan teks prasasti: ")

bersih = bersihkan_teks(teks)

print("Teks Bersih:", bersih)
print("Output Terharap:", inti_palindrome(bersih))