import json
import requests
import time

def continueSearch():
    continueValid = False
    global cont

    while not continueValid:
        print('Would you like to search again? [Y/N] ')
        continueAnswer = input()

        if continueAnswer.casefold() == 'y':
            cont = True
            continueValid = True
        elif continueAnswer.casefold() == 'n':
            print('Terminating... ')
            time.sleep(2)
            cont = False
            continueValid = True
        else:
            print('Invalid response. ')
            continueValid = False

cont = True

while cont:
    valid = False

    while not valid:
        print('Filter by color? [Y/N]')
        filterAnswer = input()

        if filterAnswer.casefold() == 'y':
            print('Please enter a color: ')
            color = input()
            valid = True
        elif filterAnswer.casefold() == 'n':
            print('Displaying all widgets: ')
            color = ''
            valid = True
        else:
            print('Invalid response. ')
            time.sleep(2)
            valid = False

    r = requests.get('http://localhost:3000/%s' % color)

    try:
        data = r.json()

        for i in data:
            print(i['name'], 'is', i['color'])

        time.sleep(2)
        
        continueSearch()
    except:
        print('No widgets matching', color, 'were found.')
        time.sleep(2)
        continueSearch()