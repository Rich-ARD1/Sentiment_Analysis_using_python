#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

filepath = r'C:\PBN\Python class\articles.xlsx'

Data = pd.read_excel(filepath)


# In[25]:


Data.head()


# In[26]:


# Summary of data
data_summary = Data.describe()

# Column Summary
data_info = Data.info()
print(data_info)


# In[27]:


# Counting by source (Number of articles) with groupby function
article_count_by_source = Data.groupby(['source_id'])['article_id'].count()
print(article_count_by_source)


# In[28]:


# Count by engagement, Group by source (Publisher)
engagement_by_source = Data.groupby(['source_id'])['engagement_reaction_count'].sum()
print(engagement_by_source)


# In[29]:


# Drop a column
Data = Data.drop('engagement_comment_plugin_count', axis=1)

New_data = Data.copy()

# Function to calculate keyword flag
def calculate_keyword_flag(keyword):
    keyword_flag = []
    for heading in Data['title']:
        if keyword in str(heading):
            flag = 1
        else:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag

# Create new column for the Flag
New_data['Keyword_flag'] = pd.Series(calculate_keyword_flag('murder'))


# In[30]:


# SentimentIntensityAnalyzer
sent_int = SentimentIntensityAnalyzer()

# Loop through table to extract sentiment per title
title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []

for title in Data['title']:
    sent = sent_int.polarity_scores(str(title))
    neg = sent['neg']
    pos = sent['pos']
    neu = sent['neu']
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)


# In[31]:


# Add sentiment scores as new columns
New_data['title_neg_sentiment'] = pd.Series(title_neg_sentiment)
New_data['title_pos_sentiment'] = pd.Series(title_pos_sentiment)
New_data['title_neu_sentiment'] = pd.Series(title_neu_sentiment)
New_data.head()


# In[32]:


# Store cleaned data as Excel file
New_data.to_excel('blog_me_cleaned.xlsx', sheet_name='blogmedata', index=False)
