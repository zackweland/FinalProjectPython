Project: Topic Modeling and Character Analysis of Lord of the Rings scripts

Goal of the project: For my project, I plan on doing a text analysis, a sentiment analysis and a topic modeling of the Lord of the Rings: The Fellowship of the Ring movie script. Being that I am currently reading the books again, my goal is to break down the movie script and see how well it matches up with my perception of the characters.

Data cleaning: I scraped my script for Lord of the Rings: The Fellowship of the Ring using the modules request, BeautifulSoup, and pickle. Request is used to send my HTTP request for my script, BeautifulSoup to parse through the data, and pickle to store my script into a file. After I imported my script into a file, I did the following tasks to clean up my script in order for Python to process my data: made text all lower case, removed punctuation, remove numerical values, removed common non-sensical text, tokenized text and removed stop words. This process took a few iterations before I was satisfied.

Sentiment analysis: I took the document term matrix I pickled in the data cleaning step and imported it into a new file. I then used TextBlob to do the analysis, imported it from conda install -c conda-forge, and created used lambda to create functions that measured both the subjectivity and polarity of the script. After finding my results, I then put it into a graph for analysis.

Topic analysis: I took the genism module and decided to run Latent Dirichlet allocation (LDA), a type of topic modeling associated with genism. I imported my document term matrix, created both a corpus and dictionary of terms, and then ran my analysis. Since I was only looking through one script, I decided that only one topic would be necessary to analyze. 

Individual character analysis: I was not able to do this  unfortunately, but I have included an explanation as to why in my analysis and conclusion document.

Instructions on how to use the text: While I separated each individual step, I would run the code through the document I provide called "combined code", as this will reduce the hassle of trying to combine the different code files. I have included the different files in order to show the different steps I took throughout the process. Additionally, I will provide both .py and .ipynb files, depending on whether you use Spyder or Jupyter Notebook. As a note, when looking at the beginning combined code file, change where you're saving the script files to your own computer.

Analysis and conclusions: I will provide these in a word document called "Analysis and Conclusion" at the end of the repository! These will include different graphs I created in order to better represent the analysis I did throughout the project.
