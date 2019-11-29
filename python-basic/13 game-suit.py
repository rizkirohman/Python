import random

print()
print("Gunting, Batu, Kertas!")
print()
print("Pilihan: ")
print()
print("1. Gunting")
print("2. Batu")
print("3. Kertas")
print()

def permainan():
  def mainlagi():
    main_lagi = input("Main lagi? [Y/N]: ")
    if (main_lagi == 'Y') or (main_lagi == 'y'):
      permainan()
    else:
      print()
      print("Good Bye!")
      exit()

  print()
  player = int(input("Pilihanmu [1/2/3]: "))
  comp = random.choice(["Gunting", "Batu", "Kertas"])
  if player == 1:
    print("Kamu \t\t: Gunting")
    print(f"Komputer \t: {comp}")
    if comp == "Gunting":
      print("Hasil \t\t: Hmm Draw..")
      print()
      mainlagi()
      print()
    elif comp == "Batu":
      print("Hasil \t\t: Yaah Kalah :(")
      print()
      mainlagi()
      print()
    elif comp == "Kertas":
      print("Hasil \t\t: Yess Menang!")
      print()
      mainlagi()
      print()
      
  elif player == 2:
    print("Kamu \t\t: Batu")
    print(f"Komputer \t: {comp}")
    if comp == "Gunting":
      print("Hasil \t\t: Yess Menang!")
      print()
      mainlagi()
      print()
    elif comp == "Batu":
      print("Hasil \t\t: Hmm Draw..")
      print()
      mainlagi()
      print()
    elif comp == "Kertas":
      print("Hasil \t\t: Yaah Kalah :(")
      print()
      mainlagi()
      print()

  elif player == 3:
    print("Kamu \t\t: Kertas")
    print(f"Komputer \t: {comp}")
    if comp == "Gunting":
      print("Hasil \t\t: Yahh Kalah :(")
      print()
      mainlagi()
      print()
    elif comp == "Batu":
      print("Hasil \t\t: Yess Menang!")
      print()
      mainlagi()
      print()
    elif comp == "Kertas":
      print("Hasil \t\t: Hmm Draw..")
      print()
      mainlagi()
      print()
      
  elif player >= 4:
    print("Pilihan tidak tersedia")
    print()
    mainlagi()
    print()

permainan()
