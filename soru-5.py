# 5) Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.

pald = input("Please enter something: ")
num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
is_number = True
sign = False
if pald[0] == "-":
    sign = True
    pald = pald[1:]
for i in pald:
    if i not in num_list:
        if sign:
            pald = "-" + pald
        is_number = False
        break
if is_number:
    pald = int(pald)
    pald = abs(pald)
    pald = str(pald)

    reversed = pald[::-1]

    if reversed == pald:
        print("palindromdur")
    else:
        print("palindrom değil")
else:
    reversed = pald[::-1]

    if reversed == pald:
        print("palindromdur")
    else:
        print("palindrom değil")
