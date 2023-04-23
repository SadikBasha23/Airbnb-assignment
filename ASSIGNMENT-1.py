#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv


# In[5]:


l=[]
with open("Airbnb_UK_2022.csv",'r') as csv_file:
    csv_reader=csv.reader(csv_file)
    for row in csv_reader:
        l.append(row)
        for col in row:
            print(col,end='\t')
        print()


# In[6]:


l


# In[15]:


def value_wise(col1,col2,col3,col4,col5,colwise,value):
    col1_index=l[0].index(col1)
    col2_index=l[0].index(col2)
    col3_index=l[0].index(col3)
    col4_index=l[0].index(col4)
    col5_index=l[0].index(col5)
    colwise_index=l[0].index(colwise)
    print(colwise," ",col1," ",col2," ",col3," ",col4," ",col5)
    print("-----------------------------------------------------------------------")
    for i in l:
        if value==i[colwise_index]:
            print(i[colwise_index],"    ",i[col1_index],"    ",i[col2_index],"    ",i[col3_index],"    ",i[col4_index],"    ",i[col5_index])
            print()


# In[16]:


value_wise('name','host_name','description','host_location','host_since','host_id','60302')


# In[17]:


value_wise('host_name','property_type','price','minimum_nights','maximum_nights','host_location','London')


# In[25]:


value_wise('room_type', 'accommodates', 'bathrooms_text', 'bedrooms', 'beds','property_type','rental unit')


# In[29]:


value_wise( 'review_scores_rating', 'review_scores_accuracy','review_scores_cleanliness', 'review_scores_checkin', 'review_scores_location','host_location', 'London')


# In[ ]:





# In[1]:


import pandas as pd
from warnings import filterwarnings
filterwarnings('ignore')


# In[2]:


data1=pd.read_csv("Airbnb_UK_2022.csv")


# In[3]:


data1.head()


# In[24]:


data1['property_type'].unique()


# In[7]:


data=data1.copy()


# In[8]:


data.shape


# In[10]:


data.size


# In[11]:


data.ndim


# In[12]:


data.columns


# In[47]:


data.info()


# In[13]:


data.isnull().sum()


# In[24]:


import ast


# In[29]:


li=[]
for i in range(len(data)):
    li.extend(ast.literal_eval(data['amenities'][i]))   


# In[30]:


li


# In[31]:


from collections import Counter


# In[33]:


count_amenities=Counter(li)


# In[34]:


count_amenities


# In[39]:


sort_amenities=sorted(count_amenities.items(), key=lambda x:x[1], reverse=True)


# In[41]:


for i in range(10):
    print(sort_amenities[i])
    


# In[42]:


data.groupby(['host_location'])[['price']].mean()


# In[43]:


data.groupby(['host_location'])[['review_scores_rating']].mean()


# In[50]:


data.groupby(['host_location'])[['review_scores_checkin']].mean()


# In[51]:


data.groupby(['room_type'])[['price']].mean()


# In[5]:


import matplotlib.pyplot as plt
import seaborn as sb


# In[55]:


g=data['bedrooms'].value_counts()


# In[59]:


plt.pie(g,labels=g.index,autopct='%.2f%%')
plt.title("Bedrooms proportion",fontweight="bold",fontsize=17)
plt.show();


# In[70]:


plt.bar(data["room_type"].value_counts().index,data["room_type"].value_counts())
plt.title("Count of room type",fontweight="bold",fontsize=17)
plt.show();


# In[8]:


plt.scatter(data['accommodates'],data['price'],edgecolor ="green")
plt.xlabel("accommodates")
plt.ylabel("Price")
plt.title("Accomodates VS Price",fontweight="bold",fontsize=17)
plt.show();


# In[143]:


import datetime
from datetime import datetime


# In[144]:


time_df=data[['host_since','price']]
time_df


# In[145]:


l=[]
for i in range(0,len(time_df)):
    l.append(time_df['host_since'][i].rsplit('-',1)[0]+'-20'+time_df['host_since'][i].rsplit('-',1)[-1])


# In[146]:


l


# In[147]:


time_df["host_since1"]=l


# In[148]:


time_df


# In[149]:


time_df.host_since1=pd.to_datetime(time_df.host_since1)


# In[150]:


time_df.info()


# In[153]:


time_df.drop(columns="host_since",inplace=True)


# In[154]:


time_df


# In[159]:


time_df=time_df.sort_values(by=['host_since1']).groupby(["host_since1"])[["price"]].sum().reset_index()
time_df


# In[164]:


t=1
plt.figure(figsize=(22,10))
for i in ['2019','2020','2021','2022']:
    plt.subplot(2,2,t)
    time_df[time_df['host_since1'].dt.strftime('%Y') == i]['price'].plot()
    plt.title(i,fontweight="bold",fontsize=17)
    t=t+1
    plt.tight_layout()
plt.show();


# In[165]:


g=data['room_type'].value_counts()
plt.pie(g,labels=g.index,autopct='%.2f%%')
plt.title("room_type proportion",fontweight="bold",fontsize=17)
plt.show();


# In[14]:


plt.scatter(data['review_scores_rating'],data['review_scores_accuracy'],edgecolor ="green")
plt.xlabel("review_scores_rating")
plt.ylabel("review_scores_accuracy ")
plt.title("review_scores_rating  VS review_scores_accuracy ",fontweight="bold",fontsize=17)
plt.show();


# In[ ]:




