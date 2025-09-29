#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize,sent_tokenize 
nltk.download('punkt') 
nltk.download('stopwords') 
text=""" """ 
stopwords=set(stopwords.words("english")) 
words=word_tokenize(text) 
wordfreq=dict() 
 
for word in words: 
    word=word.lower() 
    if word in stopwords: 
        continue 
    if word in wordfreq: 
        wordfreq[word]+=1 
    else: 
        wordfreq[word]=1 
print(wordfreq)
(/)
sentences=sent_tokenize(text) 
sentrank=dict() 
for sentence in sentences: 
    for word,freq in wordfreq.items(): 
        if word in sentence.lower(): 
            if sentence in sentrank: 
                sentrank[sentence]+=freq 
            else: 
                sentrank[sentence]=freq 
sumrank=sum(sentrank.values()) 
averagerank=sumrank/len(sentrank) 
summary='' 
for sentence in sentences: 
    if((sentence in sentrank) and (sentrank[sentence]>1.2*averagerank)): 
        summary+=" "+sentence 
print(f"Summary:{summary}") 


# In[ ]:




