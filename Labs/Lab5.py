# 1. Take a birthday date input and calculate how many seconds old you are.

import datetime

invalid = True

while invalid:
    print("What is your birth year? [YYYY]")
    year = int(input())

    print("What is your birth month? [1-12]")
    month = int(input())

    print("What day were you born? [1-31]")
    day = int(input())

    try:
        birthday = datetime.date(year, month, day)
        invalid = False
    except:
        print("Enter a valid birthday [YYYY/MM/DD]")
        invalid = True

today = datetime.date.today()
age = (today - birthday).total_seconds()
print("You are " + str(age) + " seconds old!")

