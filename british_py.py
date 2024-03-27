#!/usr/bin/env python
# coding: utf-8

# # British airways review 

# In[81]:



import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict
plt.style.use("ggplot")
sns.set(style="whitegrid")


# In[82]:


df = pd.read_csv(r"C:\Users\juani\OneDrive\Desktop\PYTHON\myexercises\data\British_airways_review\British_Airway_Review.csv")


# In[83]:


df.head()


# In[84]:


num_rows, num_columns = df.shape

null_values = df.isnull().sum().sum()

duplicates_n = df[df.duplicated()].shape[0]
# Diagnostics results
data_checking = """
- The data has {0} rows and {1} columns
- There are {2} null/na values and {3} duplicated rows. 
""" 
print(data_checking.format(num_rows, num_columns,
                        null_values, duplicates_n))


# In[85]:


for col in df.columns[2:]:
    print(col)
    columns_cats_count = df[col].value_counts(sort=True)
    num_cats = len(columns_cats_count.keys())
    frequency = dict(columns_cats_count)
    if num_cats <= 10:
        print(num_cats)
        print(frequency)
    else:
        print(num_cats)


# In[ ]:





# In[86]:


profile_columns = ['country', 'seat_type', 'type_of_traveller']
profile_statistic = df[profile_columns].describe()
print(profile_statistic)


# #  Top 5 countries with most flights

# In[87]:


country_flights = df["country"].value_counts(normalize=False, sort=True)
countries_top5 = country_flights.head(5)
countries_top5.plot(kind="bar", color=["lightblue","lightgreen","violet","brown"], rot=45)
plt.ylabel("Number of Flights", fontweight='bold')
plt.title("TOP 5 COUNTRIES WITH MOST FLIGHTS", fontsize=15, fontweight='bold')
plt.show()
print(countries_top5)


# # TOP 3 TYPE OF TRAVELLER PER COUNTRY
#   

# In[88]:


country_flights = df["country"].value_counts()
countries_top10 = country_flights.head(3)
type_travellers_countries = df[df["country"].isin(countries_top10.index)].groupby(["type_of_traveller", "country"]).size().reset_index(name="counts")

plt.figure(figsize=(12, 10))
sns.barplot(data=type_travellers_countries, x="counts", y="country", hue="type_of_traveller")
plt.xlabel("Passengers", fontsize=13, fontweight='bold')
plt.title(" Type of Traveller per country", fontsize=15, fontweight='bold')
plt.legend(title="Type of Traveller")
plt.show()


# #   Type of traveller total number 
#  

# In[89]:


seat_freq = df['seat_type'].value_counts(sort=True)
seat_type = list(seat_freq.index)
seat_counts = list(seat_freq.values)

tipo_freq = df['type_of_traveller'].value_counts(sort=True)
tipos = list(tipo_freq.index)
tipo_counts = list(tipo_freq.values)

fig, (ax1, ax2) = plt.subplots(1,2)
fig.suptitle("Flights and Seat types", y=0.8, fontsize=15, fontweight="bold")
ax1.pie(labels=seat_type, x=seat_counts, autopct='%.0f%%')
ax1.set_title('${Seat}$ ${Type}$', fontweight="bold")
ax2.pie(labels=tipos, x=tipo_counts, autopct='%.0f%%')
ax2.set_title("${Traveller}$ $ {Type}$", fontweight="bold")
fig.tight_layout(pad=.75)
plt.show()


# # Who recommend the flights? 

# In[90]:


sns.barplot(data = df, x="stars", y="seat_type", hue="recommended")
plt.title("Recommendations by Seat Type")
plt.xlabel("Number of stars")
plt.show()


# 
# 

# In[ ]:





# In[ ]:




