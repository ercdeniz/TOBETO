# 2) Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.

ham_maas = int(input("Maaşınızı girin: "))
zam_orani = float(input("Zam oranını girin (1 ile 100 arası bir sayı giriniz.): "))

if (zam_orani == 0):
    print("oran sıfır olamaz!!!")
elif(zam_orani < 1 or zam_orani >= 100):
    print("Geçersiz zam oranı girdiniz.")

zamli_maas = ham_maas + (ham_maas * (zam_orani / 100))

print("Zamlı maaşınız: ", zamli_maas)
is_fakir = (zamli_maas-ham_maas)
if is_fakir < 100:
    print("sen de fakirsin kardeşim")
elif is_fakir < 200:
    print("eh işte")
elif is_fakir < 300:
    print("iyisin yine")