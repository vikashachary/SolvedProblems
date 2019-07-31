# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 20:14:29 2019

@author: vikash
"""


# importing itertools for accumulate() 
import itertools 
# importing functools for reduce() 
import functools 
  
# initializing list  
lis = [ 1, 3, 4, 10, 4 ] 
  
# priting summation using accumulate() 
print ("The summation of list using accumulate is :",end="") 
print (list(itertools.accumulate(lis,lambda x,y : x+y))) 
  
# priting summation using reduce() 
print ("The summation of list using reduce is :",end="") 
print (functools.reduce(lambda x,y:x+y,lis)) 

