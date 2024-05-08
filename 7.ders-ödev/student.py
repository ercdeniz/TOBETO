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


class Student:

    student_list = []

    def add(self, first_name, last_name, gender, number):
        for std in self.student_list:
            if std["number"] == number:
                std["name"] = first_name + " " + last_name
                std["gender"] = gender
                print(f"{YELLOW}{std['name']} updated successfully.{RES}")
                return

        name = first_name + " " + last_name
        student_info = {
            "name": name,
            "gender": gender,
            "number": number
        }
        self.student_list.append(student_info)
        print(f"{GREEN}{name} added successfully.{RES}")

    def remove(self, number):
        for index, std in enumerate(self.student_list):
            if std["number"] == number:
                removed = self.student_list.pop(index)
                print(f"{RED}Removed: {removed['name']}{RES}")
                break

    def list(self):
        if not self.student_list:
            print(f"{RED}No students registered yet.{RES}")
            return
        print(f"    {CYAN}{'Name':<18}{'Gender':<9}{'Number':<10}{RES}")
        for student in self.student_list:
            print(f"    {YELLOW}{student['name'][:15]:<16}| {student['gender'][:5]:<7}| {student['number']:<10}{RES}")
