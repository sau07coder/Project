#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import nltk  
from nltk.corpus import stopwords 
nltk.download('stopwords')
(/)
def generateNGram(text,n=1): 
words=nltk.word_tokenize(text) 
words=[word for word in words if word.lower() not in 
set(stopwords.words('english'))] 
print(f"sentence after stop word removal {words}") 
temp=zip(*[words[i:]for i in range(0,n)]) 
ngram=[' '.join(ngram) for ngram in temp] 
return ngram 
generateNGram("my name is xyz my teacher name is maya maam she 
teaches us NLP",4)


# In[ ]:




