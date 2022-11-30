import json
import random
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
        print('')
        filterAnswer = input()

        if filterAnswer.casefold() == 'y':
            print('')
            answer = input()
            valid = True
        elif filterAnswer.casefold() == 'n':
            print('')
            answer = ''
            valid = True
        else:
            print('Invalid response. ')
            time.sleep(2)
            valid = False

    r = requests.get('http://localhost:3000/%s' % answer)

    try:
        data = r.json()

        for i in data:
            print(i['name'], 'is', i['answer'])

        time.sleep(2)
        
        continueSearch()
    except:
        print('No movies matching', answer, 'were found.')
        time.sleep(2)
        continueSearch()