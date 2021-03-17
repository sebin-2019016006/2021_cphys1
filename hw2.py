#!/usr/bin/env python
# coding: utf-8

# # Logistic Map (part 2)

# $ f_{n+1}=r f_{n}(1-f_{n}) $

# # r=4.5, f_0 = 0.5

# In[17]:


def f(x):
    y=r*x*(1-x)
    return y


# In[51]:


r,y=4.5,0.5
n=20
fn=[]
for i in range(n):
    fn.append(y)


# In[21]:


fn


# # r=4.5, f_0 = 0.51

# In[38]:


r,y=4.5,0.51
n=20
fn=[]
for i in range(n):
    fn.append(y)


# In[35]:


fn


# # r=4.5, f_0 = 0.501

# In[36]:


r,y=4.5,0.501
n=20
fn=[]
for i in range(n):
    fn.append(y)


# In[37]:


fn


# # 피보나치 수

# $ F_n = F_{n-1} + F_{n-2}$

# In[43]:


def F(n):    
    f = []
    for n in range(n):
        if n<2:
            f.append(1)
        else:
            f.append(f[n-1]+f[n-2])
            
    return(f)
    


# In[44]:


F(11)


# In[ ]:




