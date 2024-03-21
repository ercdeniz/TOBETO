# 1) Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.
boy = float(input("Boyunuzu girin: "))
kilo = int(input("Kilonuzu girin: "))
if kilo > 90:
    print("Dün kaç ramazan pidesi gömdün?")
vki = kilo/(boy * boy)

if vki < 18.5:
    print("Zayıf", vki)
elif vki >= 18.5 and vki < 25:
    print("Normal", vki)
elif vki >= 25 and vki < 30:
    print("Fazla Kilolu", vki)
elif vki >= 30:
    print("Canan Karatay kalp krizi geçirdi!")