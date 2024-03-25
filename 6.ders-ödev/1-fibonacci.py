import os # os is used for clear the screen
from colorama import Fore, Style

# Clear the screen
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Fibonacci algorithm
def fibonacci(number, num1=1, num2=1):
    if number == 0:
        return
    div = ", " if number > 1 else "\n"
    print(Fore.LIGHTGREEN_EX + str(num1) + Style.RESET_ALL, end=div)
    fibonacci(number - 1, num2, num1 + num2)

clear()
print(f"{Fore.LIGHTRED_EX}!!!Usege:\n{Fore.LIGHTYELLOW_EX}\
    Enter -1 to exit. Enter -2 to clear the screen.{Style.RESET_ALL}")
while True:
    try:
        number = int(input(f"{Fore.LIGHTMAGENTA_EX}Enter a number: {Style.RESET_ALL}"))
        if number < 0:
            if number == -1:
                print(f"{Fore.LIGHTRED_EX}exit{Style.RESET_ALL}", end="")
                break
            elif number == -2:
                clear()
                continue
    except:
        print(f"{Fore.RED}Please enter a valid number!{Style.RESET_ALL}")
        continue
    fibonacci(number)
