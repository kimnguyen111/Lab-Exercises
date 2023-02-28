! pip install html5lib
from bs4 import BeautifulSoup
import requests
import html5lib
import csv 

#Writes the information onto a file called library_scrape
new_csv = open("library_scrape.csv","w", newline="", encoding="utf-8")
csv_writer = csv.writer(new_csv)

#Starts scraping from page 1
page = 1

#Scrapes up until the 5th page
while page != 6:
    source = requests.get(f"https://www.loc.gov/search/?q=cats&sp={page}").text  #Sources the website to scrape from
    soup = BeautifulSoup(source, "lxml") 

#Scrapes the specified information for all items on pages 1-5
    for element in soup.find_all("div", class_="item-description"):
        title = element.a.text.strip()
        try:
            description = element.find("span", class_="item-description-abstract").text.strip()
        except:
            decription = "No description found"
        link = element.a.get("rel")
        
#Extra Credit
        try:
            contributor = element.find("ul").text.strip()
        except:
            contributor = "No contributor found"
        
        print(title)
        print(description)
        print(link)
        print(contributor)
       
        csv_writer.writerow([title, description, link])
    page += 1
    
new_csv.close()
    
