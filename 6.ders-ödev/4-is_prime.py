import os # os is used for clear the screen
from colorama import Fore # Fore is used for foreground color

# Clear the screen
def clear():
    _os = os.system('cls')

# Prime number algorithm
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

clear()
print(f"{Fore.LIGHTRED_EX}!!!Usege:\n{Fore.LIGHTYELLOW_EX}  Exit command: CONTROL + C{Fore.RESET}")

while True:
    try:
        number = int(input(f"{Fore.MAGENTA}Enter a number: {Fore.RESET}"))
        if is_prime(number):
            print(f"{Fore.GREEN}{number} is a prime number.{Fore.RESET}")
        else:
            print(f"{Fore.RED}{number} is not a prime number.{Fore.RESET}")
    except ValueError as ve:
        print(f"{Fore.RED}Error: {ve}\n{Fore.YELLOW}Please enter a valid number!{Fore.RESET}")
        continue
    except KeyboardInterrupt:
        print(f"\n{Fore.BLUE}Exited by user.{Fore.RESET}")
        break