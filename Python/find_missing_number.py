# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 09:24:16 2019

@author: vikash
"""
def missing_item(lst,n):
    missing = -1
    if len(lst) == 0:
        return 1
    
    sum_n = n*(n+1)/2
    sum_lst = sum(lst)
    missing = sum_n-sum_lst
    return int(missing)
t = int(input())
for i in range(t):
    n = int(input())
    lst = list(map(int, input().rstrip().split()))
    result = missing_item(lst,n)
    print(result)