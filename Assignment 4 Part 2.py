#!/usr/bin/env python
# coding: utf-8

# In[1]:


from arcgis.gis import GIS


# In[2]:


gis = GIS()


# In[3]:


public_content = gis.content.search("Fire", item_type="Feature Layer", max_items=10)


# In[4]:


public_content


# In[8]:


from IPython.display import display
for item in public_content:
    display(item)


# In[9]:


example_item = public_content[1]
display(example_item)


# In[10]:


for lyr in example_item.layers:
    print(lyr.properties.name)


# In[18]:


m1 = gis.map('california')
m1


# In[22]:


m1.zoom_to_layer(example_item.layers)
m1.add_layer(example_item.layers)
m1 = gis.map('california')
m1


# In[ ]:




