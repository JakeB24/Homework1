#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# problem 1
def github() -> str:
    return " "


# In[7]:


# problem 2 evens and odds. 
def evens_and_odds(n: int) -> dict:
    evencount=0
    oddcount=0
    for i in range(1,n):
        if(i%2==0):
            evencount += i   
        else:
            oddcount +=i

    return{"evens": evencount, "odds": oddcount}
    
print(evens_and_odds(4))   


# In[3]:


# problem 3 
from datetime import datetime
from typing import Union

def time_diff(date_1: str, date_2: str, out: str) -> Union[str,float]:
    date_1 = datetime.strptime(date_1, '%Y-%m-%d')
    date_2 = datetime.strptime(date_2, '%Y-%m-%d')
    timebetween = abs(date_2-date_1).days
    if out== "float":
        return timebetween
    else:
        print('There are ' + timebetween + 'days between the two dates')
    
    

    return None


# In[8]:


# problem 4
def reverse(in_list: list) -> list:
    reversed_list = []
    for item in in_list:
       reversed_list.insert(0, item)
    return reversed_list

#print(reverse(['a', 'b', 'c']))


# In[ ]:





# In[ ]:


def prob_k_heads(n: int, k: int) -> float:
    """
    Some docstrings.
    """

    return None

