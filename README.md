# Sentiment Analysis for twitter using nltk
1. Use the twitter_to_mongo.py to extract the data from twitter.
2. Run analysis.py to realise the word count and sentiment analysis.
3. The training set was labelled manually using manual_labelling.py.

## twitter_to_mongo.py
The data was collected from twitter by Twitter API. The keywords is #FIFA, #WorldCup, World Cup, Russia2018.\
pymongo and tweepy are used.

## analysis.py
The main function for word count and sentiment analysis.\
The result of word count and sentiment analysis will be displayed.\
The tweets will be classified into postive, negtive and natural.

## mongo_operation.py
Retrive the data from the mongoDB.\
pymongo is used.

## text_preprocessing.py
This file contains several functions to process the raw data: data cleansing(remove html tag, urls etc.), 
tokenise, lemmatize, remove the stop words, and word count.\
nltk, re and WordNet are used.

## sentiment_classifier.py
The functions related to sentiment analysis: collect training data, extract features, train the model, classfy the data.\
NaiveBayes is applied to categorise the data.\
The bag of words are used as the features.\
nltk is used.

## manual_labelling.py
The sentiments of the tweets was labelled manually by myself. I only labelled 200 of them. As a result, the training set is unbalanced. Most of them are natural.
