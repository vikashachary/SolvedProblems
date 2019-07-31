# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 13:17:03 2019
https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems/algorithm/monk-teaches-palindrome/
@author: vikash
"""
def printPalindrom(s):
    s_len = len(s)
    s_evenOdd = "EVEN" if s_len%2 ==0 else "ODD"
    if s_len ==1:
        return "YES ODD"
    isPallindrom = True
    for i in range(int(s_len/2)):
#        print(i)
        if s[i] != s[s_len-1-i]:
            isPallindrom = False
            break
    if isPallindrom:
        return "YES " + s_evenOdd
    else:
        return "NO"
#%%        
t = int(input())
for i in range(t):
    s = input()    
    print(printPalindrom(s))
