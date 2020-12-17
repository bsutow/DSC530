#!/usr/bin/env python
# coding: utf-8

# In[2]:


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


# In[3]:


#Loads data to compare first and others#
firsts = live[live.birthord == 1] 
others = live[live.birthord != 1] 
print(firsts)


# In[4]:


#Loads data for weights#

firstweights= firsts.totalwgt_lb
print(firstweights)

othersweights= others.totalwgt_lb
print(othersweights)


# In[5]:


#Below will print statistical signifant factors for both first born and others weights#
print(firstweights.mean())
print(firstweights.std())
print(firstweights.var())


# In[6]:


print(othersweights.mean())
print(othersweights.std())
print(othersweights.var())


# In[7]:


firstweights.describe()


# In[8]:


othersweights.describe()


# In[7]:


#Below shows histogram breakdown of first born child weights#
firstwhis= thinkstats2.Hist(firsts.totalwgt_lb, label= 'totalwgt_lb')
thinkplot.Hist(firstwhis)
thinkplot.show(xlabel= 'Weights', ylabel = 'Frequency')


# In[8]:


#Below shows a histogram showing the distribution of after 1st born child#
otherwhis= thinkstats2.Hist(others.totalwgt_lb, label= 'totalwgt_lb')
thinkplot.Hist(otherwhis)
thinkplot.show(xlabel= 'Weights', ylabel = 'Frequency')


# In[11]:


#The following will run cohen to show if there is a difference between the weight sets#
cohenmean= print(firstweights.mean()- othersweights.mean())
print(cohenmean)


# In[30]:


n1=len(firstweights)
n1


# In[31]:


n2=len(othersweights)
n2


# In[33]:


num= (n1+n2)
num


# In[36]:


firstwvar= firstweights.var()
otherwvar= othersweights.var()
print(firstwvar,otherwvar)


# In[39]:


polledvar = ((n1* firstwvar) + (n2 * otherwvar))
polledvar


# In[41]:


polled_var = polledvar/num
polled_var


# In[42]:


import math
squ = (math.sqrt(polled_var))
squ


# In[43]:


COHEN= polled_var/squ
COHEN


# In[ ]:


#Fun comparison#
print(firstweights.max())
print(firstweights.min())
print(othersweights.max())
print(othersweights.min())


# In[ ]:




