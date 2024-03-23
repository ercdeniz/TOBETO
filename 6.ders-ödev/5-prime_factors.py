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

# Prime factors algorithm
def prime_factors(number):
    if number < 2:
        return False
    for i in range(1, number):
        if number % i == 0:
            print(",", i, end="") if i != 1 else print(i, end="")
    print(",", number) if is_prime(number) else print()

clear()
print(f"{Fore.LIGHTRED_EX}!!!Usege:\n{Fore.LIGHTYELLOW_EX}  Exit command: CONTROL + C{Fore.RESET}")

while True:
    try:
        number = int(input(f"{Fore.MAGENTA}Enter a number: {Fore.RESET}"))
        if number < 0:
            print(f"{Fore.LIGHTRED_EX}Enter a positive number{Fore.RESET}")
            continue
        print(f"{Fore.LIGHTYELLOW_EX}Prime factors of {number}: {Fore.LIGHTBLUE_EX}", end="")
        prime_factors(number)
    except ValueError as ve:
        print(f"{Fore.RED}Error: {ve}\n{Fore.YELLOW}Please enter a valid number!{Fore.RESET}")
        continue
    except KeyboardInterrupt:
        print(f"\n{Fore.BLUE}Exited by user.{Fore.RESET}")
        break