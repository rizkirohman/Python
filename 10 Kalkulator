def tambah(x, y):
  return x + y

def kurang(x, y):
  return x - y

def kali(x, y):
  return x * y

def bagi(x, y):
  return x / y

def menu():
  print()
  print("Pilih Operasi: ")
  print()
  print("1. Penjumlahan")
  print("2. Pengurangan")
  print("3. Perkalian")
  print("4. Pembagian")
  print("5. Exit")
  print()
  
def pilih_operasi():
  pilihan = input("Pilih (1/2/3/4/5): ")
  print()
  if (pilihan == '1') or (pilihan == '2') or (pilihan == '3') or (pilihan == '4'):
    bil1 = int(input("Masukkan angka pertama: "))
    bil2 = int(input("Masukkan angka kedua: "))
    print()
    if pilihan == '1':
      print(f"{bil1} + {bil2} = {tambah(bil1, bil2)}")
    elif pilihan == '2':
      print(f"{bil1} - {bil2} = {kurang(bil1, bil2)}")
    elif pilihan == '3':
      print(f"{bil1} * {bil2} = {kali(bil1, bil2)}")
    elif pilihan == '4':
      print(f"{bil1} / {bil2} = {bagi(bil1, bil2)}")
  elif pilihan == '5':
      print("Good bye, Have a nice day!")
      exit()

  else:
    print("Pilihan tidak tersedia")
    print("Kembali ke menu? ")
    print("1. Ya")
    print("2. Tidak")

    kembaliKe_menu = input ("Pilih(1/2): ")

    if kembaliKe_menu == '1':
      menu()
      pilih_operasi()
    else:
      print()
      print("Good bye, Have a nice day!")
      exit()

  print()
  print("Kembali Menghitung? ")
  print("1. Ya")
  print("2. Tidak")
  print()
  kembali_menghitung = input("Pilih (1/2): ")
  if kembali_menghitung == '1':
    menu()
    pilih_operasi()
  else:
    print()
    print("Good bye, Have a nice day!")
    exit()

menu()
pilih_operasi()
