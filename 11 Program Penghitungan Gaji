import locale
locale.setlocale(locale.LC_ALL, 'IND')

def kalkulatorgaji():
  print()
  print("================ PROGRAM PENGHITUNGAN GAJI ================")
  print()

  while True:
    nama_pegawai = input("Nama Pegawai \t\t: ")
    if all(x.isalpha() or x.isspace() for x in nama_pegawai):
      break
    else:
      print()
      print("Error: Nama harus berupa huruf") 
      print()
      False

  while True:
    nip = input("No Induk Pegawai (NIP) \t: ")
    if nip.isdigit():
      break
    else:
      print()
      print("Error: NIP harus berupa angka")
      print()
      False

  print()
  print("1. CEO")
  print("2. VP")
  print("3. Manager")
  print("4. Staf")
  print()

  while True:
    def rupiah(gaji):
      return "{0:n}".format(gaji)

    def gaji_bos():
      total_gaji = gaji_pokok + tunjangan
      print()
      print(f"Nama \t\t: {nama_pegawai}")
      print(f"NIK \t\t: {nip}")
      print(f"Jabatan \t: {jab}")
      print(f"Gaji Pokok \t: Rp. {rupiah(gaji_pokok)}")
      print(f"Tunjangan \t: Rp. {rupiah(tunjangan)}")
      print(f"Total Gaji \t: Rp. {rupiah(total_gaji)}")

    def gaji_staf():
      print()
      print("Lembur: ")
      print()
      print("1. 1 Jam")
      print("2. 2 Jam")
      print("3. 3 Jam")
      print()
      uang_lembur = 50000
      jam_lembur = int(input("Pilih [1/2/3]: "))
      if jam_lembur == 1:
        gaji_lembur = uang_lembur * jam_lembur  
      elif jam_lembur == 2:
        gaji_lembur = uang_lembur * jam_lembur
      elif jam_lembur == 3:
        gaji_lembur = uang_lembur * jam_lembur
      else:
        False

      total_gaji_staf = gaji_pokok_staf + tunjangan_staf + gaji_lembur

      print()
      print(f"Nama \t\t: {nama_pegawai}")
      print(f"NIK \t\t: {nip}")
      print(f"Jabatan \t: {jab_staf}")
      print(f"Gaji Pokok \t: Rp. {rupiah(gaji_pokok_staf)}")
      print(f"Tunjangan \t: Rp. {rupiah(tunjangan_staf)}")
      print(f"Lembur \t\t: Rp. {rupiah(gaji_lembur)}")
      print(f"Total Gaji \t: Rp. {rupiah(total_gaji_staf)}")
      

    jabatan = input("Pilih Jabatan (1/2/3/4) : ")
    if (jabatan == '1') or (jabatan == '2') or (jabatan == '3') or (jabatan == '4'):
      if jabatan == '1':
        gaji_pokok = 80000000
        tunjangan = 5000000
        jab = "CEO"
        gaji_bos()
          
      elif jabatan == '2':
        gaji_pokok = 50000000
        tunjangan = 3000000
        jab = "VP"
        gaji_bos()

      elif jabatan == '3':
        gaji_pokok = 30000000
        tunjangan = 2000000
        jab = "Manager"
        gaji_bos()

      elif jabatan == '4':
        gaji_pokok_staf = 5000000
        tunjangan_staf = 1000000
        jab_staf = "Staf"
        gaji_staf()

      print()
      kembali = input("Kembali ke menu? [Y/N]: ")
      if kembali == 'Y' or kembali == 'y':
        kalkulatorgaji()
      else:
        exit()
      
    else:
      print()
      print("Error: Jabatan tidak tersedia")
      print()
      False

kalkulatorgaji()
