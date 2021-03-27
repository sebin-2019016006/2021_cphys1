#!/usr/bin/env python
# coding: utf-8

# # Leibniz Pi formula

# 1.함수

# In[1]:


def f(x):
    y=(1/(2*x-1))*(-1)**(x+1)
    
    return y


# In[2]:


n=101
fn=[]

for x in range(1,n,1):
    fn.append(f(x))


# In[3]:


fn


# In[4]:


def F(n):
    
    f=[]
    
    for n in range(0,n,1):
        if n==0:
            f.append(fn[0])
        else:
            f.append(f[n-1]+fn[n])
            
    return(f)


# In[5]:


F(100)


# 2.그래프

# In[6]:


import numpy as np
import matplotlib.pyplot as plt


# In[7]:


np.pi


# In[8]:


a=F(100)
b=[s for s in range (100)]
c=[np.pi/4 for s in range (100)]


# In[9]:


plt.plot(b,a ,'_-',color='pink',label='Leibniz formula for pi')
plt.plot(b,c,'_-',color='skyblue', label='${pi}/{4}$')
plt.xlabel('x')
plt.xlabel(r'$\ n$',rotation=0)
plt.ylabel('y', rotation=0)
plt.legend()


# # Logistic Map

# 1. 함수

# In[1]:


def f(r,y):
    fn=[]
    for n in range(1,100):
        y=r*y*(1-y)
        fn.append(y)
    return fn


# In[2]:


f(0.5,0.5)


# In[3]:


f(0.95,0.5)


# In[4]:


f(2,0.5)


# In[5]:


f(3.2,0.5)


# In[6]:


f(3.8,0.5)


# In[7]:


f(3.8,0.501)


# 2. 그래프

# In[8]:


import numpy as np
import matplotlib.pyplot as plt


# In[9]:


def f(r,y):
    fn=[]
    for n in range(1,100):
        y=r*y*(1-y)
        fn.append(y)
    return fn


# In[20]:


plt.plot(f(0.5,0.5),color='gray')


# In[21]:


plt.plot(f(0.95,0.5),color='black')


# In[22]:


plt.plot(f(2,0.5),color='green')


# In[23]:


plt.plot(f(3.2,0.5),color='lavender')


# In[24]:


plt.plot(f(3.8,0.5),color='pink')


# In[25]:


plt.plot(f(3.8,0.501),color='skyblue')


# # Sinc fuction

# In[26]:


import numpy as np
import matplotlib.pyplot as plt


# In[27]:


a=np.arange(-20,20,0.01)
b=[np.sin(x)/x for x in a]
plt.figure(figsize=(8,8))
plt.plot(a,b)


# 2. 테일러 전개

# In[29]:


import numpy as np
import matplotlib.pyplot as plt
import math


# In[30]:


def f(x):
    for x in range(1,100):
        y=(((-1)**(n))*(x**(2*n)))/(math.factorial(2*n+1))
        fn=[]
        fn.append(y)
    return fn
    for n in range(1,100):
        y=(((-1)**(n))*(x**(2*n)))/(math.factorial(2*n+1))
        sn=[]
        fn.append(y)
        return sn


# In[ ]:




