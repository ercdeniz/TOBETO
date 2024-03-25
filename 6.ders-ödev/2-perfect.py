import os # os is used for clear the screen
from colorama import Fore

# Clear the screen
def clear():
    os.system('cls')

# Find the perfect number
def findPerfectNumber(number):
    total = 0
    for i in range(1,number):
        if number % i == 0:
            total += i
    if total == number:
        print(f"{Fore.GREEN}it's a perfect number{Fore.RESET}")
    else:
        print(f"{Fore.RED}it's not a perfect number{Fore.RESET}")

clear()
print(f"{Fore.LIGHTRED_EX}!!!Usege:\n{Fore.LIGHTYELLOW_EX}\
    Enter -1 to exit. Enter -2 to clear the screen.{Fore.RESET}")
while True:
    try:
        number = int(input(f"{Fore.MAGENTA}Enter a number: {Fore.RESET}"))
        findPerfectNumber(number)
        if number < 0:
            if number == -1:
                print(f"{Fore.LIGHTRED_EX}exit{Fore.RESET}", end="")
                break
            elif number == -2:
                clear()
                continue
    except:
        print(f"{Fore.RED}Please enter a valid number!{Fore.RESET}")
        continue