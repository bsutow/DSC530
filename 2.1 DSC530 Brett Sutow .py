#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Setup#
import nsfg
import thinkplot
import thinkstats2
import matplotlib.pyplot as plt
import thinkstats2
hist = thinkstats2.Hist([1, 2, 2, 3, 5]) 
preg = nsfg.ReadFemPreg() 
live = preg[preg.outcome == 1] 
print(live)


# In[2]:


#First born vs others setup#
firsts = live[live.birthord == 1] 
others = live[live.birthord != 1] 
print(firsts)


# In[3]:


#Compares preg length data between first born vs other#
firstsprglngth= firsts.prglngth
print(firstsprglngth)

othersprglngth= others.prglngth
print(others.prglngth)


# In[4]:


#Histogram to compare the two lengths#
firsthist= thinkstats2.Hist(firsts.prglngth, label= 'prglngth')
thinkplot.Hist(firsthist)
thinkplot.show(xlabel= 'Length of Time', ylabel = 'Frequency')


# In[5]:


othershist= thinkstats2.Hist(others.prglngth, label= 'prglngth')
thinkplot.Hist(othershist)
thinkplot.show(xlabel= 'Length of Time', ylabel = 'Frequency')


# In[6]:


#Showing significant statistics comparing the two#
print(firstsprglngth.mean())
print(othersprglngth.mean())


# In[7]:


print(firstsprglngth.var())
print(firstsprglngth.std())
print(othersprglngth.var())
print(othersprglngth.std())


# In[12]:


print(firstsprglngth.describe())
print(othersprglngth.describe())


# In[ ]:




