'''Analysisng the Sentiment of the writer from their tweets
using negative and positive words used in the sentence'''

# getting all the positive word from file
positive_words = []
with open('./positive_words.txt', 'r') as file:
    '''loop through the file '''
    for line in file:
        if line[0] != ';' and line[0] != '\n': # append the line which does not contain ; or \n
            positive_words.append(line.strip())

# getting all the negative word from file--
negative_words = []
with open('./negative_words.txt', 'r') as file:
    '''loop through the file collecting all the negative word'''
    for line in file:
        if line[0] != ';' and line[0] !='\n': # append the line which does not contain ; or \n
            negative_words.append(line.strip())

def strip_punctuation(string):
    '''remove punctuation from the string'''
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

    for char in string:
        if char in punctuation_chars:
           string = string.replace(char, '')

    return string
#-----------------------------------------------

def get_pos(line):
    '''calculate the positive word frequency'''
    pos_count = 0
    for word in strip_punctuation(line.strip()).split():
        if word.lower() in positive_words:
            pos_count += 1

    return pos_count
#----------------------------------------------

def get_neg(line):
    '''calculate the negative word frequency'''
    neg_count = 0
    for word in strip_punctuation(line.strip()).split():
        if word.lower() in negative_words:
            neg_count += 1

    return neg_count
#----------------------------------------------

def tweet_classifier():
    tweet_data = []

    with open('./project_twitter_data.csv', 'r', encoding='utf-8') as csv_file:
        lines = csv_file.readlines()
        header = lines[0]


        for line in lines[1:]:
            tweet_value = line.strip().split(',')
            n_count = get_neg(tweet_value[0]) # get the negative word count from the tweet
            p_count = get_pos(tweet_value[0]) # get the positive word count from the tweet

            total_count = p_count - n_count # get the net count

            tweet_data.append((tweet_value[1], tweet_value[2], p_count, n_count, total_count)) # list of tuple of tweet data

    header = 'Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score'
    with open('./resulting_data.csv', 'w') as csv_file:
        csv_file.write(header)
        csv_file.write('\n')

        for data in tweet_data:
            csv_file.write('{}, {}, {}, {}, {}\n'.format(*data)) # write the data to the file
#---------------------------------------------------------------


tweet_classifier()
