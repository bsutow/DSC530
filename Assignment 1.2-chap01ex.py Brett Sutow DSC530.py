#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Setup#
import nsfg


# In[2]:


#Loads data set#
fresp = nsfg.ReadFemResp()
fresp


# In[3]:


#Shows the head of dataset#
#Shfresp.head()


# In[4]:


#Shows the number of pregnancy's#
pregnum= fresp['pregnum']
pregnum


# In[5]:


#Sorts by highest to lowest#
pregnum.sort_values(ascending=False)


# In[6]:


#Creates preg map#
preg_map = nsfg.MakePregMap(fresp)
preg_map


# In[7]:


pregnum.describe()

