# 4)Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)

import math

r = int(input("Yarı çapı giriniz :   "))

alan = math.pi * (r*2)

print("alan: ",alan)

cevre = 2 * math.pi * r
print("çevre: ",cevre)