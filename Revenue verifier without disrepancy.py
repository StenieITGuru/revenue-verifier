#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


df=pd.read_csv('march_1_to_15_cleaned.csv')


# In[3]:


df.columns


# In[4]:


df.columns = df.columns.str.strip()


# In[5]:


df.columns = df.columns.str.lower()


# In[6]:


df.columns = df.columns.str.replace(" ", "_")


# In[7]:


df.columns[df.columns.duplicated()]


# In[8]:


df.info()


# In[9]:


df['total_revenue'] = df['charge_amount'] + df['collection_charge_amount']


# In[10]:


if 'total_company_revenue' in df.columns:
    df = df.drop(columns=['total_company_revenue'])


# In[11]:


df[['charge_amount','collection_charge_amount']].head()


# In[12]:


numeric_cols = ['charge_amount', 'collection_charge_amount']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')  

df['revenue'] = df['charge_amount'] + df['collection_charge_amount']

total_charge = df['charge_amount'].sum()
total_collection = df['collection_charge_amount'].sum()
total_revenue = df['revenue'].sum()

print("Total charge_amount:", total_charge)
print("Total Collection Charge_amount:", total_collection)
print("Total Revenue (Charge + Collection):", total_revenue)


# In[ ]:




