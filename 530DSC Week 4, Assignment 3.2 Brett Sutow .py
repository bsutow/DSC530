#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Setup#
import nsfg
import thinkplot
import thinkstats2
import matplotlib.pyplot as plt
import thinkstats2


# In[8]:


#Pulls information from data source#
chil = nsfg.ReadFemResp()
pmf = thinkstats2.Pmf(chil.numkdhh, label='numkdhh')
pmf


# In[12]:


#Creates PMF Mean and Var#
PMFMean=(pmf.Mean())
PMFVAR=(pmf.Var())


# In[13]:


#Calculates mean#
PMFMean


# In[15]:


#Calculates Variance#
PMFVAR


# In[ ]:




