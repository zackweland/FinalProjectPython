#!/usr/bin/env python
# coding: utf-8

# In[35]:


# Web scraping, pickle imports
import requests
from bs4 import BeautifulSoup
import pickle

# Scrapes script data from scrapsfromtheloft.com
def url_to_lotrscript(url):
# Gives me the script from https://www.councilofelrond.com/subject/the-fellowship-of-the-ring-2/
    webpage = requests.get(url).text
    soup = BeautifulSoup(webpage, "lxml")
    text = [p.text for p in soup.find(class_="post-content").find_all('p')]
    print(url)
    return text

# URL of LOTR: The Fellowship of the Ring Script
url_1 = ['https://www.councilofelrond.com/subject/the-fellowship-of-the-ring-2/']

# Name of script
lotr_script = 'script'


# In[36]:


# Request script from website
script = [url_to_lotrscript(x) for x in url_1]


# In[37]:


# Here I pickle my script and create a new directory for the script files
for character, lines in enumerate(lotr_script):
    with open("C:/Users/Zachary/Desktop/Python Class/Final Project/Pickled Data" + lines + ".txt", "wb") as file:
        pickle.dump(script[character], file)


# In[38]:


# Here we load up pickled files
data = {}
for character, lines in enumerate(lotr_script):
    with open("C:/Users/Zachary/Desktop/Python Class/Final Project/Pickled Data" + lines + ".txt", "rb") as file:
        data[character] = pickle.load(file)


# In[42]:


# Double check to make sure data has been loaded properly
data.keys()


# In[ ]:





# In[ ]:





# In[ ]:




