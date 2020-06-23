#!/usr/bin/env python
# coding: utf-8

# In[41]:


# Pickling the data into a corpus for later use
lotr_script.to_pickle("lotr_corpus.plk")

# For my analysis, I have chosen to put it into a document term matrix as well. This will allow me to tokenize terms to 
# break down the text into words. For this particular analysis,  I have chosen to use CountVectorizer from sci-kit because 
# it allows me to tokenize terms and get rid of stop words that could change my analysis.
from sklearn.feature_extraction.text import CountVectorizer

count_vect = CountVectorizer(stop_words='english')
data_count_vect = count_vect.fit_transform(clean_script.script)
lotr_doc_matrix = pd.DataFrame(data_count_vect.toarray(), columns=count_vect.get_feature_names())
lotr_doc_matrix.index = clean_script.index
lotr_doc_matrix

# I will also pickle this data for later use
lotr_doc_matrix.to_pickle("lotr_doc_term.pkl")

# Here I will count the top 30 words with the count in the script, along with the top 15 words without the count.
import pandas as pd

data = pd.read_pickle('lotr_doc_term.pkl')
data = data.transpose()
data.head()

top_dict = {}
for c in data.columns:
    top = data[c].sort_values(ascending=False).head(30)
    top_dict[c]= list(zip(top.index, top.values))

print(top_dict)

for top_dict, top_words in top_dict.items():
    print(top_dict)
    print(', '.join([word for word, count in top_words[0:14]]))

# I will now utilize my document term matrix to run my sentiment analysis of my script
import pandas as pd

data = pd.read_pickle('lotr_doc_term.pkl')
data

# Create quick lambda functions to find the polarity and subjectivity of each routine
# I downloaded textblob through conda install -c conda-forge. 
import nltk
from textblob import TextBlob

pol = lambda x: TextBlob(x).sentiment.polarity
sub = lambda x: TextBlob(x).sentiment.subjectivity

data['polarity'] = pd.DataFrame(clean_script.script.apply(pol))
data['subjectivity'] = pd.DataFrame(clean_script.script.apply(sub))
data

# Here I will plot my results of what I found from running the script
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = [10, 8]

for index, word in enumerate(data.index):
    x = data.polarity.loc[word]
    y = data.subjectivity.loc[word]
    plt.scatter(x, y, color='green')
    plt.xlim(-.01, .12) 
    
plt.title('Sentiment Analysis', fontsize=20)
plt.xlabel('<---- Neg. ---- Pos. ---->', fontsize=15)
plt.ylabel('<-- Facts -------- Opinions -->', fontsize=15)

plt.show()


# In[ ]:




