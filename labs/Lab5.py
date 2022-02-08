# Take a birthday date input and calculate how many seconds old you are

import datetime

invalid = True

while invalid:
    print('What year were you born?')
    year = int(input())

    print('What month were you born? (1-12)')
    month = int(input())

    print('What day were you born? (1-31)')
    day = int(input())

    try:
        birthday = datetime.date(year, month, day)
        invalid = False
    except:
        print('Enter a valid birthday.')
        invalid = True

today = datetime.date.today()
age = (today - birthday).total_seconds()
print('You are ' + str(age) + ' seconds old!')

