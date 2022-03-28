import urllib.request
import re
import string

# Part 1: Harvesting text from the Internet

# Getting the book The prince by Niccolo Machiavelli using professor's code.
url = 'https://www.gutenberg.org/files/1232/1232-0.txt'
response = urllib.request.urlopen(url)
data = response.read()  # a `bytes` object
prince_text = data.decode('utf-8')

# Getting the book The Republic by Plato using professor's code.
url = 'https://www.gutenberg.org/cache/epub/1497/pg1497.txt'
response = urllib.request.urlopen(url)
data = response.read()  # a `bytes` object
republic_text = data.decode('utf-8')

# Part 2: Analyzing Your Text


def text_clean(book):
    """Function to clean text by making everything lowercase and remove all punctuation."""
    words = book.lower()

    # punc = "!()-[]{;:'\,<>./?@#$%^&*_~"
    # I tried to use a nested for loop to see if each letter was there in the punc string and the replace it with nothing but that did not work.
    # So i used regex from the article https://www.geeksforgeeks.org/python-remove-punctuation-from-string/
    words = re.sub(r'[^\w\s]', '', words)

    words = words.split()
    return words


def word_count(book):
    """Function to find the frequency of each word in the text and do some analysis with it"""
    total_words = len(book)

    print("The total words in the book are:", total_words, "words")

    word_counts = {}
    for word in book:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    total_unique_words = len(word_counts)

    print("The total unique words in the book are:", total_unique_words, "words")

    # figured out how to find top 10 words from https://docs.python.org/3/howto/sorting.html
    s = sorted(word_counts.items(),
               key=lambda item: item[1], reverse=True)[0:10]
    print("The ten most frequently used words in the book are:")
    print(s)

    s = sorted(word_counts.items(),
               key=lambda item: item[1], reverse=False)[0:10]
    # Just printing the first 10 as there are many words that appear once.
    print("The ten least frequently used words in the book are:")
    print(s)


def sentiment_analysis():
    """Function to do the the sentiment analysis of a sting"""
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    score = SentimentIntensityAnalyzer().polarity_scores(prince_text)
    print("The sentiment analysis of \"The Prince\" is:")
    print(score)
    score = SentimentIntensityAnalyzer().polarity_scores(republic_text)
    print("\nThe sentiment analysis of \"The Republic\" is:")
    print(score)


def text_similarity():
    """Function to find the similarity percentage between two stings"""
    # I have spent hours trying to get this function to work. I used a variety of methods to find the Levenshtein distance but they all did not work. 
    # I had to resort to using the inbuilt function sequencematcher which is very slow and not at all acurate. 
    # from thefuzz import fuzz
    # print(fuzz.ratio(prince_text, republic_text))
    from difflib import SequenceMatcher

    print("\nThe similarity between the two text is:")
    print(SequenceMatcher(None, prince_text, republic_text).ratio()*100, "%")


cleaned_prince_text = text_clean(prince_text)
cleaned_republic_text = text_clean(republic_text)
print("----ASSSIGNMENT 2----")
print("\nIndividual Analysis:")
print("\n||The Prince- Nicollo Machiavelli||\n")
word_count(cleaned_prince_text)
print("\n||The Republic- Plato||\n")
word_count(cleaned_republic_text)
print("\nCombined Analysis:\n")
sentiment_analysis()
text_similarity()
