import mongo_operation
import text_processing
import nltk


# MongoDB for data
# Database: WorldCupData
# Collections: train(training set)
# Fields: text(the text of the tweets), label(sentiment of the tweets)
DATABASE = 'WorldCupData'
TRAININGSET = 'train'
TEXT = 'text'
LABEL = 'label'


def get_trainingset(trainingset):
    '''
    This function is used to transform the tweets
    into tokens and label respectively.

    :param trainingset: the name of the collection of the training set
    :return trainingdata: list of the tweets and labels
    '''
    tweet, label, traindata= [], [], []
    text = mongo_operation.retrieve_data(DATABASE, trainingset, TEXT)
    labelling = mongo_operation.retrieve_data(DATABASE, trainingset, LABEL)

    for value in text:
        data = text_processing.data_preprocessing(value[TEXT])
        data = text_processing.remove_stopwords(data)
        tweet.append(data)
    for value in labelling:
        label.append(value[LABEL])

    for i in range(0, len(label)):
        traindata.append((tweet[i],label[i]))

    return traindata


def get_features(trainingset):
    '''
    This function can find all the tokens as the feature
    in the training data.

    :param trainingset: the name of the collection of the training set
    :return: the tokens appear in the training set
    '''
    traindata = get_trainingset(trainingset)
    data = []
    for (tweets, label) in traindata:
        data.extend(tweets)

    wordlist = nltk.FreqDist(data)

    return wordlist.keys()


word_features = get_features(TRAININGSET)


def extract_features(document):
    '''
    This function is use to extract the features from the tweets.

    :param document: document to classify
    :return features: the list of features
    '''
    document_words = set(document)
    features = {}
    for word in word_features:
        features[word.decode("utf8")] = (word in document_words)
    return features

traindata = get_trainingset(TRAININGSET)
trainingset = nltk.classify.apply_features(extract_features, traindata)
classifier = nltk.NaiveBayesClassifier.train(trainingset)

def classify(tweet):
    '''
    This function is used to return the label of the tweets.

    :param tweet: the tokens of the tweets
    :return: the sentiment of the tweet
    '''
    print('sentiment ananlysis: ' + classifier.classify(extract_features(tweet)))


def sentiment_analysis(data, field):
    '''
    This function is used to preprocess the tweets
    and classify the tweets.

    :param data:
    :param field:
    '''
    for d in data:
        tweet = text_processing.data_preprocessing(d[field])
        tweet = text_processing.remove_stopwords(tweet)
        print('Tweets: ' + d[field])
        classify(tweet)