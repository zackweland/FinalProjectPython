#!/usr/bin/env python
# coding: utf-8

# In[6]:


# To do the topic modeling, I will bring back in my document term matrix using the pandas and pickle
import pandas as pd
data = pd.read_pickle('lotr_doc_term.pkl')
data

# I will be doing a topic modeling known as LDA and importing the necessary modules to do so.
# matutils is used to create a corpus from a document term matrix, models is used for the analysis, and scipy.sparse is used to
# turn our document term matrix into a sparse matrix
from gensim import matutils, models
import scipy.sparse

# One of the required inputs for LDA in genism is a term-document matrix
lotr_term_doc_matrix = data.transpose()
lotr_term_doc_matrix.head()

# Here we turn our script in the term-document matrix into a gensim format
sparse_matrix = scipy.sparse.csr_matrix(lotr_term_doc_matrix)
lotr_corpus_genism = matutils.Sparse2Corpus(sparse_matrix)

# Now we read back in our document called 'count_vect' that we created before to create a dictionary of all the terms and 
# their locations in the tdm.
count_vect = pickle.load(open('count_vect.plk', 'rb'))
word_location = dict((x, y) for y, x in count_vect.vocabulary_.items())

# Having both the location and corpus allows us to run our topic modeling!

# Now that we have the corpus and word_location,we can specify two other parameters as well - 
# the number of topics and the number of passes.
lda_model = models.LdaModel(corpus=lotr_corpus_genism, id2word=word_location, num_topics=3, passes=80)
lda_model.print_topics()


# In[ ]:




