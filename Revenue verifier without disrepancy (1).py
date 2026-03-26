#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


df=pd.read_csv('March_1_25th_daily_transactions.csv',low_memory=False)


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


df[['charge_amount','collection_charge_amount']].head()


# In[11]:


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


# In[12]:


df['transaction_value'] = df['debit'] + df['credit']


# In[13]:


df[['debit','credit']].head()


# In[15]:


numeric_cols = ['debit', 'credit']
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')  

df['transation_value'] = df['debit'] + df['credit']

total_debit = df['debit'].sum()
total_credit = df['credit'].sum()
total_value = df['transaction_value'].sum()

print("Total debit:", total_debit)
print("Total  credit:", total_credit)
print("Total transaction value (debit + credit):", total_value)


# In[ ]:




