import text_processing
import mongo_operation
import sentiment_classifier


# MongoDB for data
# Database: WorldCupData
# Collections: tweets(all the tweets), train(training set), test(test set)
# Field: text(the text of the tweets)
DATABASE = 'WorldCupData'
COLLECTION = 'tweets'
TRAININGSET = 'train'
TESTSET = 'test'
field = 'text'

# word count
data = mongo_operation.retrieve_data(DATABASE, COLLECTION, field)
data_string = mongo_operation.get_all_in_string(data, field)
text = text_processing.data_preprocessing(data_string)
text_processing.word_count(text)
# text = text_processing.remove_stopwords(text)
# word_count(text)

# sentiment analysis
testset = mongo_operation.retrieve_data(DATABASE, TESTSET, field)
sentiment_classifier.sentiment_analysis(testset, field)
