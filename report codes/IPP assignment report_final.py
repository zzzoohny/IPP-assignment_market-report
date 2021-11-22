#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import pandas as pd
import numpy as np


# In[2]:


#creating a report text file and add title
path='Superstore_report.txt'

with open(path,'w',encoding='utf-8') as report_file:
    report_file.write('Superstore Report'+'\n'*2)


# In[3]:


dataset=pd.read_csv('Superstore.csv')


# In[4]:


def getData():
    path='Superstore.csv'
    data=[]
    
    with open(path,'r', encoding='UTF8') as data_report:
        reader=csv.DictReader(data_report)
        
        for row in reader:
            record={}
            record['Category']=row.get('Category')
            record['Sub-Category']=row.get('Sub-Category')
            record['State']=row.get('State')
            record['Sales']=row.get('Sales')
            record['Profit']=row.get('Profit')
            data.append(record)
    return data

data=getData()
print(data)


# In[5]:


import statistics as s


# ### 1. Total Sales

# In[6]:


def total_sales(data):
    sales=[]
    for record in data:
        current_sales=record.get('Sales')
        sales.append(float(current_sales))
    #print(sales)
    totalsales=sum(sales)
    return totalsales

data=getData()
print(total_sales(data))


# ### 2. Total Profit

# In[7]:


def total_profit(data):
    profit=[]
    for record in data:
        current_profit=record.get('Profit')
        profit.append(float(current_profit))
    totalprofit=sum(profit)
    return totalprofit

data=getData()
print(total_profit(data))
print('The total Profit is $'+str(round(total_profit(data),2)))


# In[8]:


#Writing report part1
f=open('Superstore_report.txt','a',encoding='utf-8')
f.write('1. The total Sales is $'+ str(round(total_sales(data),2))+'\n')
f.write('2. The total Profit is $'+str(round(total_profit(data),2))+'\n')


# ### 3. Sales and profit per category

# In[9]:


cat_unique=dataset['Category'].unique()
# Furniture, Office Supplies, Technology


# In[10]:


#creating a dataframe for sales and profit per category

hi=dataset[['Sales','Profit','Category']].groupby('Category')
cat_salesprofit=pd.DataFrame(hi[['Sales','Profit']].sum(),index=cat_unique)
print(cat_salesprofit)


# In[11]:


#Writing report part 2
f.write('\n'+'3. Sales and profit per category'+'\n')
cat_salesprofit.to_csv('Superstore_report.txt',header=True,index=True,sep=' ',mode='a')


# ### 4. Sales and Profit per state

# In[12]:


state_unique=dataset['State'].unique()
print(state_unique)


# In[13]:


#creating a dataframe for sales and profit per state

hi2=dataset[['Sales','Profit','State']].groupby('State')
state_salesprofit=pd.DataFrame(round(hi2[['Sales','Profit']].sum(),2),index=state_unique)
state_salesprofit.index=state_salesprofit.index.set_names('State')
print(state_salesprofit)


# In[14]:


#Writing report part3
f.write('\n'*2+'4. Sales and Profit per state'+'\n')
state_salesprofit.to_csv('Superstore_report.txt',header=True,index=True,sep=' ',mode='a')


# ### 5. The best selling Sub-Category for each state

# In[15]:


dataset


# In[16]:


# visualize the state,Sub-category and sales
salesprof_state=dataset[['Sales','Profit','State']].groupby('State')
print(salesprof_state[['Sales','Profit']].sum())


# In[17]:


subcat_state=dataset[['Sub-Category','State','Sales']]
ans=subcat_state.groupby(['State']).max()
print(ans)


# In[18]:


f.write('\n'*2+'5. The best selling Sub-Category from each State: '+'\n')

ans.to_csv('Superstore_report.txt',header=True,index=True,sep=' ',mode='a')


# In[19]:


f.close()


# In[ ]:




