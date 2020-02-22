#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random as rd


# In[4]:


class typingMonkey():
    
    def __init__(self,nGen=1,cFactor=.5, Tmax = 5, Tmin =4,mutationF = 2,userString = ""):
        self.nGen = nGen
        self.CrossoverFactor =cFactor
        self.maxChromSize=Tmax
        self.minChromeSize=Tmin
        self.mutationFactor=mutationF
        self.goalState=userString
        self.goalStateL = len(userString)
        self.possibleGenes = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w',
                              'x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T',
                              'U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0',' ','<',',','.','>','/','?',
                             ':',';','"','[',']','{','}','-','_','=','+','!','@','3','$','%','^','&','*','(',')']
        
        
    def setTmax(self,newT):
        self.maxChromSize = newT
        
    def getTmax(self):
        return self.maxChromSize
        
    def setTmin(self,newT):
        self.minChromSize =minT
        
    def getTmin(self):
        return self.minChromSize
    
    def setMutationFactor(self,newM):
        self.mutationFactor= newM
        
    def GetMutationFactor(self):
        return self.mutationFactor
    
    def generate(self):
        for()
    


# In[ ]:


t =typingMonkey(userString="hello")
t.generate()


# In[ ]:




