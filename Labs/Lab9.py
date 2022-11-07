import json
import requests

valid = False

def continueSearch():
    continueValid = False

    while not continueValid:
        print('Would you like to search again? [Y/N] ')
        continueAnswer = input()

        if continueAnswer.casefold() == 'y':
            valid = False
            continueValid = True
        elif continueAnswer.casefold() == 'n':
            print('Terminating... ')
            valid = False
            continueValid = True
        else:
            print('Invalid response. ')
            continueValid = False

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
        valid = False

r = requests.get('http://localhost:3000/%s' % color)

try:
    data = r.json()
    print(data)
    continueSearch()
except:
    print('No widgets matching', color, 'were found.')
    continueSearch()