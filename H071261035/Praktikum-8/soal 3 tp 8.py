import re


def main():
  print("=== Pembersihan Data Nomor Telepon ===")
  try:
    jumlah_data = int(input("Masukkan jumlah data: "))
  except ValueError:
    print("Jumlah data harus berupa angka.")
    return

  daftar_data = []
  for i in range(1, jumlah_data + 1):
    nomor = input(f"Nomor ke-{i}: ")
    daftar_data.append(nomor)

  print("\n--- Hasil Pembersihan ---")
  nomor_valid_list = []

  for i, nomor_sebelum in enumerate(daftar_data, 1):
    nomor_sesudah = re.sub(r"[\s-]", "", nomor_sebelum)

    pola_valid = r"^\d{10,13}$"
    if re.match(pola_valid, nomor_sesudah):
      status = "Valid"
      nomor_valid_list.append(nomor_sesudah)
    else:
      status = "Tidak valid"

    print(f"Data {i}:")
    print(f"Sebelum: {nomor_sebelum}")
    print(f"Sesudah: {nomor_sesudah}")
    print(f"Status : {status}\n")

  print(f"Jumlah nomor valid: {len(nomor_valid_list)}")


if __name__ == "__main__":
  main()