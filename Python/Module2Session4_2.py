# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 21:28:44 2019

@author: vikash
"""

# Read the three inp7ut lists, i.e. 'C', 'F', and 'H'.
import ast,sys
import functools
#input_str = sys.stdin.read()
input_list  = [[2, 5, 9, 12, 13, 15, 16, 17, 18, 19],
[2, 4, 5, 6, 7, 9, 13, 16],
[1, 2, 5, 9, 10, 11, 12, 13, 15]]
#input_list = ast.literal_eval(input_str)
C = input_list[0]
F = input_list[1]
H = input_list[2]

# Write your code here
s1 = sorted(functools.reduce(lambda x,y: set(x).intersection(set(y)) , input_list))
s2 = sorted(set(C).intersection(set(F)).difference( set(H)) )
cardi = dict()
for game in input_list:
    for stu in game:
        if stu in cardi:
            cardi[stu] +=1
        else :
            cardi[stu] =1
s3 = sorted( list(filter(lambda k: cardi[k]==2 , cardi)))
s4 = sorted( list(filter(lambda k: k not in cardi , range(1,21))))
#s2 = sorted(set(C).intersection(set(F)).difference( set(H)) )
#s1 = ""
print(s1)
print(s2)
print(s3)
print(s4)
# (Make sure your lists are sorted in ascending order before you print them out)


