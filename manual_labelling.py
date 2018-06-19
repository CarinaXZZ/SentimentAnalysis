import mongo_operation
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.WorldCupData # database: WorldCupData
collection = db.train # collection: tweets

data = mongo_operation.retrieve_data('WorldCupData', 'tweets', 'text')
count = 0
# list = ['pos', 'n','n','neg','n','n','pos','n','n','neg','pos','n','pos','pos','pos','pos', 'n','neg','neg','n','neg','pos','n','neg','n','n','pos','n','pos','n','neg','n','pos','pos','pos', 'n','n','pos','n','pos','neg','n','n','n', 'n', 'pos', 'pos','pos','n','n','n','n','n','n','neg','n','n','n','n','pos','pos','neg','n','n','neg','n','neg','n','pos','pos','pos','pos','pos','pos','n','n','n','n','neg','n','pos','pos','n','n','n','pos','neg','neg','neg','n','pos','n','n','n','pos','n','n','neg','n','n']
# list = ['n','n','pos','n','n','n', 'n','n','n','n','n','pos','pos','neg','pos','pos','pos','pos','pos','n','pos','n','n','n','n','pos','n','n','neg','n','pos','n','n','n','pos','n','neg','neg','n','pos','pos','pos','n','n','n','n','n','n','pos','n','pos','n','n','pos','pos','pos','pos','n','n','pos','n','n','n','n','pos','n','n','n','n','pos','n','pos','n','pos','n','n','neg','n','n','n','n','n','pos','n','neg','n','n','n','neg','n','n','n','n','n','n','neg','n','n','n','n']
# print(len(list))

# label the training set
count = 0
for d in data[:200]:
    data_train = {'text': d['text'], 'label':list[count]}
    # print(data_train)
    collection.save(data_train)
    count += 1


data = mongo_operation.retrieve_data('WorldCupData', 'train', 'label')
count = 0
for d in data:
    print('No.' + str(count) + ': ' + d['label'])
    count += 1

# create test set
collection = db.test
for d in data[200:1000]:
    data_test = {'text': d['text']}
    collection.save(data_test)
print('done')


data = mongo_operation.retrieve_data('WorldCupData', 'test', 'text')
count = 0
for d in data:
    print(d['text'])
    count += 1

