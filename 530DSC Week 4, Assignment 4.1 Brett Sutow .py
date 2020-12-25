#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Setup#
import nsfg
import thinkplot
import thinkstats2
import matplotlib.pyplot as plt
import thinkstats2


# In[2]:


#Pulls data for live births#
preg = nsfg.ReadFemPreg() 
live = preg[preg.outcome == 1] 
print(live)


# In[4]:


#Describes first born and other born#
firsts = live[live.birthord == 1] 
others = live[live.birthord != 1] 


# In[8]:


#Creates others cdf#
others_cdf = thinkstats2.Cdf(others.totalwgt_lb)


# In[9]:


#Checks my percentile rank within the cdf# 
others_cdf.PercentileRank(7.8)


# In[ ]:




