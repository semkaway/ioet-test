import sys
from functions import countWageForEmployee, getDateTime

hours = [{"start": getDateTime('00:01'), "end": getDateTime('09:00'), "wage":"25"},
        {"start": getDateTime('09:01'), "end": getDateTime('18:00'), "wage":"15"},
        {"start": getDateTime('18:01'), "end": getDateTime('23:59'), "wage":"20"}]

def workWithFile(filename):
    if filename.lower().endswith('.txt'):
        try:
            file = open(filename, "r")
            content = []
            for line in file:
                content.extend([line.replace('\n', '')])
            for employee in content:
                print(countWageForEmployee(employee, hours))
            file.close()
            return "OK"
        except:
            print("Please, enter the correct name of the file.")
            return "Incorrect filename"
    else:
        print("The file extention must be '.txt'")
        return "incorrect file extention"

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please, enter the name of the file.")
    elif len(sys.argv) > 2:
        print("There can be only one file.")
    else:
        workWithFile(sys.argv[1])
