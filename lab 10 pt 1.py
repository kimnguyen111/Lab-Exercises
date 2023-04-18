#!/usr/bin/env python
# coding: utf-8

# In[8]:


#Part 1

import requests
import json
from tkinter import *

root = Tk()
root.title("Drop down menu")
root.geometry("400x400")

url = "https://api.quotable.io/quotes/random?limit=10"
quote = requests.get(url)
quotejson = quote.json()
quotejson


authorList=[]
for i in range(10):
    name = quotejson[i]['author']
    authorList.append(name)
print(authorList)


def chosen_option():
    name = value.get()
    for i in range(10):
        if name == authorList[i]:
            quoteBack = quotejson[i]['content']
        
        
    result_label = Label(root, text=quoteBack)
    result_label.pack()
    
value = StringVar()
value.set("Select an author")

dropdown = OptionMenu(root, value, *authorList)
choose_button = Button(root, text="Click to get quote", command=chosen_option)

dropdown.pack()
choose_button.pack()

root.mainloop()


# In[6]:





# In[ ]:





# In[ ]:




