#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Setup#
import nsfg
import thinkplot
import thinkstats2
import matplotlib.pyplot as plt
import thinkstats2


# In[19]:


#Pulls information from data source#
chil = nsfg.ReadFemResp()


# In[20]:


#Setup for pmf#
pmf = thinkstats2.Pmf(chil.numkdhh, label='numkdhh')
pmf


# In[22]:


#Creates PMF Chart#
thinkplot.Pmf(pmf)
thinkplot.Config(xlabel='Children Total', ylabel='PMF')


# In[26]:


#Creates Bias Definition#
def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
        
    new_pmf.Normalize()
    return new_pmf


# In[27]:


#Calculates Biased#
biasedpmf= BiasPmf(pmf,label='observed biased')


# In[29]:


#Plots Biased vs PMF#
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biasedpmf])
thinkplot.Config(xlabel='Children Total', ylabel='PMF')


# In[31]:


#Biased Mean#
biasedpmf.Mean()


# In[32]:


#PMF Mean#
pmf.Mean()


# In[ ]:




