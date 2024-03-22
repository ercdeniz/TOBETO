# 5) Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.

import os
from colorama import Fore, Style

def clear():
    if os.name == 'nt':
        _os = os.system('cls')
    else:
        _os = os.system('clear')

clear()
pald = input(Fore.MAGENTA + "Please enter something: " + Style.RESET_ALL)
num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
abc = ""
sign = False
if pald[0] == "-" or pald[0] == "+":
    abc = pald[0]
    sign = True
    pald = pald[1:]
for i in pald:
    if i not in num_list:
        if sign:
            pald = abc + pald
        break
reversed = pald[::-1]
if reversed == pald:
    print(Fore.GREEN + "palindrome" + Style.RESET_ALL)
else:
    print(Fore.RED + "not palindrome" + Style.RESET_ALL)
    print(Fore.YELLOW + "reversed: " + reversed + Style.RESET_ALL)

