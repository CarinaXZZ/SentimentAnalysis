from pymongo import MongoClient


def retrieve_data(database, collection, field):
    '''
    This function retrieved the data from mongoDB.

    :param database:
    :param collection:
    :param field:
    :return:
    '''
    client = MongoClient('localhost', 27017) # connect mongodb
    db = client[database] # connect the database
    my_set = db[collection] # connect the collection
    return my_set.find({}, {field:1, '_id':0})


def get_all_in_string(data, field):
    '''
    This function combine all the tweets into one string
    for future processing.

    :param data:
    :param field:
    :return text: string
    '''
    text = ""
    for i in data:
        text += i[field]

    return text

