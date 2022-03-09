#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import squarify
from wordcloud import WordCloud

plt.style.use('fivethirtyeight')
year=["2010","2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021"]


# In[3]:


data=pd.read_csv("data/Crime_Data_from_2010_to_2019.csv")
data.info()


# In[25]:


weapon.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)


# In[4]:


result=pd.read_csv("data/result.csv")
result=result.set_index("Year",drop=True)
result.columns


# In[5]:


gun=pd.read_csv("data/gun_crime.csv")
gun.info()


# In[6]:


rate_list=[result.columns[1],result.columns[5]]
s_perday_list=[result.columns[2],result.columns[3],result.columns[4]]
g_perday_list=[result.columns[6],result.columns[7],result.columns[8]]
w_perday_list=[result.columns[9],result.columns[10]]
day_rate_list=[result.columns[-1],result.columns[-2],result.columns[-3],result.columns[-4],result.columns[-5],result.columns[-6],result.columns[-7],]


# Due to the lack of some crime data in 2012 and 2016, our statistical plot has some flaws, but this doesn't affect the statistics of some specific kinds of crime rates, because these crimes account for a certain proportion of all cases. Here we compare the rates of severe crime and gun crime. Severe crimes are derived from the Los Angeles Police Department's definition of cases that include HOMICIDE, RAPE, ROBBERY and AGGRESSIVE ASSAULTS. Gun crime refers to the criminal suspect's weapons containing various types of guns. 
# In the figure, we can see that the proportion of severe crimes has fluctuated and increased, and only in 2013 there has been a large decline (possibly related to the reduction of the felony threshold by California Proposition 47). The proportion of gun crime has not fluctuated significantly.

# In[18]:


result[rate_list].plot(ylim=0,figsize=(10,8))
plt.title('Severe&Gun Crime Rate Variation',fontsize=15)


# The figure below shows the average number of severe crime cases on each day, and the comparison of the average cases number on weekdays and weekends respectively. It can be seen that there is a significant increase in serious crime on weekends.

# In[8]:


result[s_perday_list].plot(kind="bar",figsize=(20,10))
plt.title('Severe Crime Data',fontsize=20)


# Likewise, gun crime also rose significantly over the weekends.

# In[9]:


result[g_perday_list].plot(kind="bar",figsize=(20,10))
plt.title('Gun Crime Data',fontsize=20)


# In[10]:


result[w_perday_list].plot(kind="bar",figsize=(20,10))
plt.title('Crime Count on Weekdays/Weekends',fontsize=20)


# If we divide the day into seven parts, each occupying three to four hours, it can be seen that the time of day when crime occurs most is afternoon and dust. This may be because people get off work at this time, and there are the most pedestrians. We can see that there are not many crimes at night, which is contrary to our impression of "It's more dangerous at night". This may be because there are very few pedestrians at night. The volume of these crimes is already scary enough that no one wants to be the victim. 

# In[11]:


data['DAYTIME'].value_counts().plot.pie(figsize=(15,8),autopct='%.2f',explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1))
plt.title('Crime Count on day time',fontsize = 20)
plt.xticks(rotation = 90)
plt.show()


# In[19]:


result[day_rate_list].plot(figsize=(15,10))
plt.legend(loc=2, bbox_to_anchor=(1,1),borderaxespad=0)
plt.title('Crime Rate Variation on Daytime',fontsize=20)


# We can see that the most commonly used crime guns are hand guns and simulated guns such as air guns. It is not difficult to understand that hand guns are used the most because of their portability, but why are there so many simulatyed guns? Maybe the suspect just wanted to scare the others at first, and didn't intend to cause harm, but pulled the trigger on impulse and committed the crime. 

# In[13]:


gun["Weapon Desc"].value_counts().iloc[:5].sort_values().plot(kind='barh')
plt.title('5 Most-Used Weapon in Gun Crime',fontsize=15)


# This is the proportion of the 20 most commonly used weapons. Most people will use their bodies to attack each other in the fight, causing harm to others and may also hurt themselves. This is an irrational behavior. Hate can make people impulsive and act stupidly. 

# In[30]:


tree=data['Weapon Desc'].value_counts().head(20)   
color=plt.cm.magma(np.linspace(0,1,15))
plt.style.use('fivethirtyeight')
squarify.plot(sizes=tree.values,label=tree.index,alpha=0.7,color=color)
plt.title('20 Most-Used Weapon in All Crime',fontsize=20)
plt.axis('off')


# In[ ]:




