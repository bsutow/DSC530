#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Setup#
import nsfg
import thinkplot
import thinkstats2
import matplotlib.pyplot as plt
import thinkstats2
import numpy as np


# In[5]:


#Generates Random Numbers#
rand = np.random.random(1000)
rand


# In[6]:


#Creates PMF for random numbers#

pmf = thinkstats2.Pmf(rand)
pmf


# In[7]:


#Creates CDF for random numbers#

cdf= thinkstats2.Cdf(rand)
cdf


# In[9]:


#Plots Random PMF#

thinkplot.Pmf(pmf)
thinkplot.Config(xlabel='Random Number', ylabel='PMF')


# In[10]:


#Plots random CDF#
thinkplot.Cdf(cdf)
thinkplot.Config(xlabel='Random Number', ylabel='CDF')


# In[ ]:




