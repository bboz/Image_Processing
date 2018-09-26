
# coding: utf-8

# In[1]:

test="DIP"
test


# In[2]:

s=10
s2=25
s1+s2


# In[3]:

s+s2


# In[33]:

liste=[0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1,2,0,1]


# In[13]:

for i in liste:
    print(int(i)+1)


# In[34]:

for i in range(0,len(liste)):
    liste[i]=liste[i]+1


# In[35]:

liste


# In[36]:

import random


# In[42]:

s=random.randint(2,5)
s


# In[45]:

listee=[]
for i in range(10):
    listee.append(random.randint(0,10))
print(listee)


# In[83]:

test_sayısı=100000


# In[61]:

def createArray(s):
    myList=[]
    for i in range(s):
        myList.append(random.randint(0,10))
    return myList

def printArray(array):
    print(array)
    
def incArray(array):
    myList_1=[]
    for i in array:
        myList_1.append(i+1)
    return myList_1

def createArrayVersion(s):
    myList=np.arange(s)
    return myList


# In[68]:

dizi_1=createArray(test_sayısı)
printArray(dizi_1)
dizi_2=incArray(dizi_1)
printArray(dizi_2)


# In[60]:

import numpy as np
x=np.arange(10)
x


# In[85]:

myL=createArrayVersion(test_sayısı)
myL=myL+25


# In[86]:

myL[10025]


# In[87]:

print("*"*500)


# In[88]:

import matplotlib.pyplot as plt


# In[89]:

image_1=plt.imread("test_1.jpg")


# In[93]:

plt.imshow(image_1)
plt.show()


# In[91]:

image_1.shape


# In[94]:

type(image_1)


# In[ ]:



