import math

def topla(a,b):
    return a + b


def cikar(a,b):
    return a - b


def carpma(a,b):
    return a * b


def bolme(a, b):                        #AI
    if b == 0:
        return "0 ile bölme yapamazsın"
    return a / b


def usalma(a,b):
    return a ** b


def karekok(a):
    return math.sqrt(a)


def mutlakdeger(a):     #AI
    if a < 0:
        return -a
    return a


def modalma(a,b):
    return a % b


def ortalama(a, b):            #AI
    return (a + b) / 2


def enbuyuk(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return "İki sayıda eşit"





while True:
    print("""\n--- ULTRA MEGA DELUXE HESAP MAKİNESİ----
    1- Toplama
    2- Çıkarma
    3- Çarpma
    4- Bölme
    5- Üs alma
    6- Karekök
    7- Mutlak değer
    8- Mod alma
    9- Ortalama (2 sayı)
    10- En büyük (2 sayı)
    11- Çıkış""")


    secim = input("Seçiminiz(1-11): ")


    if secim == "1":

        toplamasayi1 = int(input("1. Sayı: "))
        toplamasayi2 = int(input("2. Sayı: "))
        sonuc = topla(toplamasayi1, toplamasayi2)
        print("Sonuç:", sonuc)


    elif secim == "2":

        cikarmasayi1 = int(input("1. Sayı: "))
        cikarmasayi2 = int(input("2. Sayı: "))
        sonuc = cikar(cikarmasayi1, cikarmasayi2)
        print("Sonuç:", sonuc)


    elif secim == "3":

        carpmasayi1 = int(input("1. Sayı: "))
        carpmasayi2 = int(input("2. Sayı: "))
        sonuc = carpma(carpmasayi1, carpmasayi2)
        print("Sonuç:", sonuc)


    elif secim == "4":

        bolmesayi1 = int(input("1. Sayı: "))
        bolmesayi2 = int(input("2. Sayı: "))
        sonuc = bolme(bolmesayi1, bolmesayi2)
        print("Sonuç:", sonuc)


    elif secim == "5":

        ussayi1 = int(input("1. Sayı: "))
        ussayi2 = int(input("2. Sayı: "))
        sonuc = usalma(ussayi1, ussayi2)
        print("Sonuç:", sonuc)


    elif secim == "6":

        karekoksayi1 = int(input("Sayıyı Girin: "))
        sonuc = karekok(karekoksayi1)
        print("Sonuç:", sonuc)


    elif secim == "7":

        mutlakdegersayi1 = int(input("Sayıyı Girin: "))
        sonuc = mutlakdeger(mutlakdegersayi1)
        print("Sonuç:", sonuc)


    elif secim == "8":

        modalsayi1 = int(input("1. Sayıyı Girin: "))
        modalsayi2 = int(input("2. Sayıyı Girin: "))
        sonuc = modalma(modalsayi1, modalsayi2)
        print("Sonuç:", sonuc)


    elif secim == "9":

        ortalamasayi1 = int(input("1. Sayıyı Girin: "))
        ortalamasayi2 = int(input("2. Sayıyı Girin: "))
        sonuc = ortalama(ortalamasayi1, ortalamasayi2)
        print("Sonuç:", sonuc)


    elif secim == "10":

        enbuyuksayi1 = int(input("1. Sayıyı Girin: "))
        enbuyuksayi2 = int(input("2. Sayıyı Girin: "))
        sonuc = enbuyuk(enbuyuksayi1, enbuyuksayi2)
        print("Sonuç:", sonuc)


    elif secim == "11":

        cikis = input("""\n--- ULTRA MEGA DELUXE HESAP MAKİNESİ'den
        Çıkmak istediğine emin misin(Evet, Hayır): """)
        if cikis == "Evet":
            print("Bye Bye...")
            break


    else:
        print("Yanlış rakam girdiniz lütfen 1 ile 11 arasında bir sayı giriniz")