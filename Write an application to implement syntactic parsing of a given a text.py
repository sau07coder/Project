#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import nltk 
from nltk.tokenize import word_tokenize 
grammar1 = nltk.CFG.fromstring(""" 
S -> VP 
VP -> V NP 
NP -> Det N 
Det -> 'that' 
N -> 'flight' 
V -> 'book' 
""") 
sentence = "book that flight" 
all_tokens = word_tokenize(sentence) 
print(all_tokens) 
parser = nltk.ChartParser(grammar1) 
for tree in parser.parse(all_tokens): 
print(tree) 
tree.draw()
(/)
import nltk 
from nltk.tokenize import word_tokenize 
grammar1 = nltk.CFG.fromstring(""" 
S -> NP VP 
NP -> Pronoun | Det N | Det N PP 
VP -> V NP | VP PP 
PP -> P NP 
Pronoun -> 'I' 
N -> 'bird' | 'balcony' 
V -> 'saw' 
Det -> 'a' | 'my' 
P -> 'in' 
""") 
sentence = "I saw a bird in my balcony" 
all_tokens = word_tokenize(sentence) 
print(all_tokens) 
parser = nltk.ChartParser(grammar1) 
for tree in parser.parse(all_tokens): 
print(tree) 
tree.draw()


# In[ ]:




