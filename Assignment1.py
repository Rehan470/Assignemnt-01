#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd


# In[ ]:


path = 'C:\\Users\\Rehan Bhatti\\Downloads\\jsrt_metadata.csv'


# In[ ]:


df = pd.read_csv(path)


# In[ ]:


df


# In[ ]:


import numpy as np
df.replace("?", np.nan, inplace=True)
df


# In[ ]:


df.isnull()


# In[ ]:


df.isnull().sum()


# In[ ]:


df.groupby('diagnosis')["state"].count()


# In[ ]:


import matplotlib as plt
from matplotlib import pyplot


# In[ ]:


plt.pyplot.hist(df.groupby('diagnosis')["study_id"].count())
pyplot.show()


# In[ ]:


df.groupby('diagnosis')["state"].count()


# In[ ]:


lbl = ['malignant','benign']
lbl2=['malignant']


# In[ ]:


df['state']=pd.cut(df['diagnosis'],labels=lbl)


# In[ ]:


df['diagnosis']=df['diagnosis'].astype('double')


# In[ ]:


plt.pie(df, labels = lbl2, startangle = 90)
plt.show() 


# In[ ]:


plt.pie(y, labels = lbl2, startangle = 90)
plt.show() 


# In[ ]:


lbl3=['male']
lbl4=['female']


# In[ ]:


plt.pie(df, labels = lbl3, startangle = 90)
plt.show() 


# In[ ]:


plt.pie(df, labels = lbl4, startangle = 90)
plt.show() 

