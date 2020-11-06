import os, platform, sys
from time import sleep

path = os.getcwd()
extend = os.sep
merge = path+extend

def updown(msg):
    msg = msg.lower()
    temp = 0
    for harf in msg:
        if temp % 2 == 0:
            print(harf.lower(), end="")
        else:
            print(harf.upper(), end="")
        temp += 1

def upAndSpace(msg):
    msg = str(msg).upper()
    for char in msg:
        print(char, end=" ")

def lowAndSpace(msg):
    msg = str(msg).lower()
    for char in msg:
        print(char, end=" ")

def writeEffect(msg):
    waitTime = 0.1
    for char in msg:
        print(char, end="")
        sleep(waitTime)

def onlyFirstCharUpped(msg):
    msg = str(msg)
    messages = list(msg.split(" "))
    for message in messages:
        messg = message[0].upper()
        printable_message = messg+message[1:]
        print(printable_message, end=" ")

def onlyFirstCharLowed(msg):
    msg = str(msg).upper()
    messages = list(msg.split(" "))
    for message in messages:
        messg = message[0].lower()
        printable_message = messg + message[1:]
        print(printable_message, end=" ")

def reverse(msg):
    msg = str(msg)
    print(msg[::-1])

def par(num, msg):
    print(f"[ {num} ] {msg}")

def error(msg):
    print(f"[!] {msg}")

def success(msg):
    print(f"[+] {msg}")

def status(msg):
    print(f"[*] {msg}")

def banner():
    ban = """
           █████▒▒█████   █    ██  ██▀███      ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀▓█████  ██▀███  ▒███████▒
         ▓██   ▒▒██▒  ██▒ ██  ▓██▒▓██ ▒ ██▒   ▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒▒ ▒ ▒ ▄▀░
         ▒████ ░▒██░  ██▒▓██  ▒██░▓██ ░▄█ ▒   ▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒░ ▒ ▄▀▒░ 
         ░▓█▒  ░▒██   ██░▓▓█  ░██░▒██▀▀█▄     ░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄    ▄▀▒   ░
         ░▒█░   ░ ████▓▒░▒▒█████▓ ░██▓ ▒██▒   ░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒▒███████▒
          ▒ ░   ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░    ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░░▒▒ ▓░▒░▒
          ░       ░ ▒ ▒░ ░░▒░ ░ ░   ░▒ ░ ▒░    ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░░░▒ ▒ ░ ▒
          ░ ░   ░ ░ ░ ▒   ░░░ ░ ░   ░░   ░     ░  ░░ ░  ░   ▒   ░        ░ ░░ ░    ░     ░░   ░ ░ ░ ░ ░ ░
                    ░ ░     ░        ░         ░  ░  ░      ░  ░░ ░      ░  ░      ░  ░   ░       ░ ░    
                                                                ░                               ░        

                                @@@   @@@       @@@@@@@   @@@@@@   @@@@@@@   
                               @@@@   @@@       @@@@@@@@  @@@@@@@  @@@@@@@@  
                              @@!@!   @@!       @@!  @@@      @@@  @@!  @@@  
                             !@!!@!   !@!       !@!  @!@      @!@  !@!  @!@  
                            @!! @!!   @!!       @!@@!@!   @!@!!@   @!@!!@!   
                           !!!  !@!   !!!       !!@!!!    !!@!@!   !!@!@!    
                           :!!:!:!!:  !!:       !!:           !!:  !!: :!!   
                           !:::!!:::   :!:      :!:           :!:  :!:  !:!  
                                :::    :: ::::   ::       :: ::::  ::   :::  
                                :::   : :: : :   :         : : :    :   : :  
    """
    return ban

if str(platform.system()).lower().startswith("win"):
    clear = lambda : os.system("cls")
else:
    clear = lambda : os.system("clear")

def main(msg):
    msg = str(msg)
    print(banner())

    par(1, "Büyük Küçük Efekti")
    par(2, "Her Harf Büyük ve Ayrı")
    par(3, "Her Harf Küçük ve Ayrı")
    par(4, "Yazma Efekti")
    par(5, "Cümlenin Her Kelimesinin Sadece Baş Harfi Büyük")
    par(6, "Cümlenin Her Kelimesinin Sadece Baş Harfi Küçük")
    par(7, "Verilen Mesajın Tersten Yazımı")

    print(" ")

    try:
        choice = int(input("[?] Seçenek: "))
    except:
        error("Lütfen Bir Sayı Girin.")
        sleep(0.7)
        status("Program sonlandırılıyor...")
        sleep(2)
        sys.exit()

    if choice == 1:
        clear()
        print(" ")
        updown(msg)
        print("\n")

    elif choice == 2:
        clear()
        print(" ")
        upAndSpace(msg)
        print("\n")

    elif choice == 3:
        clear()
        print(" ")
        lowAndSpace(msg)
        print("\n")

    elif choice == 4:
        clear()
        print(" ")
        writeEffect(msg)
        print("\n")

    elif choice == 5:
        clear()
        print(" ")
        onlyFirstCharUpped(msg)
        print("\n")

    elif choice == 6:
        clear()
        print(" ")
        onlyFirstCharLowed(msg)
        print("\n")

    elif choice == 7:
        clear()
        print(" ")
        reverse(msg)
        print("\n")

    else:
        error("Lütfen Geçerli Bir Seçenek Seçin.")
        sleep(0.7)
        status("Program sonlandırılıyor...")
        sleep(2)
        sys.exit()

soru = input("[?] Çevirilecek Unsur Bir Dosyadan mı okunacak? [E/h]: ")

if str(soru).lower().startswith("e"):
    filename = input("[?] Dosya Adı: ")
    f = str(merge + filename)
    try:
        with open(f, "r", encoding="utf-8") as file:
            icerik = file.read()
        main(icerik)
    except FileNotFoundError:
        try:
            with open(f+".txt", "r", encoding="utf-8") as file:
                icerik = file.read()
            main(icerik)
        except FileNotFoundError:
            error(f"{filename} adında bir dosya bulunamadı lütfen dosyalarınızı kontrol edip tekrar deneyin...")
            sleep(5)
            status("Program sonlandırılıyor...")
            sleep(1)
            sys.exit()

elif str(soru).lower().startswith("h"):
    msg = str(input("[?] Mesaj: "))
    main(msg=msg)

else:
    error("Lütfen 'Evet' yada 'Hayır' yazın.")
    sleep(0.7)
    status("Program sonlandırılıyor...")
    sleep(2)
    sys.exit()