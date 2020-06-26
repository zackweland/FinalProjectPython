#!/usr/bin/env python
# coding: utf-8

# In[94]:


# Here I open my character script and create a list to be associated with the script

file_script = open("Frodo Script.txt", "rb")
# Check to make sure file loaded properly: 
file_script = file_script.read()

char_script = ["char_script"]

import pickle
for key, value in enumerate(char_script):
     with open("C:/Users/Zachary/Desktop/Python Class/Final Project/Pickled Data/" + value + ".txt", "wb") as file:
            pickle.dump(file_script[key], file)

data = {}
for key, value in enumerate(char_script):
    with open("C:/Users/Zachary/Desktop/Python Class/Final Project/Pickled Data/" + value + ".txt", "rb") as file:
        data[value] = pickle.load(file)
        
data.keys()
file_script


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




