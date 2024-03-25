import os # os is used for clear the screen
from colorama import Fore # Fore is used for foreground color

# Clear the screen
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# GCD algorithm: EBOB - Greatest Common Divisor
def EBOB(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1

# LCM algorithm: EKOK - Least Common Multiple
def EKOK(num1, num2):
    return num1 * num2 // EBOB(num1, num2) # (//) operator is used to get integer division

clear()
print(f"{Fore.LIGHTRED_EX}!!!Usege:\n{Fore.LIGHTYELLOW_EX}  Exit command: CONTROL + C{Fore.RESET}")
while True:
    try:
        num1 = int(input(f"{Fore.MAGENTA}Enter a number-1: {Fore.RESET}"))
        num2 = int(input(f"{Fore.MAGENTA}Enter a number-2: {Fore.RESET}"))
        clear()
        print(f"{Fore.GREEN}Numbers: {num1}, {num2}")
        print(f"{Fore.LIGHTGREEN_EX}EBOB: {EBOB(num1, num2)}")
        print(f"{Fore.LIGHTGREEN_EX}EKOK: {EKOK(num1, num2)}")
    except ValueError as ve:
        print(f"{Fore.RED}Error: {ve}\n{Fore.YELLOW}Please enter a valid number!{Fore.RESET}")
        continue
    except KeyboardInterrupt:
        print(f"\n{Fore.BLUE}Exited by user.{Fore.RESET}")
        break