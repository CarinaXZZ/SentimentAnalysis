
# from pymongo import MongoClient
# import nltk
# import re
# from nltk.stem import WordNetLemmatizer
import mongo_operation
#
#
# client = MongoClient('localhost', 27017)
#
# db = client.TwitterStream
# # db.authenticate("myUserAdmin", "abc123")
# my_set = db.tweets
# # my_set.insert({"name":"zhangsan","age":18})
# count = 0
#
data = mongo_operation.retrieve_data('TwitterStream', 'tweets', 'text')
# data.append(my_set.find({},{'username':1, '_id':0}))
for d in data:
    print(d['text'])
# # for i in my_set.find({},{'text':1,'_id':0}):
#     # count += 1
#     # # print(i[u'text'])
#     # # print(len('Were getting pretty excited for our'))
#     # print(count)
#     # print(i['text'])
# #     text += i['text']
# # fdist = nltk.FreqDist(nltk.word_tokenize(text))
# # fdist.plot(30, cumulative=True)
#
#
# #
# # emoticons_str = r"""
# #     (?:
# #         [:=;] # Eyes
# #         [oO\-]?
# #         [D\)\]\(\]/\\OpP]
# #     )"""
# #
# # regex_str = [
# #     emoticons_str,
# #     r'<[^>]+>',  # HTML tags
# #     # r'(?:@[\w_]+)',  # @-mentions
# #     # r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
# #     # r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs
# #     #
# #     # # r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
# #     # r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
# #     # # r'(?:[\w_]+)',  # other words
# #     # # r'(?:\S)'  # anything else
# #     r'[^\w\s]'
# # ]
# #
# # tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
# # emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)
# # # re.sub(r'(.)\1+', r'\1\1', word)
# #
# # def tokenize(s):
# #     return tokens_re.findall(s)
# #
# #
# # def preprocess(s, lowercase=False):
# #     tokens = tokenize(s)
# #     if lowercase:
# #         tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
# #     return tokens
# #
# # # print(text)
# # # tweet = 'RT @marcobonzanini: just an example! :D http://example.com #NLP'
# # # # print(preprocess(text))
# # # # t = re.sub(r'[^\w\s]','',text)
# # # print preprocess(text)
# # # fdist = nltk.FreqDist(preprocess(text))
# # # fdist.plot(30, cumulative=True)
# #
# # text = "fuuuuuuuuny @indon #dafa'll"
# # aaa = re.compile(r'(.)\1+')
# # print(aaa.sub(r'\1\1',text))
# # # hash_tag = re.compile("(?:\#+[\w_]+[\w\'_\-]*[\w_]+)")
# # # print(hash_tag.sub('',text))
# # # print(re.sub(r'(.)\1+', r'\1\1', text))
# # abb_ll = re.compile("(?<=[a-zA-Z])\'ll")
# # new_text = abb_ll.sub(' will', text)
# # print(new_text)
# #
# # lemmatizer = WordNetLemmatizer()
# # print(lemmatizer.lemmatize('coaches'))
a= [1,2,3,4,5]
b= [6,7,8,9,10]

