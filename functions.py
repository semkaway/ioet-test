from datetime import datetime, timedelta

def getDateTime(time):
    return datetime.strptime(time,'%H:%M')

def countWageForEmployee(employee, hours):
    try:
        name = employee.split("=")[0]
        wage = 0
        daysAndHours = employee.split("=")[1].split(",")
        for day in daysAndHours:
            dayAtWork = day[0:2]
            hoursAtWork = day[2:].split("-")
            startWorking = getDateTime(hoursAtWork[0])
            finishWorking = getDateTime(hoursAtWork[1])
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
        return "The amount to pay %s is: %d USD" % (name, wage)
    except:
        return "THERE WAS A FORMATTING ERROR IN THE FILE ON THIS LINE"
