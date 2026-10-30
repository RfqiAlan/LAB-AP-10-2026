import re


def validasi_nim(nim):
  pola = r"^H071\d{6}$"
  return bool(re.match(pola, nim))


def validasi_email(email):
  pola = r"^[\w\.-]+@[\w\.-]+\.\w+$"
  return bool(re.match(pola, email))


def validasi_telepon(telepon):
  pola = r"^\d{10,13}$"
  return bool(re.match(pola, telepon))


def main():
  print("=== Validasi Data Mahasiswa ===")
  nim = input("Masukkan NIM        : ").strip()
  email = input("Masukkan Email      : ").strip()
  telp = input("Masukkan No. Telp   : ").strip()

  is_nim_valid = validasi_nim(nim)
  is_email_valid = validasi_email(email)
  is_telp_valid = validasi_telepon(telp)

  print("\n--- Hasil Validasi ---")
  print(f"NIM\t\t: {'Valid' if is_nim_valid else 'Format NIM tidak valid!'}")
  print(
      f"Email\t\t:"
      f" {'Valid' if is_email_valid else 'Format email tidak valid!'}"
  )
  print(
      f"No. Telepon\t: {'Valid' if is_telp_valid else 'Nomor telepon tidak valid!'}"
  )

  if is_nim_valid and is_email_valid and is_telp_valid:
    print("\nData mahasiswa berhasil diverifikasi!")


if __name__ == "__main__":
  main()