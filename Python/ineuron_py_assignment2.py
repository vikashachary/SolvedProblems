#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


# n = int(input('enter number of max stars'))


# In[6]:


n=5
if n<1:
    pass
else:
    for i in range(n*2):
        print("* "*i if i<=n else "* "*(n*2-i) )
    


# In[7]:


# s = input("")
s = "ineuron"
print(s[::-1])


# In[ ]:




