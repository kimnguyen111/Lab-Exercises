#!/usr/bin/env python
# coding: utf-8

# In[16]:


import requests 
import json
import csv 
from matplotlib import pyplot as plt 
import pandas as pd 

#setting the countries to scrape information only in 2023 
year = "2023"
countries = ["VN", "US", "JP", "KR", "JP", "RU", "HT", "MX", "JM", "IT"]

#csv file is opened and initiated 
csv_file = open("allHolidays.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Country Code", "# of Holidays"])

#goes through all 10 countries and counts them (to compare), and puts them in a csv file
for i in range(len(countries)):
    countryCode = countries[i]

    counter = 0
    holidays = requests.get(f"https://date.nager.at/api/v3/PublicHolidays/{year}/{countryCode}")
    file = holidays.json()
    file

    for i in file:
        name = i['name']
        counter += 1
        csv_writer.writerow([countryCode, counter])
csv_file.close()


# In[18]:


#bonus!!
sheet = pd.read_csv("allHolidays.csv")
sheet
df = pd.DataFrame(sheet)

countryCode = df["Country Code"]
allHolidays = df["# of Holidays"]

fig = plt.figure(figsize = (22,18))
plt.bar(countryCode, allHolidays)

plt.xlabel("Country Code")
plt.ylabel("# of Holidays")
plt.title("All Holidays in Different Countries")

plt.show()


# In[ ]:




