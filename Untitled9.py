#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import csv
import seaborn as sns 

#reads csv file in order to create a panda for the data
dataframe = pd.read_csv("AB_NYC_2019 - AB_NYC_2019.csv")
dataframe

#seaborn map created and shows last review and reviews per month have null values
columns = df.columns
sns.heatmap(df[cols].isnull())

#copy of dataframe2 is created and this replaces the NaN values 
dataframe2 = dataframe.copy()
dataframe2["last_review"] = dataframe2["last_review"].fillna("No review")
dataframe2["reviews_per_month"] = dataframe2["reviews_per_month"].fillna("No review")
columns = dataframe2.columns
sns.heatmap(df2[cols].isnull())

#copy of dataframe is created to isolate the last review column
dataframe3 = dataframe.copy()
dataframe3.last_review = dataframe3.last_review.str.slice(0,4)
dataframe3

#prints all the Airbnbs in each borough
borough = dataframe3["neighbourhood_group"]
boroughDict = {}

for i in borough:
    if i not in boroughDict:
        boroughDict[i] = 1
    else:
        boroughDict[i] += 1
print(boroughDict)
        


# In[ ]:




