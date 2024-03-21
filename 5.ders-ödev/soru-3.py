# 3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.

sayi1 = int(input("1. Sayıyı Giriniz: "))
sayi2 = int(input("2. Sayıyı Giriniz: "))
sayi3 = int(input("3. Sayıyı Giriniz: "))

enBuyuk = None

if sayi1 > sayi2 and sayi1 > sayi3:
    enBuyuk = sayi1
    print("en büyük sayı : ",enBuyuk)
elif sayi2 > sayi1 and sayi2 > sayi3:
    enBuyuk = sayi2
    print("en büyük sayı : ",enBuyuk)
elif sayi3 > sayi1 and sayi3 > sayi2:
    enBuyuk = sayi3
    print("en büyük sayı : ",enBuyuk)
else:
    print("Lütfen farklı sayılar giriniz")