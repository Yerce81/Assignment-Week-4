#!/usr/bin/env python
# coding: utf-8

# In[1]:


word = 'banana'
counter = {}
for letter in word:
    if letter == 'a':
        counter[letter] = counter.get(letter, 0) + 1
counter


# In[2]:


word = 'banana'
counter = {}
for letter in word:
    counter[letter] = counter.get(letter, 0) + 1
counter


# In[3]:


word = 'banana'
counter = {}
for a in word:
    counter['a'] = counter.get('a', 0) + 1
counter


# In[ ]:


# why is 'a': 6 ????


# In[ ]:





# In[4]:


palidrome = 'redivider'
palidrome[::-1]


# In[ ]:




