
import os # os is used for clear the screen
from colorama import Fore # Fore is used for foreground color
CYAN = Fore.CYAN
LCYAN = Fore.LIGHTCYAN_EX
RED = Fore.RED
LRED = Fore.LIGHTRED_EX
MAGENTA = Fore.MAGENTA
LMAGENTA = Fore.LIGHTMAGENTA_EX
YELLOW = Fore.YELLOW
LYELLOW = Fore.LIGHTYELLOW_EX
BLUE = Fore.BLUE
LBLUE= Fore.LIGHTBLUE_EX
GREEN = Fore.GREEN
LGREEN = Fore.LIGHTGREEN_EX
RES = Fore.RESET

# Clear the screen
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

import student
import teacher

def commands_info(raw_cmd , flag):
    if flag:
        print(f"{YELLOW}Commands '{raw_cmd}' not faund.{RES}")
    print(f"""{LBLUE}Commands:
    {CYAN}add{RES}    - Add a student
    {CYAN}remove{RES} - Remove a student
    {CYAN}list{RES}   - List students
    {CYAN}clear{RES}  - Clear the screen
    {CYAN}exit{RES}   - Exit the program""")

clear()
commands_info("", False)
while True:
    try:
        raw_cmd = input(f"{LMAGENTA}> {RES}")
        cmd = raw_cmd.strip().lower()
        if not cmd:
            continue
        elif cmd == "exit":
            print(f"{RED}Exited by user.{RES}")
            break

        elif cmd == "clear":
            clear()

        elif cmd == "add":
            choice = input(f"{LBLUE}\t\b\bAdd a student or teacher? (s/t): {RES}").strip().lower()
            if choice == "s":
                First_name = input(f"{MAGENTA}\tFirst name: {RES}")
                Last_name = input(f"{MAGENTA}\tLast name: {RES}")
                Gender = input(f"{MAGENTA}\tGender: {RES}")
                Number = int(input(f"{MAGENTA}\tNumber(int): {RES}"))
                _student = student.Student(First_name, Last_name, Gender, Number)
                _student.add()
            elif choice == "t":
                First_name = input(f"{MAGENTA}\tFirst name: {RES}")
                Last_name = input(f"{MAGENTA}\tLast name: {RES}")
                Gender = input(f"{MAGENTA}\tGender: {RES}")
                Branch = input(f"{MAGENTA}\tBranch: {RES}")
                _teacher = teacher.Teacher(First_name, Last_name, Gender, Branch)
                _teacher.add()
            else:
                print(f"{RED}Invalid choice.{RES}")

        elif cmd == "remove":
            choice = input(f"{LBLUE}\t\b\bAdd a student or teacher? (s/t): {RES}").strip().lower()
            if choice == "s":
                Number = int(input(f"{MAGENTA}\tStudent number(int): {RES}"))
                student.Student.remove(Number)
            elif choice == "t":
                First_name = input(f"{MAGENTA}\tFirst_name: {RES}")
                Last_name = input(f"{MAGENTA}\tLast_name: {RES}")
                teacher.Teacher.remove(First_name + " " + Last_name)
            else:
                print(f"{RED}Invalid choice.{RES}")

        elif cmd == "list":
            choice = input(f"{LBLUE}\t\b\bList students or teachers? (s/t): {RES}").strip().lower()
            if choice == "s":
                student.Student.list(student.student_list)
            elif choice == "t":
                teacher.Teacher.list(teacher.teacher_list)
            else:
                print(f"{RED}Invalid choice.{RES}")

        else:
            commands_info(raw_cmd, True)
    except Exception as e:
        print(f"{RED}Error: {e}{RES}")
    except KeyboardInterrupt:
        print(f"\n{RED}Exited by user.{RES}")
        break