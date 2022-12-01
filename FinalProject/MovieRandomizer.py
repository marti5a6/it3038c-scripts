import json
import random
import requests
import time
import os

# Found on StackOverflow - Create a class for terminal output colors
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# Create function to restart while loop if user says yes
def continueSearch():
    # Default valid response boolean to False, instantiate global continue variable
    continueValid = False
    global cont

    # Loop while the response is invalid
    while not continueValid:
        print('Would you like to search again? ' + color.GREEN + color.BOLD + '[Y/N]' + color.END)
        continueAnswer = input()

        # If user enters y, continue operation
        if continueAnswer.casefold() == 'y':
            cont = True
            continueValid = True

        # If user enters n, exit operation
        elif continueAnswer.casefold() == 'n':
            print(color.RED + color.BOLD + 'Exiting... ' + color.END)
            time.sleep(2)
            cont = False
            continueValid = True

        # If user enters anything else, restart loop
        else:
            print(color.YELLOW + color.BOLD + 'Invalid response. ' + color.END)
            continueValid = False

# Default valid boolean to False
valid = False

# Loop while valid boolean is False
while not valid:

    # Determine window size for print formatting
    columns, rows = os.get_terminal_size()

    # Formatted terminal response
    print('=' * columns)
    print("-" * int(columns/2-19) + color.GREEN + color.BOLD + " Press 'enter' to get a random Movie! " + color.END + "-" * int(columns/2-19))
    print("-" * int(columns/2-12) + color.RED + color.BOLD + " Or type quit to exit. " + color.END + "-" * int(columns/2-11))
    print('=' * columns)

    beginAnswer = input()

    # If user presses enter, return random movie
    if beginAnswer.casefold() == '':
        valid = True

        # Default continue boolean to True
        cont = True

        # Loop while continue boolean is True
        while cont:
        
            # Logic for randomizing a movie object
            try:
                # Request and store JSON data
                r = requests.get('http://localhost:3000/api')
                data = r.json()

                # Select random movie from JSON
                randomMovie = random.choice(data)

                # Determine window size for print formatting
                columns, rows = os.get_terminal_size()

                # Formatted Terminal Response
                print('=' * columns)

                print(color.RED + color.BOLD + 'Title: ' + color.END + randomMovie['Series_Title'] 
                + ' | ' + color.RED + color.BOLD + 'Released: ' + color.END + str(randomMovie['Released_Year']))

                print(color.GREEN + color.BOLD + 'Description: ' + color.END + randomMovie['Overview'])
                
                print(color.BLUE + color.BOLD + 'Length: ' + color.END + str(randomMovie['Runtime']) 
                + ' | ' + color.BLUE + color.BOLD + 'Genre: ' + color.END + randomMovie['Genre'] 
                + ' | ' + color.BLUE + color.BOLD + 'Rating: ' + color.END + str(randomMovie['IMDB_Rating']))

                print('=' * columns)

                # Wait and ask if the user wants to continue
                time.sleep(2)
                continueSearch()
            except:
                # Catch error with API, allow user to continue anyway [RESTART API.JS IF YOU GET THIS ERROR]
                print(color.YELLOW + color.BOLD + 'Error, API is offline...' + color.END)
                time.sleep(2)
                continueSearch()

    # If user enters quit or exit, end the script
    elif beginAnswer.casefold() == 'quit':
        print(color.RED + color.BOLD + 'Exiting...' + color.END)
        time.sleep(1)
        valid = True
    elif beginAnswer.casefold() == 'exit':
        print(color.RED + color.BOLD + 'Exiting...' + color.END)
        time.sleep(1)
        valid = True

    # If user enters anything else, restart loop
    else:
        print(color.YELLOW + color.BOLD + 'Invalid response...' + color.END)
        time.sleep(1)
        valid = False