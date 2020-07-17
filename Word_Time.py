#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import json
import string
from random import randint


# In[2]:


# You only need to set the file name with path in the file_abs


# In[3]:


# Enter the file name including the path.
file_abs='data/final_format'


# In[4]:


final=open(file_abs).read()


# In[5]:


all_list=final.split('\n')


# In[6]:


strip_item=[]


# In[7]:


for item in all_list:
    strip_item.append(item.strip())


# In[8]:


result_dict=dict()


# In[9]:


i=0
sub_list=[]
for item in strip_item:
    if item.startswith('results {'):
        if len(sub_list)>0:
            result_dict[f"Result {i}"]=sub_list
            sub_list=[]
        i+=1
        continue
    sub_list.append(item)


# In[10]:


#result_dict


# In[11]:


resultant=dict()


# In[12]:


for result in result_dict.keys():
    i=0
    word_data=list()
    word_dict=dict()
    for item in result_dict[result]:
        
        if item.startswith('words') or item.startswith('alternatives {') or item.startswith('transcript:') or item.startswith('confidence:'):
            continue
        if not item.startswith('}'):
            word_data.append(item.replace('"','').replace('{','').strip())
        if item.startswith('word:'):
            word_dict[f"Word {i}"]=word_data
            word_data=[]
            i+=1
    resultant[result]=word_dict       


# In[13]:


#resultant


# In[14]:


# Similarly we can do for each and every result in a loop from keys. Result 1, Result 2..... and so on...


# In[15]:


def has_num(s):
    return any(i.isdigit() for i in s)
def convert_time(lst):
    time=lst[0].split(':')[1].strip()
    time+='.'
    if lst[1].startswith('nanos'):
        time+=lst[1].split(':')[1].strip()
    else:time+='0'
    return time     


# In[16]:


for key_res in resultant.keys():
    print(f'[{key_res}] [STARTS **********] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] []')
    i=0
    for startend in resultant[key_res]:
        word_list=resultant[key_res][startend]
        word_val=word_list[-1].split(':')[1].strip()
        if i==0:
            print('-----------------------')
            print(f"RANDOM_ID: {randint(1000,9999)}")
            nn_list=[iter_item for iter_item in word_list if has_num(iter_item)]  
            print(f"STARTS : {convert_time(nn_list)}")
            i+=1
        if word_val.endswith('.'):
            nn_list=[iter_item for iter_item in word_list if has_num(iter_item)]
            print(f"ENDS : {convert_time(nn_list)}")
            print('-----------------------')
            i=0 
    print(f'[{key_res}] [ENDS **********] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] [] []')


# In[ ]:




