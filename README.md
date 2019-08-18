# Sentiment-Analysis-on-Swachh-Bharat-using-Twitter

In this project, I performed Sentiment analysis on tweets of Swachh Bharat. 

Summary:
Tweets are collected using Tweepy library followed by the selection of useful features to my task and conversion to CSV. Then, data cleaning is performed like removing URLs, retweet symbols, username-tags, and hashtags. SentiWordNet lexicon is used to label the sentiment of the tweets. Steps like Stop words removal, Lemmatizing, Stemming are performed on the text data. Later, WordCloud is used for Data Visualization. After splitting the data, Count Vectorizer and Tfidf Vectorizer are used for mathematical representation of the text. Then, nine classification algorithms are implemented on the vectors obtained previously. Later, doc2vec models (DBOW, DMC, DMM) are trained and used vectors (obtained through these models)for classification purpose as these models preserve semantic relationships between words. Finally, the best model is evaluated using the test data.




An elaborate discussion of this project(and code) can be found in the following article. https://medium.com/@IAmTheTime/sentiment-analysis-on-swachh-bharat-using-twitter-216369cfa534 
