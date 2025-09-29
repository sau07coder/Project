#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import nltk 
nltk.download('punkt') 
(/)
from nltk.tokenize import sent_tokenize, word_tokenize 
text="This is a simple text. mr.XYZ wants it be tokenized. It should ready by 3 p.m." 
sentences=sent_tokenize(text) 
words=word_tokenize(text) 
print(f"Sentences: {sentences}") 
print(f"Words: {words}") 
(/)
get_ipython().system('pip install pyPDF2')
(/)
import PyPDF2 
import os 
os.getcwd()
(/)
import PyPDF2 
from nltk.tokenize import sent_tokenize, word_tokenize 
pdffile = open(r"D:\sample.pdf", 'rb') 
pdfdata = PyPDF2.PdfReader(pdffile) 
page = pdfdata.pages[0] 
text = page.extract_text() 
if text: 
sentences = sent_tokenize(text) 
words = word_tokenize(text) 
print(f"Sentences: {sentences}") 
print(f"Words: {words}") 
else: 
print("No text could be extracted from the PDF.") 


# In[ ]:




