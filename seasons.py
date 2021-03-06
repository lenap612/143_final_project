import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 

path = '/data/Crime_Data_from_2010_to_2019.csv'
s = ['Winter', 'Spring', 'Summer', 'Fall']
c = ['lightskyblue','lightgreen','tomato','gold']

plt.style.use('fivethirtyeight')
df = pd.read_csv(path, parse_dates=['DATE OCC'])
count = df['DATE OCC'].value_counts()
df_count = pd.DataFrame(count.values,index=count.index, columns=['count']) # count for each day 
df_count['Years'] = df_count.index.year
df_count['Seasons'] = (df_count.index.month // 3) % 4 # 0: Dec, Jan, Feb
df2 = df_count.groupby([('Years'), ('Seasons')])['count'].sum().unstack(level=1)

# total crime cases for each season and each year 
ax = df2.plot.bar(color=c)
plt.legend(['Winter', 'Spring', 'Summer', 'Fall'], loc='upper right',bbox_to_anchor=(1.3, 1))
ax.set_ylabel('Crime Cases')
plt.title('Crime cases of each season from 2016 to 2021')
plt.show()

# total crime cases for each seasons from 2016 to 2020
df3 = df_count.groupby('Seasons')['count'].sum()
df3.index = ['Winter', 'Spring', 'Summer', 'Fall']
ax2 = df3.plot.bar(color=c)
plt.title('Total crime cases of each season from 2016 to 2021')
plt.show()

# trending for each year 
years = list(range(2010, 2022))
df['Seasons'] = (df['DATE OCC'].dt.month // 3) % 4 # 0: Dec, Jan, Feb
df['Years'] = df['DATE OCC'].dt.year
df4 = df.groupby([('Years'), ('Seasons'),('Crm Cd Desc')]).size().unstack(level=2)
top = 15

# top 15 types for each year and each season
for y in years:
  df_y = 'df' + str(y)
  df_y = df4.iloc[df4.index.get_level_values('Years') == y].droplevel('Years').fillna(0).transpose()

  for i in range(4):
    n = df_y.nlargest(top,i)[i].index.tolist()
    v = df_y.nlargest(top,i)[i].values
    temp = str(y) + 'Q'+ str(i)
    temp = pd.DataFrame({'count':v}, index=n)
    ax = temp.plot.bar(color=c[i])
    plt.title('Top 15 crime cases in ' + str(y) + ' ' + s[i])
    ax.get_legend().remove()
    plt.show()


# changes of top 15 for each year 
for y in years:
  df_y = 'df' + str(y)
  df_y = df4.iloc[df4.index.get_level_values('Years') == y].droplevel('Years').fillna(0).transpose()
  values = np.zeros((top,4))
  # changes over seasons
  feature = df_y.nlargest(top,0)[0].index.tolist()
  # display(feature)
  angles=np.linspace(0, 2*np.pi, 15, endpoint=False)

  for i in range(top):
    t = df_y.iloc[df_y.index.get_level_values('Crm Cd Desc') == feature[i]].values
    values[i,:] = t
  v0 = np.concatenate((values[:,0],[values[:,0][0]]))
  v1 = np.concatenate((values[:,1],[values[:,1][0]]))
  v2 = np.concatenate((values[:,2],[values[:,2][0]]))
  v3 = np.concatenate((values[:,3],[values[:,3][0]]))
  a = np.concatenate((angles,[angles[0]]))
  # labels = np.concatenate((feature,[feature[0]]))
  fig = plt.figure(figsize=(8,6), dpi=100)
  ax = fig.add_subplot(111, polar=True)
  ax.plot(a, v0, 'o-', color=c[0], linewidth=2)
  ax.plot(a, v1, 'o-', color=c[1], linewidth=2)
  ax.plot(a, v2, 'o-', color=c[2], linewidth=2)
  ax.plot(a, v3, 'o-', color=c[3], linewidth=2)
  plt.xticks(a[:-1], feature, size=7)
  plt.yticks([1000, 2000, 3000, 4000], ["1k", "2k", "3k",'4k'], color="grey", size=7)
  ax.set_title('Top 15 types of crime in '+ str(y))
  plt.legend(s, loc='upper right',bbox_to_anchor=(1.5, 1))
  ax.spines['polar'].set_visible(False)
  plt.show()


# 10 types for each season from 2010 to 2021
df5 = df.groupby([('Seasons'),('Crm Cd Desc')]).size().unstack(level=1).fillna(0).transpose()
df5['diff'] = abs(df5[0]-df5[2])  # difference between winter and summer, including most popular in winter and most popular in summer 
count = 9
values = np.zeros((count,4))
# changes over seasons
feature = df5.nlargest(count,'diff', keep='first').index.tolist()
angles=np.linspace(0, 2*np.pi, count, endpoint=False)
for i in range(count):
  t = df5.iloc[df5.index.get_level_values('Crm Cd Desc') == feature[i]].values
  values[i,:] = t[0][0:4]
v0 = np.concatenate((values[:,0],[values[:,0][0]]))
v1 = np.concatenate((values[:,1],[values[:,1][0]]))
v2 = np.concatenate((values[:,2],[values[:,2][0]]))
v3 = np.concatenate((values[:,3],[values[:,3][0]]))
a = np.concatenate((angles,[angles[0]]))
# labels = np.concatenate((feature,[feature[0]]))
fig = plt.figure(figsize=(8,6), dpi=100)
ax = fig.add_subplot(111, polar=True)
ax.plot(a, v0, 'o-', color=c[0], linewidth=2)
ax.plot(a, v1, 'o-', color=c[1], linewidth=2)
ax.plot(a, v2, 'o-', color=c[2], linewidth=2)
ax.plot(a, v3, 'o-', color=c[3], linewidth=2)
plt.xticks(a[:-1], feature, size=7)
plt.yticks([10000, 20000, 30000, 40000, 50000], ["10k", "20k", "30k",'40k','50k'], color="grey", size=7)
ax.set_title(str(count) + ' crime types have most seasonal difference from 2010 to 2021')
plt.legend(s, loc='upper right',bbox_to_anchor=(1.5, 1))
ax.spines['polar'].set_visible(False)
plt.show()

# top5 popular types for each season 

values = np.zeros((6,4))
# changes over seasons
feature0 = df5.nlargest(6,0, keep='first').index.tolist()
feature1 = df5.nlargest(6,1, keep='first').index.tolist()
feature2 = df5.nlargest(6,2, keep='first').index.tolist()
feature3 = df5.nlargest(6,3, keep='first').index.tolist()
angles=np.linspace(0, 2*np.pi, 6, endpoint=False)

for i in range(6):
  t0 = df5.iloc[df5.index.get_level_values('Crm Cd Desc') == feature0[i]].values
  t1 = df5.iloc[df5.index.get_level_values('Crm Cd Desc') == feature1[i]].values
  t2 = df5.iloc[df5.index.get_level_values('Crm Cd Desc') == feature2[i]].values
  t3 = df5.iloc[df5.index.get_level_values('Crm Cd Desc') == feature3[i]].values
  values[i,0] = t[0][0]
  values[i,1] = t[0][1]
  values[i,2] = t[0][2]
  values[i,3] = t[0][3]
v0 = np.concatenate((values[:,0],[values[:,0][0]]))
v1 = np.concatenate((values[:,1],[values[:,1][0]]))
v2 = np.concatenate((values[:,2],[values[:,2][0]]))
v3 = np.concatenate((values[:,3],[values[:,3][0]]))
a = np.concatenate((angles,[angles[0]]))

# top5 popular types in winter 
fig = plt.figure(figsize=(8,6), dpi=100)
ax = fig.add_subplot(111, polar=True)
ax.plot(a, v0, 'o-', color=c[0], linewidth=2)
plt.xticks(a[:-1], feature0, size=7)
plt.yticks([10000, 20000, 30000, 40000, 50000], ["10k", "20k", "30k",'40k','50k'], color="grey", size=7)
ax.set_title('6 crime types have most difference from 2010 to 2021')
plt.legend(s, loc='upper right',bbox_to_anchor=(1.5, 1))
ax.spines['polar'].set_visible(False)
plt.show()

# top5 popular types in spring 
fig = plt.figure(figsize=(8,6), dpi=100)
ax = fig.add_subplot(111, polar=True)
ax.plot(a, v1, 'o-', color=c[1], linewidth=2)
plt.xticks(a[:-1], feature1, size=7)
plt.yticks([10000, 20000, 30000, 40000, 50000], ["10k", "20k", "30k",'40k','50k'], color="grey", size=7)
ax.set_title('6 crime types have most difference from 2010 to 2021')
plt.legend(s, loc='upper right',bbox_to_anchor=(1.5, 1))
ax.spines['polar'].set_visible(False)
plt.show()

# top5 popular types in summer
fig = plt.figure(figsize=(8,6), dpi=100)
ax = fig.add_subplot(111, polar=True)
ax.plot(a, v2, 'o-', color=c[2], linewidth=2)
plt.xticks(a[:-1], feature2, size=7)
plt.yticks([10000, 20000, 30000, 40000, 50000], ["10k", "20k", "30k",'40k','50k'], color="grey", size=7)
ax.set_title('6 crime types have most difference from 2010 to 2021')
plt.legend(s, loc='upper right',bbox_to_anchor=(1.5, 1))
ax.spines['polar'].set_visible(False)
plt.show()

# top5 popular types in fall
fig = plt.figure(figsize=(8,6), dpi=100)
ax = fig.add_subplot(111, polar=True)
ax.plot(a, v3, 'o-', color=c[3], linewidth=2)
plt.xticks(a[:-1], feature3, size=7)
plt.yticks([10000, 20000, 30000, 40000, 50000], ["10k", "20k", "30k",'40k','50k'], color="grey", size=7)
ax.set_title('6 crime types have most difference from 2010 to 2021')
plt.legend(s, loc='upper right',bbox_to_anchor=(1.5, 1))
ax.spines['polar'].set_visible(False)
plt.show()
