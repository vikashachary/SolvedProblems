# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:16:20 2019

@author: vikash


#%%
class KmpMatcher(object):
    def __init__(self, pattern, string, stringName):
        self.patt = pattern.upper()
        self.seq = string.upper()
        self.header = stringName
        self.prefix = []
        self.validBases = ['A', 'T', 'G', 'C', 'N']
    
    #Initialize the prefix list and set first element to 0
    def fillPrefixList(self):
        self.prefix = [None] * len(self.patt)
        self.prefix[0] = 0
    #Matches the motif pattern against itself.
    def computePrefix(self):
        #Initialize prefix array
        self.fillPrefixList()
        k = 0    
        for pos in range(1, len(self.patt)):
            #Check valid nt
            if(self.patt[pos] not in self.validBases):
                self.invalidMotif()
    
            #Unique base in motif
            while(k > 0 and self.patt[k] != self.patt[pos]):
                k = self.prefix[k]
            #repeat in motif
            if(self.patt[k] == self.patt[pos]):
                k += 1
    
            self.prefix[pos] = k
    
    #An invalid character in the motif message to the user
    def invalidMotif(self):
        print("Error: motif contains invalid DNA nucleotides")
        exit()
    
    #An invalid character in the sequence message to the user
    def invalidSequence(self):
        print("Error: " + str(self.header) + "sequence contains invalid DNA nucleotides")
        exit()
#%%
    
if __name__ == "__main__":

    #Intialise a single neuron neural network.
    kmp = KmpMatcher("AAATAAA", "AAAAAAAAATAAAAAATAAA", "vik")
    kmp.computePrefix()
    print(kmp.prefix )
"""
#%%
t = "rishrisrishirishirishrishiririshi"
p = "rishi"
m=len(p)
lcp =[0 for x in range(m)]
lcp[0]=0
#%%
for i in range(1,m):
    
    j=lcp[i-1]
    print(i ,j, p[i] , p[j])
    while(j>0 and p[i]!=p[j]):
        j=lcp[j-1]
        print(i ,j, p[i] , p[j])
    if(p[i]==p[j]):
        j+=1    
    print(j)
    lcp[i]=j
print(lcp)
#%%
n = len(t)
i=0
while (i <n):
    #j = 0
    print(i ,j, t[i] , p[j])
    #j=lcp[i-1]
    #print(i ,j, p[i] , p[j])
    
    if(t[i]==p[j]):
        i+=1
        j+=1
    if j== m:
        if i-j >=0 :
            print("found index" , i-j)
        j = lcp[j-1]
        
    if(i < n and j < m):
        print(i ,j, t[i] , p[j])
        
    if(i<n and t[i]!=p[j]):
        if j!=0:
            j = lcp[j-1]
        else:
            i+=1    
    if(i < n and j < m):
        print(i ,j, t[i] , p[j])        
        print("-----")
    #print(j)
    #i=lcp[j]
print(t[i-j:j])
