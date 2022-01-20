#!/usr/bin/env python
# coding: utf-8

# In[3]:


name=input("enter your name:")
age=int(input("In numbers, enter your age: "))
qualification=input("enter your highest qualification: ")
address=input("enter your address :")
list=[name,age,qualification,address]
for i in list:
    print(f"{i}", sep="\n")

