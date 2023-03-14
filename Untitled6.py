#!/usr/bin/env python
# coding: utf-8

# In[24]:


get_ipython().system(' pip install selenium')

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# In[25]:


PATH = Service("/Users/kimberlynguyen/Desktop/chromedriver.exe")
driver = webdriver.Chrome(service=PATH)

driver.get("https://www.binghamton-ny.gov/home")


# In[26]:


government_menu = driver.find_element(By.XPATH, "//*[@id='dropdownrootitem3']/a")
departments_submenu = driver.find_element(By.XPATH, "//*[@id='dropdownrootitem3']/div/div/ul[1]/li/a")
# personnel_menu = driver.find_element(By.XPATH, "//*[@id='widget_4_33_127']/ul/li[16]/a")
# employment_submenu = driver.find_element(By.XPATH, "//*[@id='leftNav_1038_0_145']/ul/li/ul/li[14]/ul/li/a")


actions = ActionChains(driver)
actions.move_to_element(government_menu)
actions.click(government_menu)
actions.click(departments_submenu)
# actions.move_to_element(personnel_menu)
# actions.click(employment_submenu)
actions.perform()

# click_xpath = "//*[@id='menu-primary-navigation']/li[2]/a"
# link = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, click_xpath)))
# link.click()


# In[27]:


try:
    click_xpath = "//*[@id='widget_4_33_127']/ul/li[16]/a"
    personnel = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, click_xpath)))
    personnel.click()
    
    click_xpath = "//*[@id='leftNav_1038_0_145']/ul/li/ul/li[14]/ul/li/a"
    employment = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, click_xpath)))
    employment.click()
    


# In[ ]:


# try:
#     click_xpath = "//*[@id='widget_4_33_127']/ul/li[16]/a"
#     personnel = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, click_xpath)))
#     personnel.click()
    
#     click_xpath = "//*[@id='leftNav_1038_0_145']/ul/li/ul/li[14]/ul/li/a"
#     employment = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, click_xpath)))
#     employment.click()
    
    
#     for i in range (0,10):
#         driver.find_element(By.CSS_SELECTOR, "tbody").send_keys(Keys.CONTROL + Keys.END)

#         for table in driver.find_elements(By.CLASS_NAME, "listtable responsive-table-data-mb"):
#             title = i.find_element(By.ID, "video-title-link").get_attribute("href")
#             title = i.find_element(By.XPATH, ".//*[@id='video-title']").text
#             views = i.find_element(By.XPATH, ".//*[@id='metadata-line']/span[1]").text
#             date = i.find_element(By.XPATH, ".//*[@id='metadata-line']/span[2]").text
#             print(link, title, views, date)
        
# finally:
# #     driver.quit()
#     pass

