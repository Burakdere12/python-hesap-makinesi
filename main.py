print("""
Hesap Makinesi
 Toplama İşlemi Yapmak İçin + `Ya Basınız
 Cıkarma İşlemi Yapmak İçin - `Ye Basınız
 Çarpma İşlemi Yapmak İçin ×`Ya Basınız
 Bölme İşlemi Yapmak İçin ÷ `Ye Basınız

""")

islem = str(input("İşlem Seçiniz: "))

if islem == "+":
    sayi1 = int(input("sayi1 giriniz: "))
    sayi2 = int(input("sayi2 giriniz: "))
    print("Sonuç:", sayi1 + sayi2)
elif islem == "-":
    sayi1 = int(input("sayi1 giriniz: "))
    sayi2 = int(input("sayi2 giriniz: "))
    print("Sonuç:", sayi1 - sayi2)
elif islem == "x":
    sayi1 = int(input("sayi1 giriniz: "))
    sayi2 = int(input("sayi2 giriniz: "))
    print("Sonuç:", sayi1 * sayi2)
elif islem == "÷":
    sayi1 = int(input("sayi1 giriniz: "))
    sayi2 = int(input("sayi2 giriniz: "))
    print("Sonuç:", sayi1/sayi2)
else:
    print("İşlem Gecersiz")


