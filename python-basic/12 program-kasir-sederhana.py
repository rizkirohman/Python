print()
print("=================== All About Seblak ===================")
print()
print("--- Menu Seblak: ")
print()
print("1. Seblak Original ------ Rp. 10.000")
print("2. Seblak Ceker --------- Rp. 15.000")
print("3. Seblak Tulang -------- Rp. 12.000")
print("4. Seblak Campur -------- Rp. 17.000")
print()

pilih_menu = input("Pilih Menu [1/2/3/4] \t: ")
if pilih_menu == '1':
  porsi = int(input('Jumlah Porsi \t\t: '))
  harga_seblak_original = 10000
  harga = harga_seblak_original * porsi
  print(f"Total Bayar \t\t: Rp. {harga}")
  uang_tunai = int(input("Uang Tunai \t\t: Rp. "))
  kembalian = uang_tunai - harga
  print(f"Uang Kembalian \t\t: Rp. {kembalian}")

elif pilih_menu == '2':
  porsi = int(input('Jumlah Porsi \t\t: '))
  harga_seblak_ceker = 15000
  harga = harga_seblak_ceker * porsi
  print(f"Total Bayar \t\t: Rp. {harga}")
  uang_tunai = int(input("Uang Tunai \t\t: Rp. "))
  kembalian = uang_tunai - harga
  print(f"Uang Kembalian \t\t: Rp. {kembalian}")

elif pilih_menu == '3':
  porsi = int(input('Jumlah Porsi \t\t: '))
  harga_seblak_tulang = 12000
  harga = harga_seblak_tulang * porsi
  print(f"Total Bayar \t\t: Rp. {harga}")
  uang_tunai = int(input("Uang Tunai \t\t: Rp. "))
  kembalian = uang_tunai - harga
  print(f"Uang Kembalian \t\t: Rp. {kembalian}")

elif pilih_menu == '4':
  porsi = int(input('Jumlah Porsi \t\t: '))
  harga_seblak_campur = 17000
  harga = harga_seblak_campur * porsi
  print(f"Total Bayar \t\t: Rp. {harga}")
  uang_tunai = int(input("Uang Tunai \t\t: Rp. "))
  kembalian = uang_tunai - harga
  print(f"Uang Kembalian \t\t: Rp. {kembalian}")
