#!/usr/bin/env python
# coding: utf-8

# In[23]:


import requests
import json
import csv
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


# In[31]:


lat = "42.098701"
lon = "-75.912537"
url = requests.get(f"https://api.weather.gov/points/{lat},{lon}")

csv_file = open("weather_scrape.csv", "w", newline="", encoding="utf-8")
csv_writer = csv.writer(csv_file)

json_file = url.json()
json_file

#get name, temp, detailed forecast by finding them under properties and forecast
forecast = json_file["properties"]["forecast"]
new_request = requests.get(forecast)

json = new_request.json()
json

#portion of json_file into json
info = json["properties"]["periods"]

csv_writer.writerow(["Time", "Temperature", "Description"])

#for loop prints for all the info under the properties tag
for i in info:
    print(i["name"])
    print(i["temperature"])
    print(i["detailedForecast"])
    csv_writer.writerow([i["name"], i["temperature"], i["detailedForecast"]])
csv_file.close()


# In[35]:


sheet = pd.read_csv("weather_scrape.csv")
sheet
df = pd.DataFrame(sheet)

week = df["Time"]
temp = df["Temperature"]

fig = plt.figure(figsize = (22,18))
plt.bar(week, temp)

plt.xlabel("Time")
plt.ylabel("Temperature")
plt.title("Binghamton Weather Data")

plt.show()


# In[ ]:




