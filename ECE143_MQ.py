#!/usr/bin/env python
# coding: utf-8

from collections import defaultdict
from wordcloud import WordCloud
from collections import Counter
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

data = pd.read_csv("D:/ECE143/Project/Crime_Data_from_2010_to_2019.csv")

print(data.shape)

data.info()

data_1 = pd.read_csv("D:/ECE143/Project/Crime_Data_from_2010_to_2019.csv",usecols=[0,2,3,4,5,8,9,11,12,13,14,15,19,20,24])

print(data_1.shape)

data_1 = data_1.dropna()

rec_num=list(data_1['DR_NO'])
data_1['DateTimeValues'] = pd.to_datetime(data_1['DATE OCC'])
data_1['year'] = data_1['DateTimeValues'].dt.year
data_1['month'] = data_1['DateTimeValues'].dt.month
data_1['day'] = data_1['DateTimeValues'].dt.day
year = list(data_1['year'])
month = list(data_1['month'])
day = list(data_1['day'])
time_occ=list(data_1['TIME OCC'])
area_name=list(data_1['AREA NAME'])
crm_cd=list(data_1['Crm Cd'])
crm_dec=list(data_1['Crm Cd Desc'])
vict_age=list(data_1['Vict Age'])
vict_sex=list(data_1['Vict Sex'])
vict_descent=list(data_1['Vict Descent'])
pre_cd=list(data_1['Premis Cd'])
pre_dec=list(data_1['Premis Desc'])
sta_dec=list(data_1['Status Desc'])
crm_cd=list(data_1['Crm Cd 1'])
loc=list(data_1['LOCATION'])


Crm_Dec_Dict = defaultdict(set)

Crm_Dec_List = []

for i in range(len(crm_dec)):
    crm_dec_1 = []
    str1 = " - "
    if str1 in crm_dec_1:
        crm_dec_1.replace(str1, " ")
    crm_dec_1 = crm_dec[i].split(",")
    Crm_Dec_Dict[rec_num[i]].add(crm_dec_1[0])
    Crm_Dec_List.append(crm_dec_1[0])

print(Crm_Dec_Dict[rec_num[0]])


Crm_Dec_wordcloud = ",".join(Crm_Dec_List)

word_cloud = WordCloud(font_path="simsun.ttc", 
                       background_color="white") 
word_cloud.generate(Crm_Dec_wordcloud)

plt.subplots(figsize=(12,8))
plt.imshow(word_cloud)
plt.axis("off")

years = [2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]

crm_dec_years = defaultdict(list)
for j in range(len(years)):
    for i in range(len(year)): 
        if year[i] == years[j]:
            crm_dec_years[years[j]].append(Crm_Dec_List[i])



plt.style.use('fivethirtyeight')
title_year = "25 Most Happening Crime from 2010 to 2021"
plt.title(title_year)
plt.xlabel('Crime Type')
plt.ylabel('Number of Cases')
crm_dec_dict = Counter(Crm_Dec_List)
crm_dec_dict_1 = crm_dec_dict.most_common(25)
a1,b1 = zip(*crm_dec_dict_1)
crm_dec_x = list(a1)
crm_dec_y = list(b1)
plt.xticks(rotation = 270)
plt.bar(crm_dec_x, crm_dec_y)

plt.show()

print(crm_dec_x)

crm_dec_top_25 = defaultdict(list)

for j in range(len(crm_dec_x)):
    for i in range(len(year)): 
        if Crm_Dec_List[i] == crm_dec_x[j]:
            crm_dec_top_25[crm_dec_x[j]].append(year[i])

crm_dec_top_25_dict_x = defaultdict(list)
crm_dec_top_25_dict_y = defaultdict(list)

for i in range(len(crm_dec_x)):
    x,y = zip(*sorted(Counter(crm_dec_top_25[crm_dec_x[i]]).items()))
    crm_dec_top_25_dict_x[crm_dec_x[i]] = list(x)
    crm_dec_top_25_dict_y[crm_dec_x[i]] = list(y)

plt.figure(figsize=(35, 20))
plt.style.use('fivethirtyeight')
palette = plt.get_cmap('Set1')

plt.xlim(2009,2021)
plt.ylim(0,22500)
maker = ['.-',',-','o-','v-','^-','<-','>-','1-','2-','3-','4-','s-','p-','*-','h-','H-','+-','x-','D-','d-','|-','_-','.-',',-','o-']

for i in range(len(crm_dec_x)):
    plt.plot(crm_dec_top_25_dict_x[crm_dec_x[i]], crm_dec_top_25_dict_y[crm_dec_x[i]],maker[i],linewidth=2,label=crm_dec_x[i])
plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.) 
plt.xlabel('Year') 
plt.ylabel("Number of Cases") 
plt.title("25 Most Happening Crime in LA from 2010 to 2021")

plt.savefig('plot1.png',bbox_inches='tight',transparent = True)

plt.figure(figsize=(20,10))
plt.style.use('fivethirtyeight')
palette = plt.get_cmap('Set1')

plt.xlim(2009,2021)
plt.ylim(0,22500)

for i in [1,2,3,4,10,12,13,14,19,24]:
    plt.plot(crm_dec_top_25_dict_x[crm_dec_x[i]], crm_dec_top_25_dict_y[crm_dec_x[i]],maker[i],linewidth=2,label=crm_dec_x[i])
    
plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.) 
plt.xlabel('Year')
plt.ylabel("Number of Cases") 
plt.title("10 Most Happening Crime Related to Larceny in LA from 2010 to 2021")

plt.savefig('plot2.png',bbox_inches='tight',transparent = True)

plt.figure(figsize=(15,8))
plt.style.use('fivethirtyeight')
palette = plt.get_cmap('Set1')

for i in [0,9]:
    plt.plot(crm_dec_top_25_dict_x[crm_dec_x[i]], crm_dec_top_25_dict_y[crm_dec_x[i]],maker[i],linewidth=2,label=crm_dec_x[i])
    
plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.) 
plt.xlabel('Year') 
plt.ylabel("Number of Cases") 
plt.title("BURGLARY & LARCENY VS ROBBERY Crime in LA from 2010 to 2021")

plt.savefig('plot3.png',bbox_inches='tight',transparent = True)

plt.figure(figsize=(15,8))
plt.style.use('fivethirtyeight')
palette = plt.get_cmap('Set1')

plt.xlim(2009,2021)
plt.ylim(0,22500)

for i in [3,10,12,13,14,24]:
    plt.plot(crm_dec_top_25_dict_x[crm_dec_x[i]], crm_dec_top_25_dict_y[crm_dec_x[i]],maker[i],linewidth=2,label=crm_dec_x[i])

plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.) 
plt.xlabel('Year') 
plt.ylabel("Number of Cases") 
plt.title("Crime Related to Larceny in LA from 2010 to 2021")

plt.savefig('plot4.png',bbox_inches='tight',transparent = True)

plt.figure(figsize=(15,8))
plt.style.use('fivethirtyeight')
palette = plt.get_cmap('Set1')

for i in [4,19,23]:
    plt.plot(crm_dec_top_25_dict_x[crm_dec_x[i]], crm_dec_top_25_dict_y[crm_dec_x[i]],maker[i],linewidth=2,label=crm_dec_x[i])
    
plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.) 
plt.xlabel('Year') 
plt.ylabel("Number of Cases") 
plt.title("THEFT OF IDENTITY & DOCUMENT FORGERY & BUNCO in LA from 2010 to 2021")

plt.savefig('plot5.png',bbox_inches='tight',transparent = True)

plt.figure(figsize=(20,10))
plt.style.use('fivethirtyeight')
palette = plt.get_cmap('Set1')

for i in [5,22]:
    plt.plot(crm_dec_top_25_dict_x[crm_dec_x[i]], crm_dec_top_25_dict_y[crm_dec_x[i]],maker[i],linewidth=2,label=crm_dec_x[i])
    
plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.) 
plt.xlabel('Year') 
plt.ylabel("Number of Cases") 
plt.title("INTIMATE PARTNER - SIMPLE ASSAULT & AGGRAVATED ASSAULT in LA from 2010 to 2021")

plt.savefig('plot6.png',bbox_inches='tight',transparent = True)

plt.figure(figsize=(20,10))
plt.style.use('fivethirtyeight')
palette = plt.get_cmap('Set1')

plt.plot(crm_dec_top_25_dict_x[crm_dec_x[15]], crm_dec_top_25_dict_y[crm_dec_x[15]],maker[15],linewidth=2,label=crm_dec_x[15])

plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.) 
plt.xlabel('Year')
plt.ylabel("Number of Cases") 
plt.title("TRESPASSING in LA from 2010 to 2021")

plt.savefig('plot17.png',bbox_inches='tight',transparent = True)

plt.figure(figsize=(20,10))
plt.style.use('fivethirtyeight')
palette = plt.get_cmap('Set1')

plt.xlim(2009,2021)
plt.ylim(0,22500)

for i in [2,5,6,7,8,9,11,13,15,21,22,24]:
    plt.plot(crm_dec_top_25_dict_x[crm_dec_x[i]], crm_dec_top_25_dict_y[crm_dec_x[i]],maker[i],linewidth=2,label=crm_dec_x[i])
    
plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.) 
plt.xlabel('Year')
plt.ylabel("Number of Cases")
plt.title("Crime Related to TRESPASSING in LA from 2010 to 2021")

plt.savefig('plot8.png',bbox_inches='tight',transparent = True)

plt.figure(figsize=(15,8))
plt.style.use('fivethirtyeight')
palette = plt.get_cmap('Set1')

for i in [0,5,7,11,21,22]:
    plt.plot(crm_dec_top_25_dict_x[crm_dec_x[i]], crm_dec_top_25_dict_y[crm_dec_x[i]],maker[i],linewidth=2,label=crm_dec_x[i])
    
plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.) 
plt.xlabel('Year') 
plt.ylabel("Number of Cases") 
plt.title("Crime Related to BATTERY in LA from 2010 to 2021")

plt.savefig('plot9.png',bbox_inches='tight',transparent = True)

plt.figure(figsize=(15,8))
plt.style.use('fivethirtyeight')
palette = plt.get_cmap('Set1')

plt.plot(crm_dec_top_25_dict_x[crm_dec_x[7]], crm_dec_top_25_dict_y[crm_dec_x[7]],maker[7],linewidth=2,label=crm_dec_x[7])

plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.) 
plt.xlabel('Year') 
plt.ylabel("Number of Cases")
plt.title("ASSAULT WITH DEADLY WEAPON in LA from 2010 to 2021")

plt.savefig('plot10.png',bbox_inches='tight',transparent = True)

# N/A
plt.figure(figsize=(15,8))
plt.style.use('fivethirtyeight')
palette = plt.get_cmap('Set1')

for i in [6,8]:
    plt.plot(crm_dec_top_25_dict_x[crm_dec_x[i]], crm_dec_top_25_dict_y[crm_dec_x[i]],maker[i],linewidth=2,label=crm_dec_x[i])
    
plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.) 
plt.xlabel('Year') 
plt.ylabel("Number of Cases")
plt.title("VANDALISM in LA from 2010 to 2021")

plt.savefig('plot11.png',bbox_inches='tight',transparent = True)

#Only RESTRAINING ORDER
plt.figure(figsize=(15,8))
plt.style.use('fivethirtyeight')
palette = plt.get_cmap('Set1')

for i in [16,17,18,19,20]:
    plt.plot(crm_dec_top_25_dict_x[crm_dec_x[i]], crm_dec_top_25_dict_y[crm_dec_x[i]],maker[i],linewidth=2,label=crm_dec_x[i])
    
plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.) 
plt.xlabel('Year')
plt.ylabel("Number of Cases")
plt.title("Other Most Happening Crime in LA from 2010 to 2021")

plt.savefig('plot12.png',bbox_inches='tight',transparent = True)

plt.figure(figsize=(15,8))
plt.style.use('fivethirtyeight')
palette = plt.get_cmap('Set1')

for i in [18,20,5,22]:
    plt.plot(crm_dec_top_25_dict_x[crm_dec_x[i]], crm_dec_top_25_dict_y[crm_dec_x[i]],maker[i],linewidth=2,label=crm_dec_x[i])
    
plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.) 
plt.xlabel('Year') 
plt.ylabel("Number of Cases")
plt.title("Crime Related to RESTRAINING ORDER in LA from 2010 to 2021")

plt.savefig('plot13.png',bbox_inches='tight',transparent = True)


# Vict Age

rec_num=list(data_1['DR_NO'])
data_1['DateTimeValues'] = pd.to_datetime(data_1['DATE OCC'])
data_1['year'] = data_1['DateTimeValues'].dt.year
data_1['month'] = data_1['DateTimeValues'].dt.month
data_1['day'] = data_1['DateTimeValues'].dt.day
year = list(data_1['year'])
month = list(data_1['month'])
day = list(data_1['day'])
time_occ=list(data_1['TIME OCC'])
area_name=list(data_1['AREA NAME'])
crm_cd=list(data_1['Crm Cd'])
crm_dec=list(data_1['Crm Cd Desc'])
vict_age=list(data_1['Vict Age'])
vict_sex=list(data_1['Vict Sex'])
vict_descent=list(data_1['Vict Descent'])
pre_cd=list(data_1['Premis Cd'])
pre_dec=list(data_1['Premis Desc'])
sta_dec=list(data_1['Status Desc'])
crm_cd=list(data_1['Crm Cd 1'])
loc=list(data_1['LOCATION'])

vict_sex_nonzero = []
vict_age_nonzero = []
year_nonzero = []
month_nonzero = []

for i in range(len(vict_age)):
    if vict_age != 0:
        vict_sex_nonzero.append(vict_sex[i])
        vict_age_nonzero.append(vict_age[i])
        year_nonzero.append(year[i])
        month_nonzero.append(month[i])

vict_sex_m = []
vict_sex_fm = []
for i in range(len(year)): 
    if vict_sex_nonzero[i] == 'M':
        vict_sex_m.append(year[i])
    elif vict_sex_nonzero[i] == 'F':
        vict_sex_fm.append(year[i])

vict_sex_m_dict = Counter(vict_sex_m)
vict_sex_m_dict_1 =sorted(vict_sex_m_dict.items())
x,y = zip(*vict_sex_m_dict_1)
vict_sex_m_dict_x = list(x)
vict_sex_m_dict_y = list(y)

vict_sex_fm_dict = Counter(vict_sex_fm)
vict_sex_fm_dict_1 =sorted(vict_sex_fm_dict.items())
#crm_dec_top_1_dict_1 = crm_dec_top_1_dict.most_common()
x,y = zip(*vict_sex_fm_dict_1)
vict_sex_fm_dict_x = list(x)
vict_sex_fm_dict_y = list(y)



mpl.rc('font', family='SimHei', weight='bold')
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(15,8))
vict_sex_fm_dict_x.reverse()
x = np.arange(12)
y = vict_sex_m_dict_y
y1 = vict_sex_fm_dict_y
bar_width = 0.35
tick_label = list(reversed(vict_sex_fm_dict_x))

plt.barh(x, y, bar_width, align="center", color="c",label="Male", alpha=0.5)
plt.barh(x+bar_width, y1, bar_width, align="center", color="b",label="Female", alpha=0.5)

plt.xlabel("Number of Cases")
plt.ylabel("Year")

plt.yticks(x+bar_width/2, tick_label)

plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.) 
plt.title("Victims' Gender VS Number of Cases in LA from 2010 to 2021")

plt.show()

vict_age_1 = [] #children
vict_age_2 = [] #young adults
vict_age_3 = [] #middle age adults
vict_age_4 = [] #elderly age adults
vict_age_5 = [] #senile age adults
vict_age_6 = [] #long-livers
for i in range(len(year)): 
    if vict_age_nonzero[i] >= 0 and vict_age_nonzero[i]<=17:
        vict_age_1.append(year[i])
    elif vict_age_nonzero[i] >= 18 and vict_age_nonzero[i]<=44:
        vict_age_2.append(year[i])
    elif vict_age_nonzero[i] >= 45 and vict_age_nonzero[i]<=59:
        vict_age_3.append(year[i])
    elif vict_age_nonzero[i] >= 60 and vict_age_nonzero[i]<=74:
        vict_age_4.append(year[i])
    elif vict_age_nonzero[i] >= 75 and vict_age_nonzero[i]<=89:
        vict_age_5.append(year[i])
    elif vict_age_nonzero[i] >= 90:
        vict_age_6.append(year[i])

x,y = zip(*sorted(Counter(vict_age_1).items()))
vict_age_1_dict_x = list(x)
vict_age_1_dict_y = list(y)

x,y = zip(*sorted(Counter(vict_age_2).items()))
vict_age_2_dict_x = list(x)
vict_age_2_dict_y = list(y)

x,y = zip(*sorted(Counter(vict_age_3).items()))
vict_age_3_dict_x = list(x)
vict_age_3_dict_y = list(y)

x,y = zip(*sorted(Counter(vict_age_4).items()))
vict_age_4_dict_x = list(x)
vict_age_4_dict_y = list(y)

x,y = zip(*sorted(Counter(vict_age_5).items()))
vict_age_5_dict_x = list(x)
vict_age_5_dict_y = list(y)

x,y = zip(*sorted(Counter(vict_age_6).items()))
vict_age_6_dict_x = list(x)
vict_age_6_dict_y = list(y)



pic2 = plt.figure(figsize=(8,8),dpi=80)

all_vict_age = []
for i in range(len(vict_age_1_dict_x)):
    all_vict_age.append(str(vict_age_1_dict_y[i]))
    all_vict_age.append(str(vict_age_2_dict_y[i]))
    all_vict_age.append(str(vict_age_3_dict_y[i]))
    all_vict_age.append(str(vict_age_4_dict_y[i]))
    all_vict_age.append(str(vict_age_5_dict_y[i]))
    all_vict_age.append(str(vict_age_6_dict_y[i]))



plt.figure(figsize=(15,15))
labels=['Children','Young Age', 'Middle Age', 'Elderly Age', 'Senile Age', 'Long-livers']
age_2010=all_vict_age[0:6]
age_2011=all_vict_age[6:12]
age_2012=all_vict_age[12:18]
age_2013=all_vict_age[18:24]
age_2014=all_vict_age[24:30]
age_2015=all_vict_age[30:36]
age_2016=all_vict_age[36:42]
age_2017=all_vict_age[42:48]
age_2018=all_vict_age[48:54]
age_2019=all_vict_age[54:60]
age_2020=all_vict_age[60:66]
age_2021=all_vict_age[66:72]
bottom3 = []
bottom4 = []
bottom5 = []
bottom6 = []

plt.bar(vict_age_1_dict_x, vict_age_1_dict_y,align="center", color="#66c2a5",tick_label=vict_age_1_dict_x, label='Children (0-17)')
plt.bar(vict_age_2_dict_x, vict_age_2_dict_y, align="center", color="#8da0cb", bottom=vict_age_1_dict_y, label='Young Age (18-44)')
for i in range(0, len(vict_age_2_dict_y)):
    a = vict_age_1_dict_y[i] + vict_age_2_dict_y[i]
    bottom3.append(a)
plt.bar(vict_age_3_dict_x, vict_age_3_dict_y, align="center", color="#0066cc", bottom=bottom3, label='Middle Age (45-59)')
for i in range(0, len(vict_age_2_dict_y)):
    a = vict_age_1_dict_y[i] + vict_age_2_dict_y[i] +vict_age_3_dict_y[i]
    bottom4.append(a)
plt.bar(vict_age_4_dict_x, vict_age_4_dict_y, align="center", color="#ccffff", bottom=bottom4, label='Elderly Age (60-74)')
for i in range(0, len(vict_age_2_dict_y)):
    a = vict_age_1_dict_y[i] + vict_age_2_dict_y[i] +vict_age_3_dict_y[i]+vict_age_4_dict_y[i]
    bottom5.append(a)
plt.bar(vict_age_5_dict_x, vict_age_5_dict_y, align="center", color="#ffff99", bottom=bottom5, label='Senile Age (75-89)')
for i in range(0, len(vict_age_2_dict_y)):
    a = vict_age_1_dict_y[i] + vict_age_2_dict_y[i] +vict_age_3_dict_y[i]+vict_age_4_dict_y[i]+vict_age_5_dict_y[i]
    bottom6.append(a)
plt.bar(vict_age_6_dict_x, vict_age_6_dict_y, align="center", color="#000080", bottom=bottom6, label='Long-livers (over 90)')

plt.xlabel("Year")
plt.ylabel("Number of Cases")
plt.title("Victims' Age VS Number of Cases in LA from 2010 to 2021")

plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.)

plt.show()

plt.style.use('fivethirtyeight')
plt.figure(figsize=(50,17))

crm_dec_top15_years_dict_x = defaultdict(list)
crm_dec_top15_years_dict_y = defaultdict(list)

for i in range(len(years)):
    plt.subplot(2,6,i+1)
    ax = plt.gca()
    a,b = zip(*Counter(crm_dec_years[years[i]]).most_common(15))
    crm_dec_top15_years_dict_x[years[i]] = list(a)
    crm_dec_top15_years_dict_y[years[i]] = list(b)
    plt.xticks(rotation = 270)
    plt.bar(crm_dec_top15_years_dict_x[years[i]], crm_dec_top15_years_dict_y[years[i]])
    ax.set_xlabel('Crime Type')
    ax.set_ylabel('Number of Cases')
    title = "15 Most Happening Crime in "+str(years[i])
    ax.set_title(title)

plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                wspace=0.1, hspace=1.8)

plt.savefig('plot14.png',bbox_inches='tight',transparent = True)



