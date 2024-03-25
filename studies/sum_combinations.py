import os # os is used for clear the screen
from colorama import Fore # Fore is used for foreground color

# Clear the screen
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
# Find the sum of two numbers in the array that is equal to the given integer
def sum_find(array, integer):
    answer = []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == integer:
                indexs = (i, j)
                nums = (array[i], array[j])
                answer.append({"indexs": indexs, "numbers": nums})
                return answer
    return answer

clear()
while True:
    try:
        multi_input = input(f"{Fore.MAGENTA}Enter the integer array (space-separated): {Fore.RESET}")
        array = list(map(int, multi_input.split()))
        integer = int(input(f"{Fore.MAGENTA}Enter an integer: {Fore.RESET}"))
        answer = sum_find(array, integer)
        if answer:
            print(f"{Fore.GREEN}Match not found! Answer:")
            for item in answer:
                print("indexs:", ", ".join(map(str, item["indexs"])))
                print("numbers:", ", ".join(map(str, item["numbers"])) + Fore.RESET)
        else:
            print(f"{Fore.RED}Match not found.{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Fore.RESET}")
        continue
    except KeyboardInterrupt:
        print(f"{Fore.RED}\nExited by user.{Fore.RESET}")
        break
