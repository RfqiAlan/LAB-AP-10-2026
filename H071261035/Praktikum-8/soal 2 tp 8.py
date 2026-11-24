import re


def validasi_username(username):
  pola = r"^[a-zA-Z][a-zA-Z0-9_]{4,11}$"
  return bool(re.match(pola, username))


def main():
  print("=== Registrasi Username ===")
  print("Ketik 'SELESAI' untuk mengakhiri.")

  username_valid = []

  while True:
    username = input("Masukkan username: ").strip()
    if username.upper() == "SELESAI":
      break

    if validasi_username(username):
      print("Username tersedia.")
      username_valid.append(username)
    else:
      print("Username tidak valid!")

  print("\n=== Rekapitulasi ===")
  print("Username valid:")
  for i, usr in enumerate(username_valid, 1):
    print(f"{i}. {usr}")
  print(f"Jumlah username valid: {len(username_valid)}")


if __name__ == "__main__":
  main()