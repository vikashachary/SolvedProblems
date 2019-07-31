# -*- coding: utf-8 -*-
"""
Created on Sun May 19 13:02:35 2019

@author: vikash
"""

#%%
def merge_sort(arr, start,end,depth, modNum):
    # recursion 
    # termination condition
    if(start < end):
        left = start
        mid = (int)((start+end)/2) 
        right = end
        print(left,mid,right,arr[left:mid+1] , arr[mid+1:right+1] , "stack depth " , depth)
        #keep breaking stack length = log_2(N)
        merge_sort(arr, left, mid,depth+1,modNum)        
        merge_sort(arr, mid+1, right,depth+1,modNum)
        ## after that keep sorting
        #merge(arr,left,mid,right)
        moduloMerge(arr,left,mid,right,modNum)
    # else exit
#%%
def merge (arr, left,mid,right):
    # sort from left to right 
    temp = list(range(right-left+1))
    i = left
    j = mid+1
    k = 0
    while i<= mid and j<=right:
        if arr[i] <= arr[j]:
            temp[k]=(arr[i])
            i+=1
        else:
            temp[k]=(arr[j])
            j+=1
        k+=1 
    print(i,j,k , arr[k], k < right-left+1 )
    # if there are any left overs
    if k < right-left+1 :
        while(i<= mid):
            temp[k]=(arr[i])
            i+=1
            k+=1
        while(j<= right):
            temp[k]=(arr[j])
            j+=1
            k+=1
    arr[left:right+1] = temp[0:right-left+1]
#%%
def moduloMerge (arr, left,mid,right,modNum):
    # sort from left to right 
    temp = list(range(right-left+1))
    i = left
    j = mid+1
    k = 0
    while i<= mid and j<=right:
        if (arr[i] % modNum <= arr[j] % modNum):
            temp[k]=(arr[i])
            i+=1
        else:
            temp[k]=(arr[j])
            j+=1
        k+=1 
    print(i,j,k , arr[k], k < right-left+1 )
    # if there are any left overs
    if k < right-left+1 :
        while(i<= mid):
            temp[k]=(arr[i])
            i+=1
            k+=1
        while(j<= right):
            temp[k]=(arr[j])
            j+=1
            k+=1
    arr[left:right+1] = temp[0:right-left+1]

#%%
arrInp = [12,3,34,55,46,5,46,-12,9]
mod = 3
#%%
merge_sort(arrInp,0,len(arrInp) -1,0,mod)
print(" ".join(arrInp))
print(arrInp)

#%%
nm = input().split()
n = int(nm[0])
mod = int(nm[1])
arrInp = [int(i) for i in  input().split()]
#%%
#arrInp = [12,3,34,55,46,5,46,-12,9]
#mod = 3
#%%
merge_sort(arrInp,0,len(arrInp) -1,0,mod)

print(" ".join([str(i) for i in arrInp]))



















