#!/usr/bin/env python
# coding: utf-8

# In[58]:


#step one, pip install

get_ipython().system(' pip install selenium')


# In[59]:


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# In[60]:


PATH = Service("/Users/kimberlynguyen/Desktop/chromedriver.exe")
driver = webdriver.Chrome(service=PATH)


# In[62]:


driver.get("https://techwithtim.net") #bring us to the website


# In[63]:


link = driver.find_element(By.LINK_TEXT,"Python Programming") #allow us to type the text that will show up for a link and access the element from it
link.click()


# In[64]:


try:
    element = WebDriverWait(driver, 10).until( #wait up to 10 seconds for element that was clicked before to exist in order to click an existing link on screen
        EC.presence_of_element_located((By.LINK_TEXT,"Beginner Python Tutorials"))
    )
    element.click()
    
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,"sow-button-19310003"))
    )
    
    element.click()
    
    driver.back() #this goes back to previous page
    driver.back()
    driver.back() #do 3 times to go back to the homepage
    driver.forward()
    driver.forward() #goes forward 2 times 
        
except: #use except instead of finally because we don't want the page to quit unless the code above doesn't work
    driver.quit()


# In[10]:





# In[21]:





# In[ ]:





# In[ ]:




