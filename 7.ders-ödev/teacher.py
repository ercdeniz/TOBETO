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


class Teacher:
    
    teacher_list = []

    def add(self, first_name, last_name, gender, branch):
            name = first_name + " " + last_name
            teacher_info = {
                "name": name,
                "gender": gender,
                "branch": branch
            }
            self.teacher_list.append(teacher_info)
            print(f"{GREEN}{name} added successfully.{RES}")

    def remove(self, name):
        for index, std in enumerate(self.teacher_list):
            if std["name"] == name:
                removed = self.teacher_list.pop(index)
                print(f"{RED}Removed: {removed['name']}{RES}")
                break

    def list(self, teacher_list):
        if not teacher_list:
            print(f"{RED}No teachers registered yet.{RES}")
            return
        print(f"    {CYAN}{'Name':<18}{'Gender':<9}{'Branch':<10}{RES}")
        for teacher in teacher_list:
            print(f"    {YELLOW}{teacher['name'][:15]:<16}| {teacher['gender'][:5]:<7}| {teacher['branch']:<10}{RES}")
