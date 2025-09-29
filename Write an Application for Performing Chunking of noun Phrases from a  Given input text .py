#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import nltk  
nltk.download("averaged_perceptron_tagger_eng")
(/)
nltk.download('punkt')
text="xyz is cunning as a fox " 
words=nltk.word_tokenize(text) 
print(words)
(/)
pos_tagged_words=nltk.pos_tag(words) 
print(pos_tagged_words)
(/)
grammar="NP:{<DT>?<JJ>*<NN>}" 
cp=nltk.RegexpParser(grammar) 
tree=cp.parse(pos_tagged_words) 
print(tree) 
tree.pretty_print() 


# In[ ]:




