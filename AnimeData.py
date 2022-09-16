#!/usr/bin/env python
# coding: utf-8

# In[4]:


Dataset="/home/etherious-mi/Downloads/archive/Anime.csv"


# In[5]:


import pandas as pd


# In[6]:


anime_df = pd.read_csv(Dataset)


# In[7]:


anime_df


# In[8]:


print("Number of rows: ", len(anime_df))
print("Number of columns: ", len(anime_df.columns))


# In[9]:


anime_df.axes


# In[10]:


anime_df.columns.values


# In[11]:


anime_df.loc[20]


# In[12]:


anime_df.loc[anime_df[' rank']==0]


# In[13]:


sum(anime_df[' rank']==0)


# In[14]:



anime_df.dropna(inplace=True)


anime_df.drop(anime_df.index[anime_df[' rank']==0], inplace=True)


# In[15]:


anime_df


# In[16]:


anime_df.drop(columns=[' name', ' title_synonyms', ' status', ' airing', ' aired', ' scored_by', ' members',' synopsis', ' background', ' related'], axis=1)


# In[17]:


anime_new_df=anime_df.drop(columns=[' name', ' title_synonyms', ' status', ' airing', ' aired', ' scored_by', ' members',' synopsis', ' background', ' related'], axis=1)
anime_new_df


# In[18]:


print("Update df (row): ", len(anime_new_df))
print("Update df (column)", len(anime_new_df.columns))


# In[19]:


anime_new_df.head(5)


# In[20]:


anime_new_df.tail(5)


# In[21]:



anime_new_df.sort_values(' rank').head(30)


# In[22]:




anime_new_df.sort_values(' rank', ascending=False).head(30)


# In[23]:


anime_new_df.sort_values(' popularity', ascending=True).head(30)


# In[24]:



import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[25]:


plt.plot(anime_new_df[' score'])


# In[26]:


rank=anime_new_df[' rank']
score=anime_new_df[' score']
popularity=anime_new_df[' popularity']
favorites=anime_new_df[' favorites']


# In[27]:


max(rank)


# In[28]:


max(score)


# In[29]:


max(popularity)


# In[30]:


max(favorites)


# In[31]:


sns.set_style("darkgrid")

plt.figure(1)
plt.title("Score Vs Rank")
plt.xlabel("Score")
plt.ylabel("Rank")
plt.plot(score, rank, "og")


# In[32]:


plt.figure(2)
plt.title("Score Vs Popularity")
plt.xlabel("Score")
plt.ylabel("Popularity")
plt.plot(score, popularity, "og")


# In[33]:


plt.figure(3)
plt.title("Rank Vs Popularity")
plt.xlabel("Rank")
plt.ylabel("Popularity")
plt.plot(rank, popularity, "og")


# In[34]:


plt.figure(4)
plt.title("Rank Vs Favorites")
plt.xlabel("Rank")
plt.ylabel("Favorites")
plt.plot(rank, favorites, "og")


# In[35]:


plt.figure(5)
plt.title("Popularity Vs Favorites")
plt.xlabel("Popularity")
plt.ylabel("Favorites")
plt.plot(popularity, favorites, "og")


# In[36]:


plt.figure(6)
plt.title("Score Vs Favorites")
plt.xlabel("Score")
plt.ylabel("Favorites")
plt.plot(score, favorites, "og")


# In[37]:


plt.figure(7)
plt.title("Score Vs Rank Vs Popularity")
sns.scatterplot( score, rank, popularity);


# In[38]:


plt.figure(8)
plt.title("Favourites Vs Rank Vs Popularity")
sns.scatterplot( favorites, rank, popularity);


# In[39]:


plt.figure(9)
plt.title("Score Vs Favorites Vs Popularity")
sns.scatterplot( score, favorites, popularity);


# In[40]:


anime_new_df[' genre'].unique()


# In[41]:



import numpy as np

genreArray=np.array(anime_new_df[' genre'].unique())
print("Shape", genreArray.shape)
print(genreArray)


# In[42]:


for genres in genreArray:
    print(genres)
    print(len(genres))


# In[43]:


import ast

genre_dict = {}

ind=0;
for genres in genreArray:
    genreList = ast.literal_eval(genres) 
    print("Length ",ind,": ", len(genreList))
    for genre in genreList:
        if genre in genre_dict:     
            genre_dict[genre]+=1
        else:
            genre_dict[genre]=1       
        print(genre)
    print("\n")
    ind+=1


# In[44]:


genre_dict


# In[45]:


print("Total genre is ", len(genre_dict), " in this anime dataset")


# In[47]:



genre_dict={k: v for k, v in sorted(genre_dict.items(), key=lambda item: item[1])}
genre_dict


# In[48]:


pieLabels=["%s" % key for key in genre_dict]
pieValues=["%d" % genre_dict[key] for key in genre_dict]


# In[49]:


pieLabels, pieValues


# In[50]:





figureObject, axesObject = plt.subplots(figsize=(20, 10))

box = axesObject.get_position()
axesObject.set_position([box.x0, box.y0, box.width * 1.3, box.height])


axesObject.pie(pieValues,labels=pieLabels,autopct='%1.2f', startangle=90, radius=200, frame=True)



axesObject.axis('equal')

plt.title("Anime Genre and its respective count")
plt.show()


# In[51]:



        


fig = plt.figure(figsize=(20,10))
ax = fig.add_axes([0,0,1,1])

y_pos = np.arange(len(pieLabels))

ax.barh(y_pos, pieValues, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(pieLabels)
ax.invert_yaxis() 
ax.set_xlabel('Count')
ax.set_title('Genre Anime')

plt.show()


# In[52]:


anime_new_df[' producers'].unique()


# In[53]:


producerArray=np.array(anime_new_df[' producers'].unique())
print("Shape", producerArray.shape)
print(producerArray)


# In[54]:




producer_dict = {}

ind=0;
for producers in producerArray:
    producerList = ast.literal_eval(producers) 
    print("Length ",ind,": ", len(producerList))
    for producer in producerList:
        if producer in producer_dict:      
            producer_dict[producer]+=1
        else:
            producer_dict[producer]=1       
        print(producer)
    print("\n")
    ind+=1


# In[55]:


producer_dict


# In[56]:


print("Total producer is ", len(producer_dict), " in this anime dataset")


# In[57]:



producer_dict={k: v for k, v in sorted(producer_dict.items(), key=lambda item: item[1])}
producer_dict


# In[58]:


print("Highest number producer: ", max(producer_dict, key=producer_dict.get), "with count: ", producer_dict[max(producer_dict, key=producer_dict.get)])


# In[59]:


producerList=[]
for key, value in producer_dict.items():
    temp = [key,value]
    producerList.append(temp)


# In[60]:


producerList


# In[61]:


producer_df=pd.DataFrame(producerList, columns = ["Producer", "Count"]) 
producer_df


# In[62]:


producer_top10_df=producer_df.sort_values("Count").tail(10)
producer_top10_df


# In[63]:


plt.title("Top 10 Anime Producer")

sns.barplot('Count', 'Producer', data=producer_top10_df);


# In[64]:


anime_new_df


# In[65]:


source_df=anime_new_df.groupby(' source')[[' favorites']].mean()
source_df


# In[66]:


import matplotlib
matplotlib.rcParams['figure.figsize'] = (10, 10)

source_df.plot.area();


# In[67]:


source_df.plot.pie(y=" favorites")


# In[ ]:




