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

# from thefuzz import fuzz
# test= fuzz.ratio(prince_text, republic_text)
# print(test)
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
# score = SentimentIntensityAnalyzer().polarity_scores(prince_text)
# print(score)
# score = SentimentIntensityAnalyzer().polarity_scores(republic_text)
# print(score)
# print(prince_text)
from difflib import SequenceMatcher

# def similar():
#     return SequenceMatcher(None, prince_text, republic_text).ratio()

# from diff_match_patch import diff_match_patch

# def compute_similarity_and_diff():
#     dmp = diff_match_patch()
#     dmp.Diff_Timeout = 0.0
#     diff = dmp.diff_main(prince_text, republic_text, False)

#     # similarity
#     common_text = sum([len(txt) for op, txt in diff if op == 0])
#     text_length = max(len(prince_text), len(republic_text))
#     sim = common_text / text_length

#     return sim, diff
# # print(similar())

# print(compute_similarity_and_diff())

# from nltk.corpus import stopwords
# # nltk.download('stopwords')
# from nltk.tokenize import word_tokenize


# text_tokens = word_tokenize(prince_text)

# tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]

# print(tokens_without_sw)
