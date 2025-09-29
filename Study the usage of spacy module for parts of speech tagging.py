#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install spacy ')
import spacy
(/)
spacy.cli.download("en_core_web_sm") 
nlp = spacy.load("en_core_web_sm")
(/)
doc = nlp(u'I will google about facebook') 
for word in doc: 
    print(word.text, "--->", word.pos_, word.tag_, spacy.explain(word.tag_))


# In[ ]:




