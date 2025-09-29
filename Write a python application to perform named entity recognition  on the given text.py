#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import spacy 
spacy.cli.download('en_core_web_sm')  
nlp=spacy.load('en_core_web_sm')  
content=""" """
(/)
doc=nlp(content)  
for ent in doc.ents: 
print(ent.text,ent.start_char,ent.end_char,ent.label_)  
print("xyz")
(/)
from spacy import displacy  
displacy.render(doc,style="ent")  


# In[ ]:




