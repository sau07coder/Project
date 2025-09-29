#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import nltk 
nltk.download('brown') 
from nltk.corpus import brown 
#checking the file ids in the corpus 
print(f"File ids of Brown corpus is{brown.fileids()}")
(/)
ca01=brown.words("ca01") 
print(f"Words in ca01 are as follows\n{ca01}") 
(/)
print(f"ca01 has {len(ca01)}words") 
(/)
print(f"categories in Brown corpus are {brown.categories()}")
(/)
import nltk 
from nltk.corpus import brown 
print("Avg wordlen\tAvg Sentlen\tNumber of times each word appears on 
avg\tFileName") 
for fileid in brown.fileids(): 
num_chars = len(brown.raw(fileid)) 
num_words = len(brown.words(fileid)) 
num_sents = len(brown.sents(fileid)) 
num_vocab = len(set([w.lower() for w in brown.words(fileid)])) 
avg_word_len = num_chars / num_words 
avg_sent_len = num_words / num_sents 
avg_word_freq = num_words / num_vocab 
print(f"{avg_word_len:.2f}\t\t{avg_sent_len:.2f}\t\t{avg_word_freq:.2f}\t\t{fileid}
 ") 


# In[ ]:




