#!/usr/bin/env python
# coding: utf-8

# In[19]:


import re
a='ujeghbg fay Ahkjknhqs e;k ip[w0ospk[w oi837y7 8756$$$^v]]'
b = re.sub(r'[^a-zA-Z0-9]+', '', a)
b


# In[16]:


c=re.findall(r'\w*y\w*', a)
c


# In[17]:


#для перевірки візьмемо n=3
d=re.findall(r'\b\w{3}\b', a)
d


# In[20]:


f=re.findall(r'\b[aAbB]\w*s\b', a)
f


# In[22]:


def collect_amounts(text):
    r = r'\d+(?:\.\d+)?'
    amounts = re.findall(r, text)
    return amounts
text = "first amount is $123.45, second amount is $400"
monetary_amounts = collect_amounts(text)
print(monetary_amounts)


# In[27]:


def collect_amounts(text):
    r = r'\d+(?:\.\d+)?'
    amounts = re.findall(r, text)
    for i in range(len(amounts)):
        amounts[i] = float(amounts[i])
    return amounts
text = "first amount is $123.45, second amount is $400"
monetary_amounts = collect_amounts(text)
print(monetary_amounts)
    


# In[26]:


def collect_amounts(text):
    r = r'\d+(?:\.\d+)?'
    amounts = re.findall(r, text)
    for i in range(len(amounts)):
        amounts[i] = float(amounts[i])
    return amountsz
text = "first amount is $123.45, second amount is $400"
monetary_amounts = collect_amounts(text)
s= sum(monetary_amounts)
print(s)


# In[34]:


import re

python_code = """
def factorial(n):
    # Base case
    if n == 0:
        return 1
    # Recursive case
    else:
        return n * factorial(n-1)

# Calculate factorial of 5
result = factorial(5)
print("Factorial of 5:", result)
"""

remove_comments = re.sub(r'#.*', '', python_code)
print(remove_comments)



# In[35]:


remove_blank_lines = re.sub(r'\n\s*\n', '\n', remove_comments)
print(remove_blank_lines)


# In[32]:


original_date = "yyyy-mm-dd"
#original_date='2020-04-18'
year, month, day = original_date.split('-')
new_date = day + '-' + month + '-' + year
print(new_date)

