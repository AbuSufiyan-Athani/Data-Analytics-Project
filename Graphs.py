#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


data=pd.read_csv("C:/Users/DELL/Documents/DA project/heart.csv")


# In[3]:


data


# In[4]:


data.isnull().sum()


# In[8]:


import seaborn as sns
plt.figure(figsize = (8,8))
plt.subplot(2,2,1)
sns.countplot('Sex', data = data, palette = 'rocket')


# In[9]:


plt.figure(figsize = (8,8))
plt.subplot(2,2,1)
sns.countplot('HeartDisease', data = data, palette = 'rocket')
plt.figure(figsize = (8,8))
plt.subplot(2,2,1)
sns.countplot('ChestPainType', data = data, palette = 'rocket')
plt.figure(figsize = (8,8))
plt.subplot(2,2,1)
sns.countplot('ExerciseAngina', data = data, palette = 'rocket')


# In[10]:


plt.figure(figsize = (15,8))
sns.heatmap(data.corr(), annot = True, cmap ='viridis')


# In[11]:


sns.jointplot(x = 'Age', y = 'Cholesterol', data = data, kind = 'hex')


# In[13]:


sns.pairplot(data, hue = 'Age')


# In[15]:


data['Age'].plot.box()


# In[16]:


age = 'Age'
Maxhr = 'MaxHR'
plt.scatter(age, Maxhr, data = data)
plt.xlabel('Age', fontsize = 15)
plt.ylabel('Max Heart Rate', fontsize = 15)
plt.title('Age v/s Max heart rate', fontsize = 15)


# In[17]:


age = 'Age'
Maxhr = 'RestingBP'
plt.scatter(age, Maxhr, data = data)
plt.xlabel('Age', fontsize = 15)
plt.ylabel('Resting Blood Pressure', fontsize = 15)
plt.title('Age v/s RestingBP', fontsize = 15)


# In[18]:


age = 'Age'
Maxhr = 'Cholesterol'
plt.scatter(age, Maxhr, data = data)
plt.xlabel('Age', fontsize = 15)
plt.ylabel('Cholesterol', fontsize = 15)
plt.title('Age v/s Cholesterol', fontsize = 15)


# In[26]:


data["Age"].hist(bins=6)


# In[27]:


data["RestingBP"].hist(bins=6)


# In[28]:


data["Cholesterol"].hist(bins=6)


# In[29]:


data["MaxHR"].hist(bins=6)


# In[ ]:





# In[32]:





# In[ ]:




