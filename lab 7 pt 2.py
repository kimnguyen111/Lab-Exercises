#!/usr/bin/env python
# coding: utf-8

# In[24]:


import requests
import json
import csv
import pandas as pd
from datetime import date

#looking for Vietnam info in 2023 
year = "2023"
countryCode = "VN"

#get general info about Vietnam in 2023
vietInfo = requests.get(f"https://date.nager.at/api/v3/CountryInfo/{countryCode}")
jsonVietInfo = vietInfo.json()
print(jsonVietInfo)
print()

#get all countries by returning name and code
countries = requests.get(f"https://date.nager.at/api/v3/AvailableCountries")
jsonCountries = countries.json()
print(jsonCountries)
print()

#get the start and end date of the long weekend for a specific country and year
weekend = requests.get(f"https://date.nager.at/api/v3/LongWeekend/{year}/{countryCode}")
jsonWeekend = weekend.json()
print(jsonWeekend)
print()

#get holidays of Vietnam in 2023 
holidays = requests.get(f"https://date.nager.at/api/v3/PublicHolidays/{year}/{countryCode}")
jsonHoli = holidays.json()
print(jsonHoli)
print()

#find out whether today is a holiday in Vietnam
todayHoli = requests.get(f"https://date.nager.at/api/v3/IsTodayPublicHolidays/{countryCode}")
if todayHoli.status_code == 404:
    pass
else:
    jsonToday = todayHoli.json()
    print(jsonToday)
    print()

#get the holidays that are upcoming within the week
nextHoli = requests.get(f"https://date.nager.at/api/v3/NextPublicHolidaysWorldiwide")
if nextHoli.status_code == 404:
    pass
else:
    jsonNext = nextHoli.json()
    print(jsonNext)
    print()




# In[ ]:




