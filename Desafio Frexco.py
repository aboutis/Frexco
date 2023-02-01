#!/usr/bin/env python
# coding: utf-8

# In[200]:


import numpy as np
import pandas as pd 


# In[201]:


dados = pd.read_excel(r"C:\Users\biama\Downloads\Dados.xlsx") #dados das vendas


# In[202]:


dados.head()


# In[218]:


rolling_mean = dados['Vendas'].rolling(window=5).mean()


# In[219]:


rolling_mean = rolling_mean.fillna(dados['Vendas'].mean())


# In[220]:


dados['rolling_mean'] = rolling_mean


# In[223]:


forecast = pd.DataFrame(data={'date': dados['Data'][-5:], 'demand_forecast': np.round(dados['rolling_mean'][-5:])})


# In[224]:


print(forecast)


# In[ ]:




