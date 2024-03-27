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


student_list = []
class Student:
    def __init__(self,first_name, last_name, gender, number):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.number = number

    def add(self):
            name = self.first_name + " " + self.last_name
            student_info = {
                "name": name,
                "gender": self.gender,
                "number": self.number
            }
            student_list.append(student_info)
            print(f"{GREEN}{name} added successfully.{RES}")

    @staticmethod
    def remove(number):
        for index, std in enumerate(student_list):
            if std["number"] == number:
                removed = student_list.pop(index)
                print(f"{RED}Removed: {removed['name']}{RES}")
                break

    @staticmethod
    def list(student_list):
        if not student_list:
            print(f"{RED}No students registered yet.{RES}")
            return
        print(f"    {CYAN}{'Name':<18}{'Gender':<9}{'Number':<10}{RES}")
        for student in student_list:
            print(f"    {YELLOW}{student['name'][:15]:<16}| {student['gender'][:5]:<7}| {student['number']:<10}{RES}")
