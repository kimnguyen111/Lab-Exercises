#!/usr/bin/env python
# coding: utf-8

# In[110]:


#step one, pip install

get_ipython().system(' pip install selenium')


# In[169]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# In[170]:


PATH = Service("/Users/kimberlynguyen/Desktop/chromedriver.exe")
driver = webdriver.Chrome(service=PATH)


# In[171]:


driver.get("https://data.gov/") #bring us to the website


# In[172]:


link = driver.find_element(By.LINK_TEXT,"DATA") #allow us to type the text that will show up for a link and access the element from it
link.click()


# In[173]:


searchBar = driver.find_element(By.NAME,'q') #finds the searchbar and clicks it
searchBar.send_keys("Climate change") #types in "climate change"
searchBar.send_keys(Keys.RETURN) #presses the enter button to direct us to results from search


# In[164]:


import selenium


# In[174]:


#scrape first title
title = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div/section[1]/div[2]/ul/li[5]/div/h3/a").text #allow us to access the title 
print(title)


# In[118]:


link = driver.find_element(By.LINK_TEXT,"Food Price Outlook") #allow us to access the link of the article


# In[109]:


description = driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div/article/section[1]/div[2]").text #allow us to access the description after pressing link
print(description)


# In[ ]:





# In[175]:


# scraping all titles
title_list = []

for i in titles:
    title_list.append(i.text)
print(title_list)
  


# In[152]:


len(titles)


# In[153]:


titles[:10]


# In[ ]:




