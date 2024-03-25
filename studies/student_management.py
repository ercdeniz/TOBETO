import os # os is used for clear the screen
from colorama import Fore # Fore is used for foreground color

# Clear the screen
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Add a student
def add(students):
    name = input(f"{Fore.LIGHTBLUE_EX}   Enter student name: {Fore.RESET}")
    surname = input(f"{Fore.LIGHTBLUE_EX}   Enter student surname: {Fore.RESET}")
    if not name or not surname:
        print(f"{Fore.RED}Name and surname cannot be empty.\nADD FAILED{Fore.RESET}")
        return
    studend = {"name": name, "surname": surname}
    students.append(studend)
    print(f"{Fore.GREEN}{name} {surname} added successfully.{Fore.RESET}")

# Remove a student
def remove(students, index):
    if index < 0 or index >= len(students):
        print(f"{Fore.RED}Student not found.{Fore.RESET}")
        return
    name_surname = f"{students[index].get('name')} {students[index].get('surname')}"
    students.pop(index)
    print(f"{Fore.GREEN}{name_surname} removed successfully.{Fore.RESET}")

# List students
def list(students):
    if not students:
        print(f"{Fore.RED}No students registered yet.{Fore.RESET}")
        return
    print(f"    {Fore.CYAN}{'ID':<3}{'Name':<12}{'Surname':<10}{Fore.RESET}")
    for index, student in enumerate(students):
        print(f"    {Fore.CYAN}{index + 1:<3}{Fore.YELLOW}{student['name'][:10]:<12}{student['surname'][:10]:<10}{Fore.RESET}")

# Get a student by ID
def get_student(students, index):
    if index < 0 or index >= len(students):
        print(f"{Fore.RED}Student not found.{Fore.RESET}")
        return
    print(f"{Fore.CYAN}Student id: {index + 1}\nName: {students[index].get('name')}")
    print(f"Surname: {students[index].get('surname')}{Fore.RESET}")

# Commands info
def commands_info(raw_cmd , flag):
    if flag:
        print(f"{Fore.YELLOW}Commands '{raw_cmd}' not faund.{Fore.RESET}")
    print(f"""{Fore.LIGHTBLUE_EX}Commands:
    {Fore.CYAN}add{Fore.RESET}    - Add a student
    {Fore.CYAN}remove{Fore.RESET} - Remove a student
    {Fore.CYAN}list{Fore.RESET}   - List students
    {Fore.CYAN}get{Fore.RESET}    - Get a student by ID
    {Fore.CYAN}clear{Fore.RESET}  - Clear the screen
    {Fore.CYAN}exit{Fore.RESET}   - Exit the program""")

clear()
students = []
commands_info("", False)
while True:
    try:
        raw_cmd = input(f"{Fore.MAGENTA}> {Fore.RESET}")
        cmd = raw_cmd.strip().lower()
        if not cmd:
            continue
        elif cmd == "exit":
            print(f"{Fore.RED}Exited by user.{Fore.RESET}")
            break
        elif cmd == "clear":
            clear()
        elif cmd == "add":
            add(students)
        elif cmd == "remove":
            list(students)
            remove(students, int(input(f"{Fore.LIGHTBLUE_EX}  Enter student ID to remove: {Fore.RESET}")) - 1)
        elif cmd == "list":
            list(students)
        elif cmd == "get":
            list(students)
            get_student(students, int(input(f"{Fore.LIGHTBLUE_EX}  Enter student ID to get: {Fore.RESET}")) - 1)
        else:
            commands_info(raw_cmd, True)
    except Exception as e:
        print(f"{Fore.RED}Error: {e}{Fore.RESET}")
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Exited by user.{Fore.RESET}")
        break