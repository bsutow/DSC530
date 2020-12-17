#!/usr/bin/env python
# coding: utf-8

# # Examples and Exercises from Think Stats, 2nd Edition
# 
# http://thinkstats2.com
# 
# Copyright 2016 Allen B. Downey
# 
# MIT License: https://opensource.org/licenses/MIT
# 

# In[8]:


from __future__ import print_function, division

import nsfg


# ## Examples from Chapter 1
# 
# Read NSFG data into a Pandas DataFrame.

# In[9]:


preg = nsfg.ReadFemPreg()
preg.head()


# Print the column names.

# In[32]:


preg.columns
for col in preg.columns: 
    print(col) 


# Select a single column name.

# In[13]:


preg.columns[1]


# Select a column and check what type it is.

# In[14]:


pregordr = preg['pregordr']
type(pregordr)


# Print a column.

# In[15]:


pregordr


# Select a single element from a column.

# In[16]:


pregordr[0]


# Select a slice from a column.

# In[17]:


pregordr[2:5]


# Select a column using dot notation.

# In[19]:


pregordr = preg.pregordr
pregordr


# Count the number of times each value occurs.

# In[20]:


preg.outcome.value_counts().sort_index()


# Check the values of another variable.

# In[21]:


preg.birthwgt_lb.value_counts().sort_index()


# Make a dictionary that maps from each respondent's `caseid` to a list of indices into the pregnancy `DataFrame`.  Use it to select the pregnancy outcomes for a single respondent.

# In[22]:


caseid = 10229
preg_map = nsfg.MakePregMap(preg)
indices = preg_map[caseid]
preg.outcome[indices].values


# ## Exercises

# Select the `birthord` column, print the value counts, and compare to results published in the [codebook](http://www.icpsr.umich.edu/nsfg6/Controller?displayPage=labelDetails&fileCode=PREG&section=A&subSec=8016&srtLabel=611933)

# In[26]:


birthord= preg['birthord']
print(birthord)


# We can also use `isnull` to count the number of nans.

# In[27]:


preg.birthord.isnull().sum()


# Select the `prglngth` column, print the value counts, and compare to results published in the [codebook](http://www.icpsr.umich.edu/nsfg6/Controller?displayPage=labelDetails&fileCode=PREG&section=A&subSec=8016&srtLabel=611931)

# In[52]:


prglngth = preg['prglngth']
prglngth


# To compute the mean of a column, you can invoke the `mean` method on a Series.  For example, here is the mean birthweight in pounds:

# In[30]:


preg.totalwgt_lb.mean()


# Create a new column named <tt>totalwgt_kg</tt> that contains birth weight in kilograms.  Compute its mean.  Remember that when you create a new column, you have to use dictionary syntax, not dot notation.

# In[37]:


preg['totalwgt_kg'] = preg.totalwgt_lb / 2.205
totalwgt_kg= preg['totalwgt_kg']
print(totalwgt_kg)
preg.totalwgt_kg.mean()


# `nsfg.py` also provides `ReadFemResp`, which reads the female respondents file and returns a `DataFrame`:

# In[38]:


resp = nsfg.ReadFemResp()


# `DataFrame` provides a method `head` that displays the first five rows:

# In[39]:


resp.head()


# Select the `age_r` column from `resp` and print the value counts.  How old are the youngest and oldest respondents?

# In[41]:


age_r = resp['age_r']
age_r.sort_values()


# We can use the `caseid` to match up rows from `resp` and `preg`.  For example, we can select the row from `resp` for `caseid` 2298 like this:

# In[42]:


resp[resp.caseid==2298]


# And we can get the corresponding rows from `preg` like this:

# In[43]:


preg[preg.caseid==2298]


# How old is the respondent with `caseid` 1?

# In[50]:


resp1 = resp[resp.caseid==1]
resp1.age_r


# What are the pregnancy lengths for the respondent with `caseid` 2298?

# In[53]:


preg2298= preg[preg.caseid==2298]
preg2298.prglngth


# What was the birthweight of the first baby born to the respondent with `caseid` 5012?

# In[54]:


preg5012 = preg[preg.caseid==5012]
print(preg5012.totalwgt_lb)


# In[ ]:




