# Sentiment_Analysis_using_python
# Data Analytics on Blogme
This repository contains a Python script for preprocessing and analyzing data related to articles fetched from various sources. The script performs tasks such as data cleaning, summarization, grouping, keyword flagging, and sentiment analysis on article titles. Additionally, it provides functionality to export the cleaned data into an Excel file for further analysis.

# Usage 

This script is designed to preprocess and analyze article data stored in an Excel file. After running the script, it generates a cleaned Excel file with additional columns for keyword flags and sentiment scores.

# Data Format

Ensure that your article data is stored in an Excel file (articles.xlsx) in the following format:

article_id	source_id	title	engagement_reaction_count
1	101	Title of Article 1	25
2	102	Title of Article 2	15
...	...	...	...
article_id: Unique identifier for each article.
source_id: Identifier for the source/publisher of the article.
title: Title of the article.
engagement_reaction_count: Number of reactions/engagements received on the article.

# Installtion

Install the required Python libraries:

pip install pandas
pip install vaderSentiment

# Acknowledgments

This project utilizes the Pandas library for data manipulation and analysis.
Sentiment analysis is performed using the VADER library.

# Additional Information

For more details on the project, refer to the script (blogme_analysis.py) and the provided sample files (articles.xlsx, blog_me_cleaned.xlsx).
