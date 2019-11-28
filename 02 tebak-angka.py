while True:
    tebak_angka = int(input("Silahkan masukkan angka: "))
    if tebak_angka == 7:
        print("Horee jawaban benar!")
        main_lagi = input("Mau main lagi?")
        if main_lagi != "y":
            print("sampai ketemu lagi ya..")
            break
    
    else:
        print("Yahhh jawaban salah, ayo coba lagi..")
