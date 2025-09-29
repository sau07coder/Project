#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install wordcloud')
(/)
get_ipython().system('pip install Wikipedia')
(/)
from wordcloud import WordCloud,STOPWORDS 
import matplotlib.pyplot as plt 
import wikipedia as wp 
page=wp.page("Artificial intelligence") 
page_content=page.content 
print(page_content)
(/)
def plot_wordcloud(wc): 
plt.axis("off") 
plt.figure(figsize=(10,10)) 
plt.imshow(wc) 
plt.show() 
wc=WordCloud(width=300,height=200,background_color="cyan",random_state=1,
 stopwords=STOPWORDS).generate(page_content) 
plot_wordcloud(wc)


# In[ ]:




