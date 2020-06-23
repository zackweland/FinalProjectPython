Project: Topic Modeling and Character Analysis of Lord of the Rings scripts

Goal of the project: For my project, I plan on doing a text analysis, a sentiment analysis and a topic modeling of the Lord of the Rings: The Fellowship of the Ring movie script. Being that I am currently reading the books again, my goal is to break down the movie script and see how well it matches up with my perception of the characters.

Data cleaning: I scraped my script for Lord of the Rings: The Fellowship of the Ring using the modules request, BeautifulSoup, and pickle. Request is used to send my HTTP request for my script, BeautifulSoup to parse through the data, and pickle to store my script into a file. After I imported my script into a file, I did the following tasks to clean up my script in order for Python to process my data: made text all lower case, removed punctuation, remove numerical values, removed common non-sensical text, tokenized text and removed stop words. This process took a few iterations before I was satisfied.

Sentiment analysis: I took the document term matrix I pickled in the data cleaning step and imported it into a new file. I then used TextBlob to do the analysis, imported it from conda install -c conda-forge, and created used lambda to create functions that measured both the subjectivity and polarity of the script. After finding my results, I then put it into a graph for analysis

Topic analysis:

Individual character analysis: To individually analyze each character, I picked out five characters (Frodo, Gandalf, Sam, Aragorn, and Boromir), copy and pasted their dialogues into a text document and did individual text analysis. I followed the same steps used in the data cleaning and sentiment analysis of the entire script.

Instructions on how to use the text: While I separated each individual step, I would run the code through the document I provide called "combined code", as this will reduce the hassle of trying to combine the different code files. I have included the different files in order to show the different steps I took throughout the process. Additionally, I will provide both .py and .ipynb files, depending on whether you use Spyder or Jupyter Notebook. 

Analysis and conclusions: I will provide these in a word document at the end of the files! These will include different graphs I created in order to better represent the analysis I did throughout the project.
