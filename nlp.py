#!/usr/bin/env python
# coding: utf-8

# #write a python program to implement n gram model of a given set

# In[1]:


import nltk 
from nltk.corpus import stopwords
nltk.download('stopwords')


# In[10]:


def generateNGram(text,n=1):
    words=nltk.word_tokenize(text)
    words=[word for word in words if word.lower() not in set(stopwords.words('english'))]
    print(f"sentence after stop word removal {words}")
    temp=zip(*[words[i:]for i in range(0,n)])
    ngram=[' '.join(ngram) for ngram in temp]
    return ngram

generateNGram("my name is YASh GUPTA my teacher name is maya maam she teaches us NLP",4)


    


# #study of a corpus "brown"

# #the brown corpus is a carefully selected collection of 1 million words of american english text and it comprises of 15 different genre news,fiction,
# #government
# 
# 

# In[3]:


import nltk
nltk.download('brown')
from nltk.corpus import brown
#checking the file ids in the corpus
print(f"File ids of Brown corpus is{brown.fileids()}")


# In[4]:


ca01=brown.words("ca01")
print(f"Words in ca01 are as follows\n{ca01}")


# In[5]:


print(f"ca01 has {len(ca01)}words")


# In[6]:


# categories n brown corpus
print(f"categories in Brown corpus are {brown.categories()}")


# In[7]:


import nltk
from nltk.corpus import brown


print("Avg wordlen\tAvg Sentlen\tNumber of times each word appears on avg\tFileName")

for fileid in brown.fileids():
    num_chars = len(brown.raw(fileid))
    num_words = len(brown.words(fileid))
    num_sents = len(brown.sents(fileid))
    num_vocab = len(set([w.lower() for w in brown.words(fileid)]))
    avg_word_len = num_chars / num_words
    avg_sent_len = num_words / num_sents
    avg_word_freq = num_words / num_vocab
    print(f"{avg_word_len:.2f}\t\t{avg_sent_len:.2f}\t\t{avg_word_freq:.2f}\t\t{fileid}")


# In[ ]:




