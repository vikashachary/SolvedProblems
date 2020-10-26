#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np


# In[2]:


# n = int(input('enter number of max stars'))


# In[5]:


lst = []
for i in range(2000,3201,7):
    if i%5!=0: 
        lst.append(str(i))
print( ','.join(lst) ) 


# In[7]:


f = input("first name")
l = input("last name")
# s = "ineuron"
print(f[::-1] +' '+ l[::-1])


# In[17]:


vol = (4/3)*np.pi*(12**3)
print(vol ," cubic cm ")


# In[ ]:




