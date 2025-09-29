#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install contractions')
(/)
get_ipython().system('pip install textblob')
(/)
import nltk  
import string  
import contractions  
from nltk.corpus import stopwords  
from nltk.tokenize import word_tokenize   
from textblob import TextBlob  
from nltk.stem import PorterStemmer 
from nltk.stem import WordNetLemmatizer 
Name   : Kishan Patel 
Roll No: TCS2526090 
Code: 
nltk.download('punkt')  
nltk.download('stopwords')  
nltk.download('wordnet')  
nltk.download('omw-1.4')
(/)
nltk.download('punkt_tab')
(/)
text="The big bron fox jumped over the lazy dog !!!! Wasn't it scary ???" 
  
expanded_text=contractions.fix(text)  
  
tokens=word_tokenize(expanded_text)  
  
tokens=[token.lower() for token in tokens]  
  
tokens=[token for token in tokens if token not in string.punctuation]  
  
stop_words=set(stopwords.words("english"))  
tokens=[token for token in tokens if token not in stop_words]  
  
corrected_tokens=[str(TextBlob(token).correct()) for token in tokens]  
  
stemmer=PorterStemmer()  
stemmed_tokens=[stemmer.stem(token) for token in corrected_tokens]  
  

lemmatizer=WordNetLemmatizer()  
lemmatized_tokens=[lemmatizer.lemmatize(token) for token in corrected_tokens]  
  
print(f"Original Text:{text}\n")  
print(f"Expanded Tex: {expanded_text}\n")  
print(f"Tokens: {tokens}\n")  
print(f"Corrected tokens: {corrected_tokens}\n")  
print(f"Stemmed tokens: {stemmed_tokens}\n")  
print(f"Lemmatized tokens: {lemmatized_tokens}\n")


# In[ ]:




