#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas_datareader.data as web


# In[7]:


import datetime


# In[9]:


start = datetime.datetime(2020,3,3)
end = datetime.datetime(2020,3,29)


# In[11]:


gs=web.DataReader("078930.KS","yahoo",start,end)


# In[12]:


gs


# In[ ]:




