! pip install html5lib
from bs4 import BeautifulSoup
import requests
import html5lib
import csv 

#This website was sourced to scrape from
source = requests.get("https://www.imdb.com/list/ls055592025/").text
soup = BeautifulSoup(source, "lxml")

#Creates a file for the information called film_scrape
new_csv = open("film_scrape.csv","w", newline="", encoding="utf-8")
csv_writer = csv.writer(new_csv)

#Prints the specified information for all movies on the website
for element in soup.find_all("div", class_="lister-item-content"):
    title = element.a.text
    date = element.find("span", class_="lister-item-year text-muted unbold").text
    rating = element.find("span", class_="ipl-rating-star__rating").text
    
    print(title)
    print(date)
    print(rating)
    
    csv_writer.writerow([title, date, rating])
new_csv.close()
