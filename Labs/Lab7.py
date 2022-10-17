from bs4 import BeautifulSoup as bs
import requests as req
import time

def continueURL():
    accepted = False
    while not accepted:
        try:
            print("=" * 5 + " Would you like to continue with this URL? [Yes / No] " + "=" * 5)
            response = str(input("Response: "))

            if response.casefold() == "No".casefold():
                global cont
                cont = False
                accepted = True
            elif response.casefold() == "Yes".casefold():
                accepted = True
            else:
                print("Invalid. Enter Yes or No.")
        except:
            print("Invalid. Enter Yes or No.")

valid = True

while valid:
    print("=" * 15 + " Enter the URL you want to scrape (omit 'https://'): " + "=" * 15)
    print("=" * 15 + " Or type quit to exit. " + "=" * 15)

    try:
        URL = 'https://' + str(input("URL: "))

        if URL.casefold() == "https://quit".casefold():
            print("Shutting down...")
            time.sleep(2)
            valid = False
        elif URL.casefold() == "https://exit".casefold():
            print("Shutting down...")
            time.sleep(2)
            valid = False
        else:
            cont = True

            while cont:
                print("[1] Full-Scrape")
                print("[2] Tag Select")
                print("[3] ID Select")
                print("[4] Exit to main menu.")

                try:
                    answer = int(input())

                    if answer == 1:
                        print("=" * 15 + " Full-Scrape " + "=" * 15)
                        time.sleep(2)

                        page = req.get(URL)
                        soup = bs(page.content, "html.parser")

                        print(soup.get_text())

                        time.sleep(2)

                        continueURL()
                    elif answer == 2:
                        print("=" * 15 + " Tag Select " + "=" * 15)
                        time.sleep(2)
                        
                        page = req.get(URL)
                        soup = bs(page.content, "html.parser")

                        tagIsValid = False
                        while not tagIsValid:
                            print("=" * 15 + " Enter a tag to parse at this URL [a, p, etc.]: " + "=" * 15)
                            print("=" * 15 + " Or type quit to exit. " + "=" * 15)
                            try:
                                userTag = str(input("Tag: "))

                                if userTag.casefold() == "quit".casefold():
                                    print("Exiting...")
                                    tagIsValid = True
                                elif userTag.casefold() == "exit".casefold():
                                    print("Exiting...")
                                    tagIsValid = True
                                else:
                                    tagSelections = (soup.findAll(userTag))
                                    for tagSelection in tagSelections:
                                        print(tagSelection.get_text())

                                    tagIsValid = True
                            except:
                                print("Invalid. Enter a tag in use.")

                        time.sleep(2)

                        continueURL()
                    elif answer == 3:
                        print("=" * 15 + " ID Select " + "=" * 15)
                        time.sleep(2)

                        page = req.get(URL)
                        soup = bs(page.content, "html.parser")

                        idIsValid = False
                        while not idIsValid:
                            print("=" * 15 + " Enter an id in use at this URL [Case-Sensitive]: " + "=" * 15)
                            print("=" * 15 + " Or type quit to exit. " + "=" * 15)
                            try:
                                userID = str(input("ID: "))

                                if userID.casefold() == "quit".casefold():
                                    print("Exiting...")
                                    idIsValid = True
                                elif userID.casefold() == "exit".casefold():
                                    print("Exiting...")
                                    idIsValid = True
                                else:
                                    # idSelections = soup.select("#" + userID)
                                    idSelections = soup.find_all(id = userID)
                                    for idSelection in idSelections:
                                        if idSelection.get_text() == "":
                                            print("ID was found, but there is no text inside.")
                                        else:
                                            print(idSelection.get_text())
                                            idIsValid = True
                            except:
                                print("Invalid. Enter an id in use.")

                        time.sleep(2)

                        continueURL()
                    elif answer == 4:
                        print("=" * 15 + " Exiting to main menu... " + "=" * 15)
                        time.sleep(2)
                        cont = False
                    else:
                        print("Invalid. Enter a number [1 - 4].")
                except:
                    print("Invalid. URL Could not be reached.")
                    time.sleep(2)
                    cont = False
    except:
        print("Enter a valid URL.")
        time.sleep(2)