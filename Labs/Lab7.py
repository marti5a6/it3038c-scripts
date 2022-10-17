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

        if URL == "https://quit":
            print("Shutting down...")
            time.sleep(2)
            valid = False
        elif URL == "https://exit":
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

                        print(soup.p.get_text())

                        time.sleep(2)

                        continueURL()
                    elif answer == 3:
                        print("=" * 15 + " ID Select " + "=" * 15)
                        time.sleep(2)

                        page = req.get(URL)
                        soup = bs(page.content, "html.parser")

                        idIsValid = False
                        while not idIsValid:
                            try:
                                print("Enter an id in use at this URL: ")
                                id = str(input("ID: "))

                                soup.id.get_text()

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