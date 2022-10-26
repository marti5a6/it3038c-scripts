from bs4 import BeautifulSoup as bs
import requests as req
import time

# Store Page Content
URL = str("https://legislature.ohio.gov/legislators/senate-directory")
page = req.get(URL)
soup = bs(page.content, 'html.parser')

# Create Array of Name and Description
title = soup.find_all("div", attrs={"class":"mediaCaptionTitle"})
caption = soup.find_all("div", attrs={"class":"mediaCaptionSubtitle"})

# Print Function Description
print("="*15, "List of Ohio Senators", "="*15)
time.sleep(2)

# Print Formatted List
for i in range(0, len(title)):
    print(title[i].get_text() + " | " + caption[i].get_text())