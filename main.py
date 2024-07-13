day = 1
month = 1
day_of_week = 1 #1-7 representing mon-sun
year = 1900
num_of_sundays = 0

def last_day_of_month(day, month, year):
    thirty_days = [4, 6, 9, 11]
    if month in thirty_days:
        if day == 30:
            return True
        else:
            return False
    elif month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            if day == 29:
                return True
            else:
                return False
        else:
            if day == 28:
                return True
            else:
                return False
    elif day == 31:
        return True
    else:
        return False

def change_day_of_week(day_of_week):
    if day_of_week == 7:
        day_of_week = 1
    else:
        day_of_week = day_of_week + 1
    return day_of_week

while year < 2001:
    if month == 12 and day == 31:
        year = year + 1
        day = 1
        month = 1
    elif last_day_of_month(day, month, year) is True:
        month = month + 1
        day = 1
    else:
        day = day + 1

    day_of_week = change_day_of_week(day_of_week)
    if day_of_week == 7 and day == 1 and year > 1900:
        num_of_sundays = num_of_sundays + 1
    print(day, day_of_week)
print(num_of_sundays)
