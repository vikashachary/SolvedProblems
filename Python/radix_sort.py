# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 18:12:50 2019
https://www.geeksforgeeks.org/radix-sort/
@author: vikash
"""
#%%

def counter_sort(lst,xPos =0):
    n = len(lst)
    base10list = []
    for i in range(10):
        base10list.append([])
    output = []
    for i in range(n):
        num = lst[i]
        for k in range(xPos):
           num = int(num /10)
        j = int(num % 10)
        base10list[j].append(lst[i])
    for i in range(10):
        if len(base10list[i]) >0:
            for j in base10list[i]:
                output.append(j)
    return output
#%%
# print(counter_sort([67,34,345,56],1))
lst = [67,34,345,56]
maxNum = 0
for i in lst:
    maxNum = maxNum if i < maxNum else i
maxChar = 0
num = maxNum
while num >0:
    num = int(num /10)
    maxChar +=1
for k in range(maxChar):
    lst = counter_sort(lst,k)
print(lst)
# t = int(input())
# for i in range(t):
#     n = int(input())
#     lst = list(map(int, input().rstrip().split()))
#     result = counter_sort(lst,n)
#     print(result)

