import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk


def lemmatization(text):
    '''
    This function used the WordNet to lemmatize the tokens of the tweets.

    :param text: the token of the tweets
    :return: the tokens after lemmatization
    '''
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(t) for t in text]
    return tokens


def tokenize(text):
    '''
    Return tokens of the text.

    :param text:
    :return: tokens
    '''
    return nltk.word_tokenize(text)


def clean_data(text):
    '''
    This function used the regex to remove the redundant information
    and adapt the abbreviation of the tweets.

    :param text:
    :return new_text:
    '''
    html_tag = re.compile('<[^>]+>') # html-tag
    urls = re.compile('http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+') # URLs
    numbers = re.compile('(?:(?:\d+,?)+(?:\.?\d+)?)') # numbers
    mention = re.compile('(?:@[\w_]+)') # mention-@
    hash_tag = re.compile("(?:\#+[\w_]+[\w\'_\-]*[\w_]+)") # hash-tag
    ascii = re.compile('[^\x00-\x7F]+') # ASCII
    repeating_c = re.compile(r'(.)\1+') # repeating charaters
    abb_s1 = re.compile("(it|he|she|that|this|there|here)(\'s)", re.I) # abbreviation 's for is
    abb_s2 = re.compile("(?<=[a-zA-Z])\'s") # abbreviation 's after subject
    abb_s3 = re.compile("(?<=s)\'s?") # abbreviation s'
    abb_t = re.compile("(?<=[a-zA-Z])n\'t") # abbreviation 't for not
    abb_d = re.compile("(?<=[a-zA-Z])\'d") # abbreviation 'd for would
    abb_ll = re.compile("(?<=[a-zA-Z])\'ll") # abbreviation 'll for will
    abb_m = re.compile("(?<=[I|i])\'m") # abbreviation 'm for am
    abb_re = re.compile("(?<=[a-zA-Z])\'re") # abbreviation 're for are
    abb_ve = re.compile("(?<=[a-zA-Z])\'ve") # abbreviation 've for have
    punctuation = re.compile('[^\w\s]') # punctuation

    # replace above with ...
    new_text = html_tag.sub('', text.lower())
    new_text = urls.sub('', new_text)
    new_text = numbers.sub('', new_text)
    new_text = mention.sub('', new_text)
    new_text = hash_tag.sub('', new_text)
    new_text = ascii.sub('', new_text)
    new_text = repeating_c.sub(r'\1\1', new_text)
    new_text = abb_s1.sub(r'\1 is', new_text)
    new_text = abb_s2.sub('', new_text)
    new_text = abb_s3.sub('', new_text)
    new_text = abb_t.sub(' not', new_text)
    new_text = abb_d.sub(' would', new_text)
    new_text = abb_ll.sub(' will', new_text)
    new_text = abb_m.sub(' am', new_text)
    new_text = abb_re.sub(' are', new_text)
    new_text = abb_ve.sub(' have', new_text)
    # new_text = new_text.replace('-', ' ')
    # new_text = new_text.replace('.', ' ')
    new_text = punctuation.sub(' ', new_text)

    return new_text


def data_preprocessing(text):
    '''
    This function preprocesses the data.
    Including clean the data, tokenize and lemmatization.

    :param text: tweets
    :return tokens: the tokens after processed
    '''
    new_text = clean_data(text)
    tokens = tokenize(new_text)
    tokens = lemmatization(tokens)

    # print(tokens)
    return tokens

def remove_stopwords(tokens):
    '''
    This function remove the stopwords using nltk.

    :param tokens:
    :return clean_tokens: token after processed
    '''
    clean_tokens = tokens[:]
    sw = stopwords.words('english')
    for t in tokens:
        # if t in sw:
        #     clean_tokens.remove(t)
        if len(t) <= 2:
            clean_tokens.remove(t) # remove the word which length is less than 2

    # print(clean_tokens)
    return clean_tokens


def word_count(tokens):
    '''
    This function is used to count the words respectively,
    print the result, and plot the first 30 words with highest frequency.

    :param tokens:
    :return:
    '''
    freq = nltk.FreqDist(tokens)
    for key, val in freq.items():
        print (str(key) + ':' + str(val))
    freq.plot(30)
