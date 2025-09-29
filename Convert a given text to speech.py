#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install gTTs ')
from gtts import gTTS  
mytext="Welcome to the world of Natural Language Processing"  
language="en"  
myobj=gTTS(text=mytext,lang=language,slow=False)  
myobj.save("nlpaudio.mp3") 
import os  
os.getcwd()


# In[ ]:




