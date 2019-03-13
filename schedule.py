import sys
from datetime import datetime, timedelta

content = []
hours = [{"start": datetime.strptime('00:01','%H:%M'), "end": datetime.strptime('09:00','%H:%M'), "wage":"25"},
        {"start": datetime.strptime('09:01','%H:%M'), "end": datetime.strptime('18:00','%H:%M'), "wage":"15"},
        {"start": datetime.strptime('18:01','%H:%M'), "end": datetime.strptime('23:59','%H:%M'), "wage":"20"}]

if len(sys.argv) < 2:
    print("Please, enter the name of the file.")
elif len(sys.argv) > 2:
    print("There can be only one file.")
else:
    if sys.argv[1].lower().endswith('.txt'):
        try:
            file = open(sys.argv[1], "r")
            for line in file:
                content.extend([line.replace('\n', '')])
            for employee in content:
                try:
                    name = employee.split("=")[0]
                    wage = 0
                    daysAndHours = employee.split("=")[1].split(",")
                    for day in daysAndHours:
                        dayAtWork = day[0:2]
                        hoursAtWork = day[2:].split("-")
                        startWorking = datetime.strptime(hoursAtWork[0],'%H:%M')
                        finishWorking = datetime.strptime(hoursAtWork[1],'%H:%M')
                        totalHours = int(((finishWorking - startWorking).seconds)/3600)
                        startWorking += timedelta(minutes=1)
                        initialStartWorking = startWorking
                        while totalHours > 0:
                            for period in hours:
                                if startWorking.time() >= period["start"].time() and startWorking.time() <= period["end"].time():
                                    if initialStartWorking.date() < startWorking.date() and dayAtWork == "SU":
                                        dayAtWork = "MO"
                                    if initialStartWorking.date() < startWorking.date() and dayAtWork == "FR":
                                        dayAtWork = "SA"
                                    if dayAtWork == "SA" or dayAtWork == "SU":
                                        wage += int(period["wage"]) + 5
                                    else:
                                        wage += int(period["wage"])
                            startWorking += timedelta(hours=1)
                            totalHours -= 1
                    print("The amount to pay %s is: %d USD" % (name, wage))
                except:
                    print("THERE WAS AN ERROR IN THE FILE ON THIS LINE")
            file.close()
        except:
            print("Please, enter the correct name of the file.")
    else:
        print("The file extention must be '.txt'")
